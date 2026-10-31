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
To verify the supported migration after installing/starting Linux Docker:

```powershell
.\.venv\Scripts\apiheal.exe setup-runner
.\.venv\Scripts\apiheal.exe repair ..\apiheal-demo --verify
```

Verification uses the actual SDKs with a local mock HTTP server inside isolated
containers. It does not call a live provider or require provider credentials.
Missing Docker/images or failed/indeterminate checks stop verification.

Draft PR publishing is implemented with `--verify --pr` for a real GitHub
checkout. This local demo has no GitHub remote, so it cannot publish a PR.
