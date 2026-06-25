import fastf1
import fastf1.plotting
import fastf1.utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fastf1.Cache.enable_cache('f1_cache')

plt.style.use('dark_background')
fig_color = '#0B0B0C'
plot_color = '#111112'

COLOR_HAM = '#E10600'
COLOR_RUS = '#00D2BE'

TYRE_COLORS = {
    'SOFT': '#FF3333',
    'MEDIUM': '#FFE600',
    'HARD': '#FFFFFF'
}

session = fastf1.get_session(2026, 7, 'R')
session.load(telemetry=True, weather=False)


ham_laps = session.laps.pick_drivers('HAM')
rus_laps = session.laps.pick_drivers('RUS')
total_laps = int(session.total_laps)


ham_lap_44 = ham_laps.pick_laps(44)
rus_lap_66 = rus_laps.pick_laps(66)
ham_telemetry = ham_lap_44.get_telemetry().add_distance()
rus_telemetry = rus_lap_66.get_telemetry().add_distance()
ref_distance = np.linspace(0, max(rus_telemetry['Distance']), num=1000)

speed_ham = np.interp(ref_distance, ham_telemetry['Distance'], ham_telemetry['Speed'])
speed_rus = np.interp(ref_distance, rus_telemetry['Distance'], rus_telemetry['Speed'])

ds = np.gradient(ref_distance)
dt_ham = (ds * 3.6) / speed_ham
dt_rus = (ds * 3.6) / speed_rus

accurate_delta = np.cumsum(dt_rus - dt_ham)

actual_lap_time_diff = 80.640 - 80.122
calculated_final_diff = accurate_delta[-1]
calibration_offset = (actual_lap_time_diff - calculated_final_diff) * (ref_distance / max(ref_distance))
accurate_delta = accurate_delta + calibration_offset
fig1, axes1 = plt.subplots(4, 1, figsize=(14, 24), facecolor=fig_color)
fig1.suptitle(
    "2026 BARCELONA GP: STRATEGY & LAP TIMING DYNAMICS\n"
    "Hamilton Lap 44 (Ferrari Red) vs Russell Lap 66 (Mercedes Cyan)",
    fontsize=16, fontweight='bold', color='white', y=0.97
)


ax1_1 = axes1[0]
ax1_1.set_facecolor(plot_color)

vsc_start, vsc_end = 48, 51
ax1_1.axvspan(vsc_start, vsc_end, color='#FF5500', alpha=0.25, label='Virtual Safety Car (Alonso DNF)')


for stint, laps in ham_laps.groupby('Stint'):
    comp = laps['Compound'].iloc[0].upper()
    color = TYRE_COLORS.get(comp, '#888888')
    start_l = laps['LapNumber'].min()
    end_l = laps['LapNumber'].max()
    ax1_1.barh('L. Hamilton\n(Ferrari)', end_l - start_l + 1, left=start_l, color=color, edgecolor='black', height=0.45)


for stint, laps in rus_laps.groupby('Stint'):
    comp = laps['Compound'].iloc[0].upper()
    color = TYRE_COLORS.get(comp, '#888888')
    start_l = laps['LapNumber'].min()
    end_l = laps['LapNumber'].max()
    ax1_1.barh('G. Russell\n(Mercedes)', end_l - start_l + 1, left=start_l, color=color, edgecolor='black', height=0.45)

ax1_1.set_title("Race Stint Strategy & Tyre Timeline", fontsize=12, fontweight='bold', color='white')
ax1_1.set_xlabel("Lap Number", color='white')
ax1_1.set_xlim(1, total_laps)
ax1_1.set_xticks(range(1, total_laps + 1, 5))
ax1_1.tick_params(colors='white')
ax1_1.grid(True, linestyle=':', alpha=0.1, color='white')

legend_patches = [
    mpatches.Patch(color=TYRE_COLORS['SOFT'], label='Soft (Red)'),
    mpatches.Patch(color=TYRE_COLORS['MEDIUM'], label='Medium (Yellow)'),
    mpatches.Patch(color=TYRE_COLORS['HARD'], label='Hard (White)'),
    mpatches.Patch(color='#FF5500', alpha=0.3, label='Virtual Safety Car')
]
ax1_1.legend(handles=legend_patches, loc='upper right', framealpha=0.2)


ax1_2 = axes1[1]
ax1_2.set_facecolor(plot_color)


ax1_2.plot(ham_laps['LapNumber'], ham_laps['LapTime'].dt.total_seconds(), color=COLOR_HAM, label='Hamilton (Ferrari)', linewidth=2)
ax1_2.plot(rus_laps['LapNumber'], rus_laps['LapTime'].dt.total_seconds(), color=COLOR_RUS, label='Russell (Mercedes)', linewidth=2, linestyle='--')

