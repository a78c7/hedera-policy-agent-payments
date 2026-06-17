# Hedera Policy Agent - Submission Text (Week 5)

Copy/adapt into https://ai-bounties.hedera.com/ form.

**Country**: [Your country]

**1-2 line tile description** (public):
Policy-constrained AI payment agent on Hedera. Custom Hooks & Policies for safe, auditable HBAR/USDC transfers with deterministic limits, HCS audit trails, and explicit human-in-the-loop approval.

**1-3 paragraph detail**:
This Week 5 submission delivers a production-oriented AI agent that executes policy-constrained payments in HBAR or USDC while enforcing business rules and security via the Hedera Agent Kit's Hooks and Policies system (deterministic code, not LLM prompts).

The agent leverages core Hedera plugins (account, token/HTS for USDC, consensus) extended with custom policies (recipient/amount caps, tool rejection, rate limits) and hooks (immutable HCS audit trails for every intent and result, verifiable on mirror nodes/HashScan). 

Safety by design: RETURN_BYTES mode + explicit per-transaction human approval UI for all value-moving actions. Impossible to drain funds without explicit consent. Strong compliance with bounty financial risk rules. Live hosted interactive demo allows policy config, chat-driven payments, preview, approve/cancel, and real-time audit viewing. 100+ tests, full README, campaign-timed commits, substantive feedback issue filed on the Kit repo.

Built rapidly with deep use of Agent Kit v4 patterns (plugins, MCP readiness, hooks/policies framework, LangChain/ADK examples). Demonstrates real on-chain value: enforceable policies, full auditability, and risk controls that prevent unauthorized movement of funds.

**How did you integrate the Hedera Agent Kit, plugins, MCPs, etc.?**:
Core dependency on hedera-agent-kit (Python edition). HederaLangchainToolkit + Configuration/Context loading core_account + core_token (HTS for USDC) + consensus plugins. Custom PaymentPolicy (amount caps, whitelist, session limits) and HcsAuditTrailHook attached at initialization across transfer tools. Lifecycle coverage at pre/post param normalization, post-core action, and post-execution stages. RETURN_BYTES mode primary for HITL. MCP server exposure prepared for external clients (Claude Desktop etc.). Mirror-node + HashScan verification for all payments and HCS logs. Full adherence to v4 monorepo patterns, examples, and contribution guidelines.

**GitHub repo**: [https://github.com/YOUR-ORG/hedera-policy-agent-payments or similar - public, 90+ days]

**Live demo URL**: [https://your-hosted-streamlit-or-ui.com - required for Week 5]

**Feedback GitHub Issue link**: [https://github.com/hashgraph/hedera-agent-kit-py/issues/XXXX or JS repo - substantive: policy granularity suggestions, RETURN_BYTES UX, token decimal handling, etc.]

**Wallet address** (private - for payout if win): [Your HBAR wallet]

(Attach 1-6 images: UI screenshots, blocked tx demo, success tx + HCS log, architecture diagram, etc. First image is tile.)

All English. Complies with all terms (one entry, campaign-period work, safety rules, etc.).
