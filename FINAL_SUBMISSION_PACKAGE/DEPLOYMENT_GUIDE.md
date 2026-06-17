# Fast Deployment Guide for Live Demo (Required for Week 5)

You need a publicly accessible URL for the Streamlit UI.

Fastest free options (recommended order):

## Option 1: Render.com (easiest, ~5-10 minutes)
1. Go to https://render.com and sign up (GitHub login is fastest).
2. New Web Service → Connect your GitHub repo (the one you will push this folder to).
3. Settings:
   - Name: hedera-policy-agent-demo (or anything)
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run demo_ui.py --server.port $PORT --server.address 0.0.0.0`
   - Auto-deploy on push: Yes
4. Add environment variables from .env.example (you can use fake/placeholder keys for the demo if you don't want real testnet calls in the public demo — the UI still shows the policy logic beautifully).
5. Deploy. After it finishes, copy the public URL (something like https://hedera-policy-agent-demo.onrender.com).
6. Keep the service awake (Render free tier sleeps after 15 min inactivity — for the bounty period you can manually ping it or upgrade temporarily if needed).

## Option 2: Streamlit Community Cloud (also free)
1. Push the repo to GitHub first.
2. Go to https://share.streamlit.io/
3. Deploy from GitHub repo, select `demo_ui.py` as the main file.
4. Add secrets if needed.

## Option 3: Railway / Hugging Face Spaces / Fly.io
Any platform that can run a Python web app works. The important thing is a stable public HTTPS URL.

**Important for the bounty**:
- The demo must remain accessible for at least 90 days after the campaign ends.
- Test that the UI actually loads and the policy blocking is visible before submitting.

Once deployed, put the URL in the bounty submission form and in your X post.
