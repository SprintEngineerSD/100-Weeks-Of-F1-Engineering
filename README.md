## Day 6: 2024 Spanish GP Qualifying Analysis
This analysis investigates the technical margins between Lando Norris (Pole) 
and Max Verstappen (P2) during the final qualifying session at the 2024 Spanish Grand Prix.

1) _**Initial Pace & Aerodynamic Efficiency:**_ In the high-speed opening phase, both drivers are within a similar window,
    though Max maintains a slight speed advantage of approximately 10 km/h on the straights. 
    This underscores the low drag efficiency of the RB20's aerodynamic package.

2) **_Braking Zone Entry:_** As we approach the 400m mark, Lando Norris’s deceleration curve begins earlier.
   While Max pushes deeper into the braking zone, a trademark of his aggressive style, 
   the telemetry suggests Norris is prioritizing a more stable platform for the corner apex.

3) **_Mid-Corner Instability:_** Just before the exit of the primary braking zone, the RB20 appears to experience a minor disturbance. 
     This could indicate a snap of oversteering or a front-end "wash" (understeer) that forced Max to modulate his inputs. 
     This loss of stability is the exact moment Max begins to lose the time delta to the McLaren.

4) **_Traction & Exit Strategy:_** Because Norris maintained a cleaner mid-corner line, he achieved superior traction on exit.
  He reached 100% throttle application significantly earlier than Max. This superior exit momentum allowed him to recover 
  the straight line deficit, ultimately clinching Pole Position.

## Visual Analysis
Top Chart: Velocity Trace (km/h) Visualizes the time delta. (As discussed on Day 5).

Middle Chart: Throttle Application Shows driver aggression and traction limits.

Bottom Chart: Brake Engagement Highlights the braking points and trail-braking phases.
![SPANISH GP 2024 QUALIFYING Throttle,Brake ANALYSIS](TELEMETRY%20ANALYSIS/Spain_2024_Full_Telemetry.png)


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
![SPANISH GP 2024 QUALIFYING ANALYSIS](TELEMETRY%20ANALYSIS/2024_spain_norver.png)



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