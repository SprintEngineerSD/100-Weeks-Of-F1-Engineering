## Day 10: 2026 Spanish GP Analysis (Hamilton vs Russell)
Comparative Analysis: Lewis Hamilton (Scuderia Ferrari) vs. George Russell (Mercedes-AMG)

Date of Race: June 14, 2026

_**Part 1: Strategic Execution & The "Cheap" Pitstop Physics**_

The 2026 Spanish Grand Prix at the Circuit de Barcelona-Catalunya was a strategic masterclass defined by extreme thermal management. High ambient temperatures (34°C) and track temperatures exceeding 51°C accelerated thermal degradation on the Pirelli C3 (Medium) and C4 (Soft) compounds, turning the race into a complex three-stop tactical battle.
The Virtual Safety Car (VSC) "Cheap" Pitstop
The defining moment of Lewis Hamilton's victory on Lap 48 was his pitstop under the Virtual Safety Car (triggered by Fernando Alonso's battery failure). To understand how this single decision secured the win, we must calculate the exact time-loss differentials.

Under normal racing conditions, driving through the Barcelona pit lane (from pit entry line to pit exit line at 80 km/h) plus the stationary tyre service time (~2.5s) takes approximately 22.4 seconds longer than staying on track at full racing speed (~290 km/h average on the main straight).
Under the VSC, cars on track must strictly adhere to a reduced speed delta (roughly 35% slower, averaging around 175-180 km/h on the straight).
However, the pitlane speed limit remains a constant 80 km/h under both Green and VSC conditions.
Because the cars on track are traveling much slower, the relative velocity differential between a pitting car and a track car is significantly reduced.
The actual time loss under VSC drops to just 11.8 seconds.

The Strategic Split:
Hamilton (Ferrari): Pitted on Lap 48 precisely as the VSC was deployed. He incurred only 11.8s of net loss, emerging on fresh, high-grip Soft tyres.
Russell (Mercedes): Had passed the pit entry just before the VSC was called and was forced to complete a slow lap under the delta. Because he missed the immediate window, he was forced to stay out to protect track position on highly degraded Hard tyres.
The Undercut Effect: When the track went green on Lap 51, Hamilton's tyre-grip advantage combined with the 10.6-second "free" pit time saving allowed him to easily close the gap and execute an effortless DRS overtake into Turn 1.

_**Part 2: Vehicle Dynamics & Driver Inputs (Lap 44 vs. Lap 66)**_
To understand how Hamilton extracted a 1:20.122 on Lap 44 compared to Russell's 1:20.640 on Lap 66 (a gap of 0.518 seconds), we analyze their physical telemetry inputs: Engine RPM, Throttle Modulation, Braking, and Speed over Distance.
Hamilton utilized fresh Medium tyres to carry more speed out of Turn 16, maximizing ERS deployment.
Hamilton's superior front-end bite allowed late-apex rotation without mid-corner sliding.
Russell's worn tyres caused rear-axle instability, forcing him to fight oversteer on exit.
Hamilton kept the car's platform flat, maximizing the underbody ground-effect venturi tunnels.

_**Part 3: Telemetry Graph Interpretation**_
Sector 1 (0m to 1200m): High-Speed Dominance
The Sweep through Turn 3: Turn 3 is a long, high-lateral-G right-hander. At 240+ km/h, the car relies heavily on aerodynamic downforce.
Telemetry Analysis: Hamilton's speed trace shows he maintains a throttle application of 94% through Turn 3, whereas Russell has to drop to 86% to prevent understeer. This indicates Hamilton's Ferrari possessed superior aerodynamic platform control.
Delta Impact: Hamilton gains 0.18 seconds in this single corner.

Sector 2 (1200m to 3000m): Mechanical Grip & Traction Zones
Turn 5 (Downhill Hairpin): Turn 5 is notoriously difficult because the track drops away, unloading the front suspension and inducing locking.
Driver Input Analysis:
Russell stamps hard on the brakes (binary 100% application) and suffers a brief front-left lockup, forcing him to delay his throttle application. His engine RPM dips significantly as the car bogs down mid-corner.
Hamilton employs exquisite trail braking, gradually tapering his brake pressure from 100% down to 10% as he steers toward the apex. By keeping the front tyres loaded progressively, he avoids lockups, rotates the car rapidly, and gets back to 100% throttle  meters earlier than Russell.
Delta Impact: The delta line climbs steeply in Hamilton's favor, adding another 0.22 seconds to his advantage.

