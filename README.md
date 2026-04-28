Day 3 : The Delta Path
**Objective:** Mastering the primary tool of the Race Engineer—The Delta Graph.

**Technical Goal:** Use NumPy interpolation to align two independent telemetry streams on a common distance axis.
**Analysis:** Compared George Russell and Kimi Antonelli at the 2026 Australian GP.

**Engineering Finding:** While the speed traces look nearly identical, 
the **Delta line** reveals that Antonelli gains 0.04s in the high-speed Turn 6/7 complex, but Russell's superior energy management allows him to claw back 0.06s on the following straight.

![Delta Analysis](TELEMETRY%20ANALYSIS/merc_delta_analysis.png)


Day 2: The Fastest Lap

**Tools Used**: FastF1, Matplotlib, Git, and PyCharm.

**Session**: 2024 Saudi Arabian GP (Jeddah) — Qualifying.

**Engineering Insight**: Comparing **Verstappen (Red Bull)** and **Leclerc (Ferrari)** on a high-speed street circuit.

**Braking Profile**: Observed the "sharpness" of the braking curves.
Verstappen's data often shows a more aggressive initial brake pressure, allowing for a shorter braking zone before the apex.

**Top Speed**: Red Bull's aerodynamic efficiency (low drag) is evident in the higher peak speeds achieved on the main straights compared to the Ferrari.
![Fastest Lap](TELEMETRY%20ANALYSIS/fastest_lap_comparison.png)