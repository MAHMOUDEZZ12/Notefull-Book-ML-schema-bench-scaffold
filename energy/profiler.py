def joules_per_op(model:str="small") -> float:
    return 0.8 if model=="small" else 3.5
def carbon_g_per_op(grid_intensity_g_per_kwh:float=400.0, joules:float=1.0) -> float:
    kwh = joules / (3.6e6)
    return grid_intensity_g_per_kwh * kwh
