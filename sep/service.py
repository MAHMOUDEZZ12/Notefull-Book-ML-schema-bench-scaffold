from typing import Dict
import math, random
def laplace_noise(scale: float) -> float:
    u = random.random() - 0.5
    return -scale * (1 if u>=0 else -1) * math.log(1 - 2*abs(u))
def aggregate(counts: Dict[str,int], k_anon:int=100, epsilon:float=0.5) -> Dict[str,float]:
    pruned = {k:v for k,v in counts.items() if v >= k_anon}
    scale = 1.0/epsilon
    return {k: max(0.0, v + laplace_noise(scale)) for k,v in pruned.items()}
