from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import time

Scale = str

@dataclass
class ActiveSchema:
    key: str
    scale: Scale
    weight: float = 0.5
    startedAt: float = field(default_factory=lambda: time.time())
    ttlDays: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    privacy: str = "P2"

def decay(s: ActiveSchema) -> ActiveSchema:
    if s.ttlDays is None or s.scale in ("role","root"):
        return s
    age_days = (time.time() - s.startedAt) / 86400.0
    factor = max(0.0, 1.0 - (age_days / s.ttlDays))
    return ActiveSchema(**{**s.__dict__, "weight": round(s.weight * factor, 4)})

def promote(s: ActiveSchema, repeats: int) -> ActiveSchema:
    if s.scale == "ephemeral" and repeats >= 3:
        return ActiveSchema(**{**s.__dict__, "scale":"seasonal", "ttlDays":60})
    if s.scale == "seasonal" and repeats >= 12:
        return ActiveSchema(**{**s.__dict__, "scale":"track", "ttlDays":365})
    return s
