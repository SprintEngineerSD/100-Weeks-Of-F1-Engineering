import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings

warnings.filterwarnings('ignore')
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
fastf1.Cache.enable_cache('f1_cache')

plt.style.use('dark_background')
fig_color = '#0B0B0C'
plot_color = '#111112'


COLOR_HAM = '#E10600'
COLOR_VER = '#3671C6'

TYRE_COLORS = {
    'SOFT': '#FF3333',
    'MEDIUM': '#FFE600',
    'HARD': '#FFFFFF'
}

session = fastf1.get_session(2026, 'Austria', 'R')
session.load(telemetry=True, weather=False)

ham_laps = session.laps.pick_drivers('HAM')
ver_laps = session.laps.pick_drivers('VER')

# Get circuit info to mark the corners on the track
circuit_info = session.get_circuit_info()
total_laps = int(session.total_laps)

ham_lap_11 = ham_laps.pick_lap(11)
ver_lap_11 = ver_laps.pick_lap(11)

ham_tel_11 = ham_lap_11.get_telemetry().add_distance()
ver_tel_11 = ver_lap_11.get_telemetry().add_distance()


# Helper function to format the axes with 500m intervals and mark turns
def format_axis_with_turns(ax, title, ylabel):
    ax.set_facecolor(plot_color)
    ax.set_title(title, fontsize=12, fontweight='bold', color='white')
    ax.set_xlabel("Track Distance (Meters)", color='white')
    ax.set_ylabel(ylabel, color='white')
    ax.set_xticks(np.arange(0, 5000, 500))
    ax.tick_params(colors='white')
    ax.grid(True, linestyle=':', alpha=0.3, color='white')

    # Mark corners
    if circuit_info is not None:
        trans = ax.get_xaxis_transform()
        for _, corner in circuit_info.corners.iterrows():
            ax.axvline(x=corner['Distance'], color='grey', linestyle=':', alpha=0.4)
            ax.text(corner['Distance'], 0.95, f"T{corner['Number']}", transform=trans,
                    color='grey', fontsize=8, rotation=90, verticalalignment='top')


fig1, axes1 = plt.subplots(4, 1, figsize=(14, 20), facecolor=fig_color)
fig1.suptitle(
    "2026 AUSTRIAN GP - LAP 11: HAMILTON DEFENDS VERSTAPPEN\n"
    ,
    fontsize=16, fontweight='bold', color='white', y=0.96
)

# 1. Tyre Offset Plot (Lap 11)
ax1_1 = axes1[0]
ax1_1.set_facecolor(plot_color)
ham_compound_11 = str(ham_lap_11['Compound']).upper()
ver_compound_11 = str(ver_lap_11['Compound']).upper()
ham_age_11 = int(ham_lap_11['TyreLife'])
ver_age_11 = int(ver_lap_11['TyreLife'])

ax1_1.barh('L. Hamilton\n(Ferrari)', ham_age_11, color=TYRE_COLORS.get(ham_compound_11, 'grey'), edgecolor=COLOR_HAM,
           linewidth=2)
ax1_1.barh('M. Verstappen\n(Red Bull)', ver_age_11, color=TYRE_COLORS.get(ver_compound_11, 'grey'), edgecolor=COLOR_VER,
           linewidth=2)
ax1_1.set_title("Tyre Offset at Lap 11 (Compound & Laps Old)", fontsize=12, fontweight='bold', color='white')
ax1_1.set_xlabel("Tyre Age (Laps)", color='white')
ax1_1.tick_params(colors='white')
ax1_1.grid(True, linestyle=':', alpha=0.2, color='white')
ax1_1.text(ham_age_11 / 2, 0, f"{ham_compound_11} ({ham_age_11} Laps)", color='black', fontweight='bold', ha='center',
           va='center')
ax1_1.text(ver_age_11 / 2, 1, f"{ver_compound_11} ({ver_age_11} Laps)", color='black', fontweight='bold', ha='center',
           va='center')

