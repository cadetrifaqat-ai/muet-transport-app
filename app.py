"""Wrapper module exposing the Flask app at module-level name `app`.

This lets gunicorn start the app with `gunicorn app:app` from the
project root while keeping the existing package layout.
"""
from muet_transport.app import app

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # Use 0.0.0.0 so Render (or other hosts) can bind to the container
    app.run(host="0.0.0.0", port=port, debug=True)
