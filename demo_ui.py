"""
Streamlit Demo UI for Hedera Policy Agent (Week 5)
Live hosted demo required for bounty submission.

Run locally:
  streamlit run demo_ui.py

Deploy to Render / Vercel / Railway for public URL (free tier OK, keep alive 90+ days).
"""

import streamlit as st
import asyncio
import os
from dotenv import load_dotenv

# Import the core from main (or duplicate minimal setup for standalone)
from main import create_policy_agent  # assumes same dir

load_dotenv()

st.set_page_config(page_title="Hedera Policy Agent - Bounty Demo", page_icon="🛡️")
st.title("🛡️ Hedera Policy Agent (Week 5)")
st.caption("Policy-constrained HBAR / USDC payments • Deterministic Hooks & Policies • HITL via RETURN_BYTES • HCS Audit Trail")

st.sidebar.header("Policy Controls (Live)")
max_hbar = st.sidebar.slider("Max HBAR per tx", 1.0, 200.0, 50.0, 1.0)
max_usdc = st.sidebar.slider("Max USDC per tx", 1.0, 200.0, 50.0, 1.0)
whitelist = st.sidebar.text_input("Allowed recipients (comma sep)", "0.0.1234,0.0.9999")
session_limit = st.sidebar.number_input("Max payments per session", 1, 10, 5)

if st.sidebar.button("Reset Session Counter"):
    st.session_state.session_count = 0
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("All enforcement is **deterministic code** (Policies/Hooks), not LLM prompt. RETURN_BYTES mode requires your explicit approval before any tx.")

# Simple session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "approved_txs" not in st.session_state:
    st.session_state.approved_txs = []
if "session_count" not in st.session_state:
    st.session_state.session_count = 0

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask the agent (e.g. 'pay 20 HBAR to 0.0.1234' or 'balance')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run agent (simplified; in real use full async + policy injection from sidebar)
    with st.chat_message("assistant"):
        with st.spinner("Agent thinking + policy check..."):
            try:
                # In production: re-instantiate agent with sidebar params injected into PaymentPolicy
                # Here we show the flow + simulate policy for demo
                response_text = f"**Simulated agent response to:** {prompt}\n\n"
                response_text += "Policy engine evaluated. "

                # Very simplified simulation (real version uses the main.py agent + policy)
                lower = prompt.lower()
                if "balance" in lower:
                    response_text += "Your HBAR balance: 123.45 (testnet). USDC: 67.89."
                elif "pay" in lower or "transfer" in lower or "send" in lower:
                    # Parse rough amount / token
                    amount = 10.0
                    token = "HBAR"
                    recipient = "0.0.1234"
                    # Real parsing would use LLM tool call output
                    if "usdc" in lower:
                        token = "USDC"
                    # Simulate policy
                    if amount > (max_hbar if token == "HBAR" else max_usdc):
                        response_text += f"**BLOCKED by Policy**: Amount exceeds cap ({max_hbar if token=='HBAR' else max_usdc} {token})."
                    elif recipient not in [x.strip() for x in whitelist.split(",") if x.strip()]:
                        response_text += f"**BLOCKED by Policy**: Recipient {recipient} not whitelisted."
                    else:
                        st.session_state.session_count += 1
                        if st.session_state.session_count > session_limit:
                            response_text += "**BLOCKED**: Session limit reached."
                        else:
                            response_text += f"Tx formed (RETURN_BYTES). **Preview**: Send {amount} {token} to {recipient}.\n\n"
                            response_text += "Human approval required before submit."
                            # In real: show Approve button that calls sign/submit on bytes
                            if st.button(f"✅ Approve & Submit {amount} {token} to {recipient}", key=f"approve_{len(st.session_state.approved_txs)}"):
                                st.session_state.approved_txs.append(f"Approved: {amount} {token} → {recipient}")
                                response_text += "\n**SUBMITTED (simulated).** Tx hash would appear here + HCS audit log."
                else:
                    response_text += "Query processed via toolkit (example). Use specific payment language for policy demo."

                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

            except Exception as e:
                err = f"Error: {e}"
                st.error(err)
                st.session_state.messages.append({"role": "assistant", "content": err})

# Audit / History sidebar area
st.markdown("---")
st.subheader("📜 Session Audit (HCS in real version)")
for tx in st.session_state.approved_txs:
    st.success(tx)

st.caption("In full version: Real-time HCS topic query + HashScan links for every action (via audit hook). Blocked attempts also logged for transparency.")

st.info("Deploy this UI publicly for the required 'live demo URL'. Tag @hedera @hedera_devs on X with screenshots/GIF. See README for full submission checklist and terms compliance.")

# Footer
st.markdown("**Bounty entry** • Built with Hedera Agent Kit (Python) • Custom Policies + Hooks + RETURN_BYTES HITL • Testnet • Safe by design")
