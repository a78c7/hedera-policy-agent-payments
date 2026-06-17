"""
Unit tests for the custom PaymentPolicy logic.
These are pure-Python and can run without Hedera deps or credentials.
Run: python3 -m pytest tests/test_payment_policy.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import PaymentPolicy


def test_default_policy_allows_small_transfer():
    policy = PaymentPolicy()
    block, reason = policy.should_block_transfer(10.0, "HBAR", "0.0.1234")
    assert block is False
    assert reason == "OK"


def test_exceeds_hbar_cap_blocks():
    policy = PaymentPolicy(max_hbar=50.0)
    block, reason = policy.should_block_transfer(60.0, "HBAR", "0.0.1234")
    assert block is True
    assert "exceeds cap" in reason


def test_exceeds_usdc_cap_blocks():
    policy = PaymentPolicy(max_usdc=30.0)
    block, reason = policy.should_block_transfer(40.0, "0.0.429274", "0.0.9999")
    assert block is True
    assert "exceeds cap" in reason


def test_non_whitelisted_recipient_blocks():
    policy = PaymentPolicy(allowed_recipients=["0.0.1234"])
    block, reason = policy.should_block_transfer(5.0, "HBAR", "0.0.9999")
    assert block is True
    assert "not in whitelist" in reason


def test_rate_limit_blocks_after_max():
    policy = PaymentPolicy(max_per_session=2)
    # First two should pass
    assert policy.should_block_transfer(1, "HBAR", "0.0.1234")[0] is False
    assert policy.should_block_transfer(1, "HBAR", "0.0.1234")[0] is False
    # Third should block
    block, reason = policy.should_block_transfer(1, "HBAR", "0.0.1234")
    assert block is True
    assert "Rate limit" in reason or "session" in reason.lower()


def test_disallowed_token_blocks():
    policy = PaymentPolicy(allowed_tokens=["HBAR"])
    block, reason = policy.should_block_transfer(10.0, "0.0.429274", "0.0.1234")
    assert block is True
    assert "not allowed" in reason
