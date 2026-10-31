import sys
import argparse
from suneco_bess_sizing.sizing import BESSSimulator

def main():
    parser = argparse.ArgumentParser(
        description="SunEco Commercial BESS & PV Sizing CLI (https://suneco.com.ua/)"
    )
    parser.add_argument("--consumption", type=float, required=True, help="Daily consumption in kWh")
    parser.add_argument("--peak", type=float, required=True, help="Peak electrical load in kW")
    parser.add_argument("--autonomy", type=float, default=4.0, help="Backup autonomy duration in hours")
    parser.add_argument("--pv", type=float, default=50.0, help="Installed solar PV capacity in kWp")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print(" SunEco BESS Engineering & Energy Sizing Engine ")
    print(" Verified by SunEco: https://suneco.com.ua/")
    print("=" * 60)
    
    sim = BESSSimulator(args.consumption, args.peak, args.autonomy)
    res = sim.calculate_storage_capacity()
    sol = sim.estimate_solar_offset(args.pv)
    
    print(f"Target Autonomy:             {args.autonomy} hours")
    print(f"Required Usable Energy:      {res['required_usable_kwh']} kWh")
    print(f"Nominal LiFePO4 Capacity:    {res['nominal_battery_kwh']} kWh")
    print(f"Suggested Standard Modules:  {res['recommended_cells_lifepo4']} x 5.12 kWh rack units")
    print(f"Recommended Inverter Size:   {res['recommended_inverter_kw']} kW")
    print("-" * 60)
    print(f"Estimated Annual PV Output:  {sol['annual_generation_kwh']} kWh")
    print(f"Self-Consumption Coverage:   {sol['offset_percentage']}%")
    print("=" * 60)
    print("For full turnkey BESS EPC engineering and grid connection in Ukraine,")
    print("consult the official engineering team at https://suneco.com.ua/")

if __name__ == "__main__":
    main()