# 2. Speed / Lap Pace Line Graph (Lap 11)
ax1_2 = axes1[1]
format_axis_with_turns(ax1_2, "Lap 11 Speed Profile (Pace over Distance)", "Speed (km/h)")
ax1_2.plot(ham_tel_11['Distance'], ham_tel_11['Speed'], color=COLOR_HAM, label='Hamilton', linewidth=2)
ax1_2.plot(ver_tel_11['Distance'], ver_tel_11['Speed'], color=COLOR_VER, label='Verstappen', linewidth=2,
           linestyle='--')
ax1_2.legend(loc='upper right', framealpha=0.3)

# 3. Engine RPM Line Graph (Lap 11)
ax1_3 = axes1[2]
format_axis_with_turns(ax1_3, "Engine RPM Profile", "RPM")
ax1_3.plot(ham_tel_11['Distance'], ham_tel_11['RPM'], color=COLOR_HAM, label='Hamilton RPM', linewidth=2)
ax1_3.plot(ver_tel_11['Distance'], ver_tel_11['RPM'], color=COLOR_VER, label='Verstappen RPM', linewidth=2,
           linestyle='--')
ax1_3.legend(loc='upper right', framealpha=0.3)

# 4. Braking Pattern (Lap 11)
ax1_4 = axes1[3]
format_axis_with_turns(ax1_4, "Braking Application (On/Off)", "Brake (1=On, 0=Off)")
ax1_4.plot(ham_tel_11['Distance'], ham_tel_11['Brake'], color=COLOR_HAM, label='Hamilton Brake', linewidth=2)
ax1_4.plot(ver_tel_11['Distance'], ver_tel_11['Brake'], color=COLOR_VER, label='Verstappen Brake', linewidth=2,
           linestyle='--')
