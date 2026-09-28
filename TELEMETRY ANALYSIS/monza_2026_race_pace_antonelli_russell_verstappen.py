import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 1. Setup & Data Loading
# ==========================================
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
fastf1.Cache.enable_cache('f1_cache') # Highly recommended for faster reruns
plt.style.use('dark_background')

# Common visualization colors
fig_color = '#0B0B0C'
plot_color = '#111112'
COLOR_ANT = '#00D2BE' # Mercedes Cyan (Antonelli)
COLOR_RUS = '#7F7F7F' # Grey (Russell - for contrast as teammate)
COLOR_VER = '#0600EF' # Red Bull Blue (Verstappen)

# Load the session (2026 Monza Race)
session = fastf1.get_session(2026, 'Italy', 'R')
session.load(telemetry=True, weather=False)

# Get circuit info for corner mapping
circuit_info = session.get_circuit_info()


# ==============================================================================
# IMAGE 1: RACE PACE & STRATEGY ANALYSIS
# ==============================================================================
print("Generating Image 1: Race Pace Overview...")

# Extract Laps and Filter for 'Quick Laps' (Removes SC, pits, anomalies)
laps_ant = session.laps.pick_drivers('ANT').pick_quicklaps().reset_index(drop=True)
laps_rus = session.laps.pick_drivers('RUS').pick_quicklaps().reset_index(drop=True)
laps_ver = session.laps.pick_drivers('VER').pick_quicklaps().reset_index(drop=True)

# Convert LapTime timedelta to seconds
laps_ant['LapTime_s'] = laps_ant['LapTime'].dt.total_seconds()
laps_rus['LapTime_s'] = laps_rus['LapTime'].dt.total_seconds()
laps_ver['LapTime_s'] = laps_ver['LapTime'].dt.total_seconds()

fig1, ax1 = plt.subplots(figsize=(16, 9), facecolor=fig_color)
ax1.set_facecolor(plot_color)

# 1a. Scatter raw individual lap times (lower alpha for trend visibility)
ax1.scatter(laps_ant['LapNumber'], laps_ant['LapTime_s'], color=COLOR_ANT, alpha=0.35, s=25)
ax1.scatter(laps_rus['LapNumber'], laps_rus['LapTime_s'], color=COLOR_RUS, alpha=0.35, s=25)
ax1.scatter(laps_ver['LapNumber'], laps_ver['LapTime_s'], color=COLOR_VER, alpha=0.35, s=25)

# 1b. Apply Polynomial Regression (Smoothing) for trend lines
# Degree 3 is generally good for tyre degradation modelling
def plot_trend(x, y, ax, color, label, linestyle='-'):
    x_clean = x.dropna()
    y_clean = y.dropna()
    if not x_clean.empty:
        poly_fit = np.poly1d(np.polyfit(x_clean, y_clean, 3))
        ax.plot(x_clean, poly_fit(x_clean), color=color, linewidth=3.5, label=label, linestyle=linestyle)

plot_trend(laps_ant['LapNumber'], laps_ant['LapTime_s'], ax1, COLOR_ANT, 'Antonelli (Mercedes)')
plot_trend(laps_rus['LapNumber'], laps_rus['LapTime_s'], ax1, COLOR_RUS, 'Russell (Mercedes)', '--')
plot_trend(laps_ver['LapNumber'], laps_ver['LapTime_s'], ax1, COLOR_VER, 'Verstappen (Red Bull)', '-.')

# Formatting Image 1
ax1.set_title("2026 ITALIAN GP: PACE ADVANTAGE MODEL\nAntonelli (P19 to P1) Strategy vs Leaders", fontsize=18, fontweight='bold', y=1.02)
ax1.set_xlabel("Lap Number", fontsize=12)
ax1.set_ylabel("Lap Time (Seconds)", fontsize=12)
ax1.set_ylim(82.8, 87.2) # Focused zoom on actual race pace
ax1.grid(True, linestyle=':', alpha=0.2)
ax1.tick_params(colors='white')
ax1.legend(loc='upper right', framealpha=0.3, fontsize=11)

plt.tight_layout()
plt.savefig('monza_2026_image1_race_pace.png', facecolor=fig_color, dpi=150)
plt.close(fig1) # Free memory


# ==============================================================================
# IMAGE 2: THE WINNING OVERTAKE - LAP 50 (Telemetry Stack)
# ==============================================================================
print("Generating Image 2: Winning Overtake Dynamics...")

# Select the specific lap for both drivers (Lap 50)
ant_lap_50 = session.laps.pick_driver('ANT').pick_lap(50)
rus_lap_50 = session.laps.pick_driver('RUS').pick_lap(50)

