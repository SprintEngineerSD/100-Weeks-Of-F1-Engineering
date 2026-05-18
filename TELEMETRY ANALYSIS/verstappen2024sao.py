import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
fastf1.Cache.enable_cache('f1_cache')
fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')
session = fastf1.get_session(2024, 'São Paulo Grand Prix', 'R')
session.load(telemetry=True, weather=False)
ver_laps = session.laps.pick_drivers('VER')
fig, axes = plt.subplots(3, 1, figsize=(12, 16))
fig.suptitle("Max Verstappen - 2024 Sao Paulo GP Analysis", fontsize=16, fontweight='bold')


ax1 = axes[0]
for stint, stint_laps in ver_laps.groupby('Stint'):
    clean_laps = stint_laps.dropna(subset=['LapTime']).copy()
    if clean_laps.empty:
        continue

    compound = stint_laps['Compound'].iloc[0]
    tyre_colors = {
        'SOFT': 'red',
        'MEDIUM': 'yellow',
        'HARD': 'white',
        'INTERMEDIATE': 'green',
        'WET': 'blue'
    }


    color = tyre_colors.get(str(compound).upper(), 'white')
    clean_laps['LapTime_s'] = clean_laps['LapTime'].dt.total_seconds()

    ax1.plot(clean_laps['LapNumber'], clean_laps['LapTime_s'],
             marker='o', color=color, label=f"Stint {stint} ({compound})")

ax1.set_title("Pace Evolution & Tyre Degradation")
ax1.set_xlabel("Lap Number")
ax1.set_ylabel("Lap Time (Seconds)")
ax1.legend()
ax1.grid(True, alpha=0.3)


ax2 = axes[1]
ax2.plot(ver_laps['LapNumber'], ver_laps['Position'], color='#3671C6', marker='o', linewidth=2)
ax2.invert_yaxis()
ax2.set_yticks(range(1, 21))
ax2.set_title("Track Position Progression")
ax2.set_xlabel("Lap Number")
ax2.set_ylabel("Track Position")
ax2.grid(True, alpha=0.3)

ax3 = axes[2]
telemetry = ver_laps.get_telemetry()
ax3.hist(telemetry['Throttle'], bins=20, color='cyan', edgecolor='black', alpha=0.7)
ax3.set_title("Throttle Application Distribution (Full Race)")
ax3.set_xlabel("Throttle Pedal Input (%)")
ax3.set_ylabel("Telemetry Samples (Frequency)")
ax3.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.savefig('verstappen2024sao.png')
plt.show()
print("--- Max Verstappen Position Tracker ---")
current_pos = ver_laps.iloc[0]['Position']
print(f"Starting Position (Lap 1): P{int(current_pos)}\n")

for _, lap in ver_laps.iterrows():
    lap_num = int(lap['LapNumber'])
    pos = int(lap['Position'])

    if pos < current_pos:
        gained = current_pos - pos
        print(f"Lap {lap_num}: Gained {int(gained)} position(s) -> Now P{pos}")
        current_pos = pos
    elif pos > current_pos:
        lost = pos - current_pos
        print(f"Lap {lap_num}: Dropped {int(lost)} position(s) -> Now P{pos}")
        current_pos = pos