# Evals

`scenarios.json`: 154 scenarios, two per skill. Shape:

```json
{"id": "...", "skill": "...", "user_prompt": "...", "expected_skill": "...",
 "expected_tools": ["get_connection", "...", "quote_generation"],
 "stop_condition": "waits for approval before generate", "pass": "...", "fail": "..."}
```

`python3 scripts/validate_skills.py --evals` checks every scenario names a real skill and real tools. Running them needs a fresh session with the plugin and Sloosh connected; see `docs/TESTING.md` for scoring. Record results in `verdicts.md` (create it on first run): `date · id · pass|partial|fail · one line`.
