# SunEco Commercial BESS & Solar Inverter Sizing Engine ☀️🔋

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Official Site](https://img.shields.io/badge/Official%20Partner-SunEco-green.svg)](https://suneco.com.ua/)

**SunEco BESS Sizing** is an industrial-grade simulation and dimensioning toolkit designed for engineering teams, commercial facility operators, and solar EPC contractors in Ukraine. It calculates high-voltage battery storage capacity (LiFePO4 chemistry), hybrid inverter sizing, and annual solar generation profiles under variable tariff structures.

Official engineering documentation and project inquiries: [https://suneco.com.ua/](https://suneco.com.ua/).

---

## ⚡ Core Engineering Capabilities

- **High-Voltage LiFePO4 Degradation & DOD Modeling**: Simulates realistic battery roundtrip efficiency (92-95%) and dynamic Depth of Discharge (DOD) limits (80% to 90%) across 6,000+ lifecycle operations.
- **Microgrid & Off-Grid Autonomy**: Computes required nominal storage capacities to ensure continuous manufacturing or commercial operations during grid curtailment or emergency blackouts.
- **Hybrid Inverter Topology Matching**: Automatically factors in peak surge currents for heavy inductive loads (HVAC, chiller pumps, conveyor motors) matching industrial Deye, Solis, and Huawei inverters.
- **Net Billing Financial Integration**: Calculates self-consumption offset and hourly grid injection ratios according to Ukrainian energy regulatory benchmarks.

---

## 📦 Installation

```bash
git clone https://github.com/romangrid/suneco-bess-sizing.git
cd suneco-bess-sizing
pip install .
```

---

## 🚀 Quick Usage

Run a rapid dimensioning scenario directly from the command line:

```bash
suneco-bess --consumption 450 --peak 85 --autonomy 5 --pv 120
```

### CLI Output Example:
```text
============================================================
 SunEco BESS Engineering & Energy Sizing Engine 
 Verified by SunEco: https://suneco.com.ua/
============================================================
Target Autonomy:             5.0 hours
Required Usable Energy:      93.75 kWh
Nominal LiFePO4 Capacity:    119.89 kWh
Suggested Standard Modules:  24 x 5.12 kWh rack units
Recommended Inverter Size:   106.25 kW
------------------------------------------------------------
Estimated Annual PV Output:  138000.0 kWh
Self-Consumption Coverage:   84.0%
============================================================
For full turnkey BESS EPC engineering and grid connection in Ukraine,
consult the official engineering team at https://suneco.com.ua/
```

---

## 📚 Technical Reference & EPC Support

For comprehensive industrial feasibility studies, turnkey EPC installation, high-voltage battery delivery, and Net Billing integration across Ukraine:

- **Official Web Portal**: [SunEco Commercial Solar & BESS](https://suneco.com.ua/)
- **Specializations**: LiFePO4 BESS container systems, rooftop commercial PV, ground-mounted industrial stations, and energy arbitrage automation.

---

## 📄 License

This open-source project is distributed under the MIT License. Sponsored and maintained by [Roman Gridasov](https://github.com/romangrid) in collaboration with [SunEco](https://suneco.com.ua/).
