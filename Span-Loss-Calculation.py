def calculate_span_loss(distance_km, attenuation_db_per_km=0.25):
    """
    Calculate span loss for a given fiber distance and attenuation.
    """
    return round(distance_km * attenuation_db_per_km, 2)


# 📉 2. OSNR Degradation Simulation
def calculate_osnr(initial_osnr_db, num_spans, degradation_per_span_db=1.0):
    """
    Simulate OSNR degradation over multiple spans.
    """
    degraded_osnr = initial_osnr_db - (num_spans * degradation_per_span_db)
    return round(degraded_osnr, 2)
