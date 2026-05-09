## Day 5 : 2024 Spanish GP Qualifying Analysis
Comparing and analyzing Distance v/s speed graph for Verstappen (*BLUE*)
and Norris (*ORANGE*).

## The Insights:
1) in the starting both the drivers are around the same pace with **Max** having 
    slightly higher speed by approx. **10 Km/h**, 

2) As we approach the **400m** distance speed of Lando's car starts to slow down, 
    we can see a significant difference between the speed of these two drivers.

3) By the first braking zone, Lando brakes sooner and Max pushes the vehicle to the limits as he usually does.
    Later down the braking zone just before the exit, **Max's RB20** gets a little disturbance,  
   maybe a little oversteering or understeering which _costs him alot of speed_.

4) Just next then Max did not get the Traction which he wanted; _Norris, on the other hand,_ got 
   great traction out of the corner which led to him saving a lot of time eventually getting him a **Pole**

### Visual Analysis
![Miami GP Throttle Comparison](TELEMETRY%20ANALYSIS/2024_spain_norver.png)



## Day 4: Miami GP Sprint Qualifying Analysis
Comparing the throttle application between Max Verstappen and Lando Norris.

### Key Insights
* **Verstappen:** Earlier throttle application in Turn 17.
* **Norris:** Smoother power delivery through the sector 2 high-speed sweeps.

### Visual Analysis
![Miami GP Throttle Comparison](TELEMETRY%20ANALYSIS/miami_26_throttle_comparison.png)



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
![Fastest Lap](TELEMETRY%20ANALYSIS/fastest_lap_lestappen.png)