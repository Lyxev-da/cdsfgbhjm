# Base44 Setup

## What this is
Originally a Replit `webbot`/Selenium script (`main.py`) — not a web app. It was turned into a **browser sandbox**: a Flask web app that renders an address bar + iframe so you can browse to any URL from the preview.

## Running it
```
docker compose -f docker-compose.base44.yml up -d
```
- Flask dev server on host port 3000, bind 0.0.0.0.
- `app.py` is the entire app; `requirements.txt` has Flask.
- The `python:3.12-slim` image installs deps on each start via the compose `command:`.

## Notes
- Many sites send `X-Frame-Options` / CSP headers that block iframe embedding — those will show a blank frame with the "Some sites block embedding" note. This is a browser/security limitation, not a bug.
- The default URL is `https://3kh0.github.io`; pass `?url=https://...` to change it.
- `main.py` is the original script, left untouched.