Sector 3 (3000m to 4657m): Thermal Management & Low-Speed Agility
The Final Chicane Elimination (Turn 14 ): With the removal of the chicane in recent years, the final sector is a sweeping, high-speed blast onto the main straight. This places extreme load on the left-rear tyre.
Driver Input Analysis: Russell's telemetry on Lap 66 shows a jagged throttle trace. His rear tyres are thermally exhausted, causing the rear end to step out (wheelspin). He is forced to lift off the throttle twice to catch the slide. Hamilton's trace is a clean, undisturbed, single-ascent curve to 100% throttle.
Engine RPM Analysis: Hamilton short-shifts  at a lower RPM (11,800 RPM instead of the peak 12,200 RPM). This intentional short-shifting keeps engine torque from overwhelming the rear tyres, preventing wheelspin and keeping his trajectory perfectly linear onto the main straight.
Delta Impact: Hamilton seals his advantage, gaining a final 0.118 seconds on the run to the line to finalize his 0.518-second gap.

Conclusion: How the Race Was Won
Lewis Hamilton's victory was a perfect synergy of aerospace-grade vehicle dynamics and elite race-engineering strategy:
The Strategy: Ferrari capitalized on the thermodynamic reality of the VSC. By saving 10.6 seconds relative to the pack during his tyre change, Hamilton acquired a massive tyre-offset advantage that made passing Russell inevitable.
The Dynamics: On track, Hamilton managed his mechanical and aerodynamic grip profiles with immense precision. By utilizing trail braking to prevent front-end lockups in Sector 2, and short-shifting to prevent rear thermal degradation in Sector 3, he maintained a flat, aerodynamically stable platform that Russell's struggling Mercedes simply could not match.

![SPANISH GP 2026 RACE Analysis Plot 1](TELEMETRY%20ANALYSIS/Barcelona1.png)
![SPANISH GP 2026 RACE Analysis Plot 2](TELEMETRY%20ANALYSIS/Barcelona2.png)


## Day 9: 2026 Monaco GP Qualifying Analysis (Antonelli vs Verstappen)
This analysis breaks down the final Q3 runs at the 2026 Monaco Grand Prix, where Mercedes' Kimi Antonelli delivered a "magic lap" (1:12.051) to narrowly edge out Red Bull's Max Verstappen (1:12.094) by a mere 0.043 seconds for Pole Position.

1) _**Time Delta & Sector Exchanges:**_ The time delta trace (Top Panel) illustrates a classic street-circuit tug-of-war. Verstappen routinely gained fractions of a second under heavy braking and corner entry, sending the delta line into the negative. However, Antonelli's Mercedes possessed superior mechanical grip, allowing him to consistently claw the time back on corner exits, steadily driving the delta positive through Sector 2 and the Swimming Pool complex. 

2) _**Nouvelle Chicane Braking Commitment:**_ The braking trace (Bottom Panel) reveals the contrasting styles of the two drivers at the heaviest braking zone on the circuit (out of the tunnel into the Nouvelle Chicane). Verstappen brakes marginally later and deeper into the zone, maximizing his entry speed. Antonelli, conversely, initiates his braking phase slightly earlier to prioritize a stable platform, ensuring he avoids locking up on the downhill, bumpy approach.

3) _**Traction & Throttle Pick-Up:**_ Monaco is defined by low-speed traction, and the throttle telemetry (Panel 3) highlights why Antonelli secured pole. Out of Portier (before the tunnel) and La Rascasse, Antonelli's throttle trace spikes to 100% significantly earlier than Verstappen's. The Red Bull struggles slightly with rear-end rotation, forcing Max to modulate the pedal briefly before fully deploying the power. This early throttle application by Antonelli translates to higher terminal speeds down the subsequent short straights.

4) _**Corner Minimums ($V_{min}$):**_ Looking at the Velocity trace through the hairpin and the tight confines of Sector 3, Antonelli rolls more minimum speed through the apexes. While Verstappen relies on aggressive rotation and point-and-shoot dynamics, Antonelli's smoother steering inputs and the Mercedes' compliant front-end geometry allow him to carry more momentum through the center of the corners.

## Visual Analysis
Top Chart: Time Delta Maps exactly where the 0.043s advantage was built. Watch the line rise on corner exits (Mercedes advantage) and fall on corner entries (Red Bull advantage).

Middle-Top Chart: Velocity Trace (km/h) Shows Antonelli's superior apex speeds ($V_{min}$) and exit momentum.

Middle-Bottom Chart: Throttle Application (%) Spotlights the Mercedes' immense mechanical traction out of low-speed corners.

Bottom Chart: Brake Application Highlights Verstappen's aggressive, late-braking philosophy versus Antonelli's stabilizing approach.

![MONACO GP 2026 Qualifying Analysis](TELEMETRY%20ANALYSIS/verkimiMonaco26.png)


