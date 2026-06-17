# Hedera Repo and Demo Deployment Status

**GitHub Repository (created and pushed via gh CLI as direct execution):**
https://github.com/a78c7/hedera-policy-agent-payments

All code, FINAL_SUBMISSION_PACKAGE, render.yaml, tests, etc. are now public.

**Next for Live Demo (per DEPLOYMENT_GUIDE.md priority: Render):**

The repo now includes `render.yaml` for simplified deployment.

To get the Demo URL:

1. Go to https://render.com (log in with GitHub — the same account used for the repo).

2. Click "New +" → "Web Service".

3. Connect the repo: a78c7/hedera-policy-agent-payments (or search for hedera-policy-agent-payments).

4. Render should auto-detect the render.yaml. If not, use these manual settings:
   - Name: hedera-policy-agent-demo
   - Environment: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: streamlit run demo_ui.py --server.port $PORT --server.address 0.0.0.0
   - Auto Deploy: Yes

5. In Environment variables, you can add placeholders from .env.example (or leave for demo — the UI shows policy enforcement even with placeholders).

6. Deploy.

7. Once live, the URL will be something like: https://hedera-policy-agent-demo.onrender.com

**Important**:
- Test that the demo loads and you can see the policy blocking behavior.
- The demo must stay accessible for 90+ days.

Once you have the live Demo URL, reply with it (and confirm the GitHub link above).

Then we can move to the Hedera form submission step (you will confirm before I give the exact login/submit instructions).

Repo is ready. Deploy the demo on Render to get the URL.