# Get telemetry and add distance (critical for interpolation)
ant_tel = ant_lap_50.get_telemetry().add_distance()
rus_tel = rus_lap_50.get_telemetry().add_distance()

# Calculate Distance-Based Time Delta using FastF1 utility
# (Using Russell as reference. Positive value = Antonelli is faster)
delta_time, ref_tel, target_tel = fastf1.utils.delta_time(rus_lap_50, ant_lap_50)

# Create 4-panel vertical stack (sharex is essential)
fig2, axes2 = plt.subplots(4, 1, figsize=(14, 20), sharex=True, facecolor=fig_color, gridspec_kw={'height_ratios': [2, 1, 1, 1]})
fig2.suptitle(f"2026 ITALIAN GP | WINNING OVERTAKE DYNAMICS: LAP 50\n"
              f"Antonelli (Fresher Mediums) vs Russell (Older Hards)", fontsize=18, fontweight='bold', y=0.97)

# Helper function to overlay corners on a subplot
def add_corners(ax, text_y, show_labels=False):
    for _, corner in circuit_info.corners.iterrows():
        txt = f"{corner['Number']}{corner['Letter']}"
        ax.axvline(x=corner['Distance'], color='white', linestyle=':', alpha=0.15)
        if show_labels:
            ax.text(corner['Distance'], text_y, txt, color='white', alpha=0.5, fontsize=10,
                    va='center', ha='center', bbox=dict(facecolor='black', alpha=0.3, boxstyle='round'))

# --- 2a. Graph 1: Speed Profile (km/h) ---
ax_speed = axes2[0]
ax_speed.set_facecolor(plot_color)
ax_speed.plot(ant_tel['Distance'], ant_tel['Speed'], color=COLOR_ANT, label='Antonelli', linewidth=2.5)
ax_speed.plot(rus_tel['Distance'], rus_tel['Speed'], color=COLOR_RUS, label='Russell', linestyle='--', linewidth=2.5)
ax_speed.set_ylabel("Speed (km/h)", fontsize=12)
ax_speed.legend(loc='lower left')
ax_speed.set_title("Vehicle Velocity over Lap", fontweight='bold')
# Place corner labels near top speed
add_corners(ax_speed, text_y=335, show_labels=True)

# --- 2b. Graph 2: Pace Difference (Time Delta) ---
ax_delta = axes2[1]
ax_delta.set_facecolor(plot_color)
ax_delta.plot(ref_tel['Distance'], delta_time, color='white', linewidth=2)
ax_delta.axhline(0, color='grey', linestyle='--', alpha=0.5)
ax_delta.set_ylabel("Delta (s)", fontsize=12)
ax_delta.set_title("Time Delta Progression (Positive = Antonelli Gaining)", fontweight='bold')
add_corners(ax_delta, 0) # Lines only

# --- 2c. Graph 3: Throttle Application (%) ---
ax_throttle = axes2[2]
ax_throttle.set_facecolor(plot_color)
ax_throttle.plot(ant_tel['Distance'], ant_tel['Throttle'], color=COLOR_ANT, linewidth=2)
ax_throttle.plot(rus_tel['Distance'], rus_tel['Throttle'], color=COLOR_RUS, linestyle='--', linewidth=2)
ax_throttle.set_ylabel("Throttle %", fontsize=12)
ax_throttle.set_title("Driver Throttle Inputs (Traction Check)", fontweight='bold')
add_corners(ax_throttle, 0) # Lines only

# --- 2d. Graph 4: Brake Application (On/Off) ---
# (Using simplified Brake check for readability across distance)
ax_brake = axes2[3]
ax_brake.set_facecolor(plot_color)
# Convert Brake column (sometimes holds pressure, sometimes T/F) to simplified 0/1 plot
ant_brake_plot = np.where(ant_tel['Brake'] > 0, 1, 0)
rus_brake_plot = np.where(rus_tel['Brake'] > 0, 0.96, 0) # Offset slightly for visibility

ax_brake.plot(ant_tel['Distance'], ant_brake_plot, color=COLOR_ANT, linewidth=2)
ax_brake.plot(rus_tel['Distance'], rus_brake_plot, color=COLOR_RUS, linestyle='--', linewidth=2)
ax_brake.set_ylabel("Brake (Active)", fontsize=12)
ax_brake.set_xlabel("Track Distance (Meters)", fontsize=12)
ax_brake.set_yticks([0, 1])
ax_brake.set_yticklabels(['Off', 'On'])
ax_brake.set_title("Driver Braking Zones", fontweight='bold')
add_corners(ax_brake, 0) # Lines only

# Formatting Image 2 (common ticks)
ax_brake.set_xticks(np.arange(0, 6000, 500))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('monza_2026_image2_overtake_dynamics.png', facecolor=fig_color, dpi=150)
plt.close(fig2)
