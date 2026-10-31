# apiheal dummy repository

A local demo repository with a deliberately legacy OpenAI integration and a
representative Gemini permission error. This is synthetic demo content, not a
live provider incident. No credentials are included or needed for these commands.

Files:

- `app.py`: synchronous `openai.ChatCompletion.create` and legacy response access.
- `requirements.txt`: pinned legacy OpenAI SDK (`0.28.1`).
- `logs/gemini-permission.log`: synthetic, sanitized error for offline diagnosis.

Run these commands from the sibling `apiheal` project in PowerShell:

```powershell
.\.venv\Scripts\apiheal.exe scan ..\apiheal-demo
.\.venv\Scripts\apiheal.exe repair ..\apiheal-demo --dry-run
.\.venv\Scripts\apiheal.exe diagnose ..\apiheal-demo --log ..\apiheal-demo\logs\gemini-permission.log
```

Expected results:

- Scan reports one repairable legacy chat-completion call (exit code 1).
- Dry run saves an unverified source/dependency migration diff (exit code 0).
- Diagnosis reports manual action with uncertainty (exit code 1).

The demo starts with a committed, clean baseline. apiheal keeps this checkout
unchanged and saves run artifacts outside it under `~/.apiheal/runs`.
Container verification and PR publishing are not implemented in the current
apiheal release. Do not install dependencies or make live provider calls to
exercise these static/demo features.