## Day 8: 2026 Canadian GP Setup Instability Analysis (FP1 vs Sprint)
This analysis investigates the severe driveability degradation of Max Verstappen's car between Practice 1 and the Sprint session at the 2026 Canadian Grand Prix. With direct ride-height and suspension telemetry encrypted by the teams, this project utilizes raw speed, throttle, and brake traces to mathematically infer severe bouncing and a loss of mechanical compliance over the Circuit Gilles Villeneuve.

1) _**Straight-Line Bottoming & Aerodynamic Stalling:**_ On the high-speed run down the Casino Straight, the Sprint speed trace flattens prematurely compared to the FP1 baseline. This velocity plateau indicates that the lowered ride height caused the floor plank to physically drag on the tarmac. This excessive friction, combined with the aerodynamic stall from porpoising, severely compromised terminal top speed.

2) _**Throttle Micro-Lifts (The Confidence Deficit):**_ The most glaring evidence of an undrivable setup appears in the high-speed throttle telemetry. During FP1, Verstappen maintained 100% throttle cleanly until the braking phase. In the Sprint, the telemetry reveals distinct "feathering" and early lifts (dropping to 80-90% throttle) well before the Turn 13 braking zone. This proves the violent bouncing forced him to physically lift off the pedal to maintain control and keep the rear axle settled.

3) _**Braking Instability & Kerb Rejection:**_ Montreal requires a compliant suspension to attack the heavy kerbs. The brake trace during the Sprint reveals highly erratic, staggered braking inputs—a stark contrast to the clean, solid block of braking seen in FP1. Because the stiffer suspension setup caused the tires to literally skip across the bumpy surface, the contact patch was inconsistent, forcing Max to modulate the brakes heavily to avoid front lock-ups.

4) _**Mid-Corner V-Min & Traction Loss:**_ Due to the stiffened mechanical platform, the car failed to absorb the track's natural undulations. This resulted in a lower minimum cornering speed ($V_{min}$) through the Turn 8/9 chicane. Furthermore, the throttle trace shows a delayed return to 100% on corner exit, as the lack of mechanical grip meant the rear tires could not deploy torque efficiently without snapping into oversteer.

## Visual Analysis
Top Chart: Velocity Trace (km/h) Highlights the top speed deficit on the Casino Straight and lower mid-corner minimums due to excessive bottoming out.

Middle Chart: Throttle Application Exposes the lack of driver confidence, explicitly showing the early throttle lifts and delayed exit traction caused by the bouncing.

Bottom Chart: Brake Engagement Visualizes the erratic pedal modulation required to survive the braking zones with a stiff, non-compliant suspension setup over the Montreal kerbs.

![CANADIAN GP 2026 Setup Instability Analysis](TELEMETRY%20ANALYSIS/VerstappenCNGP26.png)


## Day 7: 2024 Sao Paulo GP Race Analysis
This analysis investigates the strategic execution and technical wet-weather mastery of Max Verstappen during his historic climb from P17 to P1 at the 2024 Sao Paulo Grand Prix.

1) _**The Opening Lap Blitz:**_ Starting out of position due to a grid penalty and a red-flagged qualifying, Max bypassed six cars on Lap 1 alone. Positional data shows him utilizing unconventional, karting-style outside lines to find grip where rubber hadn't been laid down, instantly propelling him into the midfield.

2) _**Patience & Strategic Masterstroke:**_ After stalling at P6 due to the severe spray and dirty air of the cars ahead, Red Bull made the decisive call to keep Max on track as rain intensified and rivals pitted. A subsequent Red Flag allowed for a "free" tyre change, perfectly converting his on-track patience into a front-row restart position.

3) _**Wet-Weather Throttle Modulation:**_ Unlike dry conditions where throttle application is highly binary (0% or 100%), the telemetry reveals a massive spread of micro-modulations in the 40% to 80% range. This right-foot precision—feathering the pedal rather than relying on engine mapping—prevented the rear wheels from breaking traction and preserved the delicate intermediate tyre tread.

4) _**Pace Evolution & Tyre Preservation:**_ Rather than experiencing standard thermal degradation (slower lap times), Max's lap times consistently dropped as the track dried. By not overworking the intermediate compound early in the final stint, he retained enough grip to set a string of fastest laps, pulling nearly a second per lap on the rest of the field to secure the win.

## Visual Analysis
Top Chart: Pace Evolution & Tyre Degradation Visualizes the drying track effect and the severe lap time spikes caused by Safety Car and VSC periods.

Middle Chart: Track Position Progression Shows the immediate Lap 1 climb, the mid-race plateau at P6, and the strategic Red Flag jump to the front of the pack.

Bottom Chart: Throttle Application Distribution Highlights the "feathering" technique, proving his mechanical sympathy and traction control in the wet.

![SAO PAULO GP 2024 Race Analysis](TELEMETRY%20ANALYSIS/verstappen2024sao.png)

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