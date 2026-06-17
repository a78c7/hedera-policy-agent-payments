# Feedback Issue Draft (Open this on the official Hedera Agent Kit repo)

**Repository to open on**: https://github.com/hashgraph/hedera-agent-kit-py (or the JS repo)

**Title suggestion**:
Enhance payment policy granularity and RETURN_BYTES preview UX for token decimals + amount validation

**Body** (copy and post as a new Issue, preferably using the "agent_kit_feedback" template if available):

During implementation of a policy-constrained payment agent for the current AI Studio bounty, I found the following areas where the hooks/policies system could be even stronger:

1. Token amount handling in policies: When using HTS fungible tokens (USDC etc.), it would be very helpful to have built-in helpers for decimal-aware amount parsing/validation inside AbstractPolicy, so custom policies don't have to re-implement decimal math every time.

2. Better support / examples for RETURN_BYTES + policy evaluation: Currently policies run before bytes are returned, but giving the policy context richer pre-sign information (exact final transaction details) would allow even stricter guardrails.

3. HCS Audit Hook improvements: Ability to easily log in RETURN_BYTES mode (without executing) would be useful for compliance/audit use cases.

I built a working custom PaymentPolicy + HcsAuditTrailHook that successfully blocks bad transfers at the policy layer while still providing a great UX in a hosted demo. Happy to share the implementation or discuss further if the team is interested.

This feedback comes from real production-oriented usage during the bounty.

**Labels**: enhancement, policy, feedback, bounty

**After posting**: Copy the issue URL and put it in the bounty submission form. This is a required deliverable.