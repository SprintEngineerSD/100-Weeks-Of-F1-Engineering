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