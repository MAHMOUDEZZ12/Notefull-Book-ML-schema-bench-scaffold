from typing import List
from sm.memory import ActiveSchema

def plan(task: str, schemas: List[ActiveSchema]) -> List[str]:
    keys = {s.key: s.weight for s in schemas}
    steps = []
    if "AI_User" in keys:
        steps.append("tool.search_ai_topics")
    if "Old_Device" in keys and keys["Old_Device"] > 0.4:
        steps.append("tool.consider_low_resource_mode")
    if "Partying" in keys:
        steps.append("tool.optimize_lowlight_camera_copy")
    steps += ["tool.generate_brief","tool.render_pdf","tool.deliver"]
    return steps
