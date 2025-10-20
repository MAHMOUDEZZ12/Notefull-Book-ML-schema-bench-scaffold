#!/usr/bin/env bash
set -euo pipefail
python - <<'PY'
from sm.memory import ActiveSchema
from fr.planner import plan
schemas = [
    ActiveSchema(key="AI_User", scale="track", weight=0.8, tags=["llm","nightlife"]),
    ActiveSchema(key="Old_Device", scale="role", weight=0.6, tags=["<=2020"]),
    ActiveSchema(key="Partying", scale="seasonal", weight=0.7, ttlDays=90, tags=["nightlife"])
]
print("Planned steps:", plan("launch phone market brief", schemas))
PY
echo "OK")
