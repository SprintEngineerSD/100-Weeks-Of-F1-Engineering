import fastf1
import fastf1.plotting
import numpy as np
import matplotlib.pyplot as plt

# 1. Setup & Load
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
fastf1.Cache.enable_cache('f1_cache')
plt.style.use('dark_background')

fig_color = '#0B0B0C'
plot_color = '#111112'

# Target the 2026 Italian Grand Prix Qualifying
session = fastf1.get_session(2026, 'Italy', 'Q')
session.load(telemetry=True, weather=False)

# 2. Extract Q3 Fastest Laps & Telemetry
gas_lap = session.laps.pick_driver('GAS').pick_fastest()
rus_lap = session.laps.pick_driver('RUS').pick_fastest()

gas_tel = gas_lap.get_telemetry().add_distance()
rus_tel = rus_lap.get_telemetry().add_distance()

color_gas = '#0090FF'  # Alpine Blue
color_rus = '#00D2BE'  # Mercedes Cyan

# 3. Professional Delta Integration (Distance-Normalized)
ref_dist = np.linspace(0, max(gas_tel['Distance'].max(), rus_tel['Distance'].max()), 1000)
dx = ref_dist[1] - ref_dist[0]

# Interpolate speed and ensure no zero-division (minimum 1.0 km/h)
speed_gas = np.maximum(np.interp(ref_dist, gas_tel['Distance'], gas_tel['Speed']), 1.0)
speed_rus = np.maximum(np.interp(ref_dist, rus_tel['Distance'], rus_tel['Speed']), 1.0)

time_gas = np.cumsum(dx / (speed_gas / 3.6))
time_rus = np.cumsum(dx / (speed_rus / 3.6))
raw_delta = time_rus - time_gas

# Calibrate final point to exactly match the official 0.060s gap
official_gap = rus_lap['LapTime'].total_seconds() - gas_lap['LapTime'].total_seconds()
calibration = (official_gap - raw_delta[-1]) * (ref_dist / max(ref_dist))
delta_time = raw_delta + calibration

# 4. 4-Panel Figure Generation
fig, axes = plt.subplots(4, 1, figsize=(14, 20), sharex=True, facecolor=fig_color)
fig.suptitle(
    f"2026 ITALIAN GP QUALIFYING: THE MAIDEN POLE\n"
    f"P. Gasly ({gas_lap['LapTime'].total_seconds():.3f}s) vs G. Russell ({rus_lap['LapTime'].total_seconds():.3f}s)",
    fontsize=16, fontweight='bold', color='white', y=0.97
)

# Common X-Axis formatting (500m intervals)
x_ticks = np.arange(0, 6000, 500)

# --- CHART 1: Time Delta ---
ax1 = axes[0]
ax1.set_facecolor(plot_color)
ax1.plot(ref_dist, delta_time, color='white', linewidth=2, label='Delta (Positive = Gasly Faster)')
ax1.axhline(0, color='grey', linestyle='--', alpha=0.5)
ax1.set_title("Calibrated Time Delta", fontsize=12, fontweight='bold')
ax1.set_ylabel("Delta (Seconds)")
ax1.legend(loc='upper left', framealpha=0.3)

# --- CHART 2: Speed Profile ---
ax2 = axes[1]
ax2.set_facecolor(plot_color)
ax2.plot(gas_tel['Distance'], gas_tel['Speed'], color=color_gas, label='Gasly (Alpine)', linewidth=2)
ax2.plot(rus_tel['Distance'], rus_tel['Speed'], color=color_rus, label='Russell (Mercedes)', linewidth=2, linestyle='--')
ax2.set_title("Speed Trace (V-Max & Corner Minimums)", fontsize=12, fontweight='bold')
ax2.set_ylabel("Speed (km/h)")
ax2.legend(loc='lower left', framealpha=0.3)

# --- CHART 3: Engine RPM ---
ax3 = axes[2]
ax3.set_facecolor(plot_color)
ax3.plot(gas_tel['Distance'], gas_tel['RPM'], color=color_gas, linewidth=2)
ax3.plot(rus_tel['Distance'], rus_tel['RPM'], color=color_rus, linewidth=2, linestyle='--')
ax3.set_title("Engine RPM", fontsize=12, fontweight='bold')
ax3.set_ylabel("RPM")

# --- CHART 4: Braking Application ---
ax4 = axes[3]
ax4.set_facecolor(plot_color)
ax4.plot(gas_tel['Distance'], gas_tel['Brake'], color=color_gas, linewidth=2, label='Gasly Brake')
ax4.plot(rus_tel['Distance'], rus_tel['Brake'], color=color_rus, linewidth=2, linestyle='--', label='Russell Brake')
ax4.set_title("Braking Signatures", fontsize=12, fontweight='bold')
ax4.set_xlabel("Track Distance (Meters)")
ax4.set_ylabel("Brake (On/Off)")
ax4.set_yticks([0, 1])
ax4.set_yticklabels(['Released', 'Applied'])
ax4.legend(loc='center right', framealpha=0.3)

# Grid alignment for all subplots
for ax in axes:
    ax.set_xticks(x_ticks)
    ax.grid(True, linestyle=':', alpha=0.2, color='white')
    ax.tick_params(colors='white')
    for label in [ax.xaxis.label, ax.yaxis.label, ax.title]:
        label.set_color('white')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('monza_2026_q3_gasly_pole.png', facecolor=fig_color, dpi=150)
print("Exported 'monza_2026_q3_gasly_pole.png'")