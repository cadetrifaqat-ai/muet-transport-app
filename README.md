# MUET Transport — Flask PWA

Minimal instructions to deploy this Flask PWA (MUET Transport) to Render (or any host supporting `gunicorn`). The app already includes PWA files (`manifest.json`, `service-worker.js`, and `static/icons`) so users can install it to Android via "Add to Home screen".

Quick steps (Render)

1. Push this repository to GitHub.
2. Create a new Web Service on Render and connect your GitHub repo.
3. Build command: leave empty (Render will install from `requirements.txt`).
4. Start command: leave empty — Render will use the `Procfile` which contains `web: gunicorn app:app`.
5. Environment: no special vars required. Render provides a `PORT` env var — the app reads it when run directly.
6. Deploy. Render will give you a public HTTPS URL. Open it on Android and choose "Add to Home screen" to install.

Local testing

Install dependencies and run locally:

```bash
python -m pip install -r requirements.txt
python app.py
# then open http://127.0.0.1:5000
```

Notes

- Do not remove any files in `templates/`, `static/` or `muet_transport/data/` — the app relies on them.
- `app.py` at the repository root is a small wrapper that exposes the Flask app as `app` so `gunicorn app:app` works.
- The PWA files are served from `static/` and remain unchanged.