ax1_4.set_yticks([0, 1])
ax1_4.set_yticklabels(['Released', 'Applied'])
ax1_4.legend(loc='upper right', framealpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('austrialap11.png', facecolor=fig_color, dpi=150)
plt.show()

ham_lap_22 = ham_laps.pick_lap(22)
ver_lap_22 = ver_laps.pick_lap(22)

ham_tel_22 = ham_lap_22.get_telemetry().add_distance()
ver_tel_22 = ver_lap_22.get_telemetry().add_distance()

fig2, axes2 = plt.subplots(5, 1, figsize=(14, 25), facecolor=fig_color)
fig2.suptitle(
    "2026 AUSTRIAN GP - LAP 22: VERSTAPPEN OVERTAKES HAMILTON\n"
    "Full Strategy Timeline & Telemetry Analysis",
    fontsize=16, fontweight='bold', color='white', y=0.97
)

# 1. Pit Strategy Histogram (Full Race)
ax2_1 = axes2[0]
ax2_1.set_facecolor(plot_color)
for stint, laps in ham_laps.groupby('Stint'):
    comp = str(laps['Compound'].iloc[0]).upper()
    color = TYRE_COLORS.get(comp, '#888888')
    ax2_1.barh('L. Hamilton', laps['LapNumber'].max() - laps['LapNumber'].min() + 1,
               left=laps['LapNumber'].min(), color=color, edgecolor='black', height=0.45)

for stint, laps in ver_laps.groupby('Stint'):
    comp = str(laps['Compound'].iloc[0]).upper()
    color = TYRE_COLORS.get(comp, '#888888')
    ax2_1.barh('M. Verstappen', laps['LapNumber'].max() - laps['LapNumber'].min() + 1,
               left=laps['LapNumber'].min(), color=color, edgecolor='black', height=0.45)

ax2_1.axvline(x=22, color='white', linestyle='--', label='Lap 22 (Overtake Moment)')
ax2_1.set_title("Race Pit Strategy Timeline", fontsize=12, fontweight='bold', color='white')
ax2_1.set_xlabel("Lap Number", color='white')
ax2_1.set_xlim(1, total_laps)
ax2_1.tick_params(colors='white')
ax2_1.grid(True, linestyle=':', alpha=0.1, color='white')
legend_patches_strat = [
    mpatches.Patch(color=TYRE_COLORS['SOFT'], label='Soft'),
    mpatches.Patch(color=TYRE_COLORS['MEDIUM'], label='Medium'),
    mpatches.Patch(color=TYRE_COLORS['HARD'], label='Hard')
]
ax2_1.legend(handles=legend_patches_strat, loc='upper right', framealpha=0.3)

# 2. Tyre Offset Plot (Lap 22)
ax2_2 = axes2[1]
ax2_2.set_facecolor(plot_color)
ham_compound_22 = str(ham_lap_22['Compound']).upper()
ver_compound_22 = str(ver_lap_22['Compound']).upper()
ham_age_22 = int(ham_lap_22['TyreLife'])
ver_age_22 = int(ver_lap_22['TyreLife'])

ax2_2.barh('L. Hamilton', ham_age_22, color=TYRE_COLORS.get(ham_compound_22, 'grey'), edgecolor=COLOR_HAM, linewidth=2)
ax2_2.barh('M. Verstappen', ver_age_22, color=TYRE_COLORS.get(ver_compound_22, 'grey'), edgecolor=COLOR_VER,
           linewidth=2)
ax2_2.set_title("Tyre Offset at Lap 22 (Compound & Laps Old)", fontsize=12, fontweight='bold', color='white')
ax2_2.set_xlabel("Tyre Age (Laps)", color='white')
ax2_2.tick_params(colors='white')
ax2_2.grid(True, linestyle=':', alpha=0.2, color='white')
ax2_2.text(ham_age_22 / 2, 0, f"{ham_compound_22} ({ham_age_22} Laps)", color='black', fontweight='bold', ha='center',
           va='center')
ax2_2.text(ver_age_22 / 2, 1, f"{ver_compound_22} ({ver_age_22} Laps)", color='black', fontweight='bold', ha='center',
           va='center')

# 3. Speed / Lap Pace Line Graph (Lap 22)
ax2_3 = axes2[2]
format_axis_with_turns(ax2_3, "Lap 22 Speed Profile (Pace over Distance)", "Speed (km/h)")
ax2_3.plot(ham_tel_22['Distance'], ham_tel_22['Speed'], color=COLOR_HAM, label='Hamilton', linewidth=2)
ax2_3.plot(ver_tel_22['Distance'], ver_tel_22['Speed'], color=COLOR_VER, label='Verstappen', linewidth=2,
           linestyle='--')
ax2_3.legend(loc='upper right', framealpha=0.3)

# 4. Engine RPM Line Graph (Lap 22)
ax2_4 = axes2[3]
format_axis_with_turns(ax2_4, "Engine RPM Profile", "RPM")
ax2_4.plot(ham_tel_22['Distance'], ham_tel_22['RPM'], color=COLOR_HAM, label='Hamilton RPM', linewidth=2)
ax2_4.plot(ver_tel_22['Distance'], ver_tel_22['RPM'], color=COLOR_VER, label='Verstappen RPM', linewidth=2,
           linestyle='--')
ax2_4.legend(loc='upper right', framealpha=0.3)

# 5. Braking Pattern (Lap 22)
ax2_5 = axes2[4]
format_axis_with_turns(ax2_5, "Braking Application (On/Off)", "Brake (1=On, 0=Off)")
ax2_5.plot(ham_tel_22['Distance'], ham_tel_22['Brake'], color=COLOR_HAM, label='Hamilton Brake', linewidth=2)
ax2_5.plot(ver_tel_22['Distance'], ver_tel_22['Brake'], color=COLOR_VER, label='Verstappen Brake', linewidth=2,
           linestyle='--')
ax2_5.set_yticks([0, 1])
ax2_5.set_yticklabels(['Released', 'Applied'])
ax2_5.legend(loc='upper right', framealpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('austrialap22.png', facecolor=fig_color, dpi=150)
plt.show()