ax1_2.set_title("Lap Times Progression (Full Race)", fontsize=12, fontweight='bold', color='white')
ax1_2.set_xlabel("Lap Number", color='white')
ax1_2.set_ylabel("Lap Time (Seconds)", color='white')
ax1_2.set_xlim(1, total_laps)
ax1_2.set_xticks(range(1, total_laps + 1, 5))
ax1_2.tick_params(colors='white')
ax1_2.grid(True, linestyle=':', alpha=0.15, color='white')
ax1_2.legend(loc='upper right', framealpha=0.3)

ax1_3 = axes1[2]
ax1_3.set_facecolor(plot_color)

ax1_3.plot(ham_telemetry['Distance'], ham_telemetry['Speed'], color=COLOR_HAM, label='Hamilton (Lap 44)', linewidth=2)
ax1_3.plot(rus_telemetry['Distance'], rus_telemetry['Speed'], color=COLOR_RUS, label='Russell (Lap 66)', linewidth=2, linestyle='--')

ax1_3.set_title("Telemetry Speed Profile Comparison", fontsize=12, fontweight='bold', color='white')
ax1_3.set_xlabel("Track Distance (Meters)", color='white')
ax1_3.set_ylabel("Speed (km/h)", color='white')
ax1_3.tick_params(colors='white')
ax1_3.grid(True, linestyle=':', alpha=0.2, color='white')
ax1_3.legend(loc='lower left', framealpha=0.3)

ax1_4 = axes1[3]
ax1_4.set_facecolor(plot_color)
ax1_4.plot(ref_distance, accurate_delta, color='#FFFFFF', label='Delta Time (Russell ref)', linewidth=2)
ax1_4.axhline(0, color='grey', linestyle='--', alpha=0.5)

ax1_4.set_title("Time Delta Progression (Positive values = Hamilton is faster)", fontsize=12, fontweight='bold', color='white')
ax1_4.set_xlabel("Track Distance (Meters)", color='white')
ax1_4.set_ylabel("Delta (Seconds)", color='white')
ax1_4.tick_params(colors='white')
ax1_4.grid(True, linestyle=':', alpha=0.2, color='white')
ax1_4.legend(loc='upper left', framealpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Barcelona1.png', facecolor=fig_color, dpi=150)
plt.show()


fig2, axes2 = plt.subplots(3, 1, figsize=(14, 18), sharex=True, facecolor=fig_color)
fig2.suptitle(
    "2026 BARCELONA GP: DRIVER PHYSICAL INPUTS ANALYSIS\n"
    "Hamilton Lap 44 (Ferrari Red) vs Russell Lap 66 (Mercedes Cyan)",
    fontsize=16, fontweight='bold', color='white', y=0.96
)


ax2_1 = axes2[0]
ax2_1.set_facecolor(plot_color)

ax2_1.plot(ham_telemetry['Distance'], ham_telemetry['RPM'], color=COLOR_HAM, label='Hamilton RPM', linewidth=2)
ax2_1.plot(rus_telemetry['Distance'], rus_telemetry['RPM'], color=COLOR_RUS, label='Russell RPM', linewidth=2, linestyle='--')

ax2_1.set_title("Engine RPM Profile", fontsize=12, fontweight='bold', color='white')
ax2_1.set_ylabel("RPM", color='white')
ax2_1.tick_params(colors='white')
ax2_1.grid(True, linestyle=':', alpha=0.2, color='white')
ax2_1.legend(loc='lower left', framealpha=0.3)


ax2_2 = axes2[1]
ax2_2.set_facecolor(plot_color)

ax2_2.plot(ham_telemetry['Distance'], ham_telemetry['Throttle'], color=COLOR_HAM, label='Hamilton Throttle', linewidth=2)
ax2_2.plot(rus_telemetry['Distance'], rus_telemetry['Throttle'], color=COLOR_RUS, label='Russell Throttle', linewidth=2, linestyle='--')

ax2_2.set_title("Throttle Application (%)", fontsize=12, fontweight='bold', color='white')
ax2_2.set_ylabel("Throttle %", color='white')
ax2_2.tick_params(colors='white')
ax2_2.grid(True, linestyle=':', alpha=0.2, color='white')
ax2_2.legend(loc='lower left', framealpha=0.3)


ax2_3 = axes2[2]
ax2_3.set_facecolor(plot_color)

ax2_3.plot(ham_telemetry['Distance'], ham_telemetry['Brake'], color=COLOR_HAM, label='Hamilton Brake (On/Off)', linewidth=2)
ax2_3.plot(rus_telemetry['Distance'], rus_telemetry['Brake'], color=COLOR_RUS, label='Russell Brake (On/Off)', linewidth=2, linestyle='--')

ax2_3.set_title("Brake Application", fontsize=12, fontweight='bold', color='white')
ax2_3.set_xlabel("Track Distance (Meters)", color='white')
ax2_3.set_ylabel("Brake (On/Off)", color='white')
ax2_3.set_yticks([0, 1])
ax2_3.set_yticklabels(['Released', 'Applied'])
ax2_3.tick_params(colors='white')
ax2_3.grid(True, linestyle=':', alpha=0.2, color='white')
ax2_3.legend(loc='upper right', framealpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Barcelona2.png', facecolor=fig_color, dpi=150)
plt.show()

