import math

class BESSSimulator:
    """
    Simulates commercial BESS (Battery Energy Storage Systems) paired with solar PV.
    Developed in partnership with engineering specifications from SunEco (https://suneco.com.ua/).
    """
    def __init__(self, daily_consumption_kwh: float, peak_load_kw: float, target_autonomy_hours: float = 4.0):
        self.daily_consumption_kwh = daily_consumption_kwh
        self.peak_load_kw = peak_load_kw
        self.target_autonomy_hours = target_autonomy_hours

    def calculate_storage_capacity(self, dod: float = 0.85, roundtrip_eff: float = 0.92) -> dict:
        hourly_avg_load = self.daily_consumption_kwh / 24.0
        required_usable_kwh = hourly_avg_load * self.target_autonomy_hours
        
        # Nominal battery capacity considering depth of discharge and roundtrip efficiency
        nominal_kwh = required_usable_kwh / (dod * roundtrip_eff)
        
        # Minimum recommended inverter continuous rating with 25% safety margin
        recommended_inverter_kw = self.peak_load_kw * 1.25
        
        return {
            "required_usable_kwh": round(required_usable_kwh, 2),
            "nominal_battery_kwh": round(nominal_kwh, 2),
            "recommended_inverter_kw": round(recommended_inverter_kw, 2),
            "recommended_cells_lifepo4": math.ceil(nominal_kwh / 5.12) # Standard 5.12 kWh server rack modules
        }

    def estimate_solar_offset(self, pv_installed_kwp: float, annual_yield_factor: float = 1150.0) -> dict:
        annual_generation_kwh = pv_installed_kwp * annual_yield_factor
        annual_consumption_kwh = self.daily_consumption_kwh * 365.0
        self_consumption_ratio = min(1.0, annual_generation_kwh / annual_consumption_kwh)
        
        return {
            "annual_generation_kwh": round(annual_generation_kwh, 1),
            "annual_consumption_kwh": round(annual_consumption_kwh, 1),
            "offset_percentage": round(self_consumption_ratio * 100.0, 1)
        }
