import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
fastf1.Cache.enable_cache('f1_cache')
fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')
print("Loading FP1 Data...")
fp1 = fastf1.get_session(2026, 'Canada', 'FP1')
fp1.load(telemetry=True, weather=True)
print("Loading Sprint Data...")
sprint = fastf1.get_session(2026, 'Canada', 'Sprint')
sprint.load(telemetry=True, weather=True)

ver_fp1 = fp1.laps.pick_drivers('VER').pick_fastest()
ver_sprint = sprint.laps.pick_drivers('VER').pick_fastest()
tel_fp1 = ver_fp1.get_telemetry().add_distance()
tel_sprint = ver_sprint.get_telemetry().add_distance()


fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)
fig.suptitle("Max Verstappen Setup Instability: 2026 Canadian GP (FP1 vs Sprint)", fontsize=16, fontweight='bold')

ax1 = axes[0]
ax1.plot(tel_fp1['Distance'], tel_fp1['Speed'], label='FP1 (Baseline Setup)', color='white', linewidth=2)
ax1.plot(tel_sprint['Distance'], tel_sprint['Speed'], label='Sprint (Stiff Setup)', color='red', alpha=0.8, linewidth=2)
ax1.set_title("Velocity (km/h) - Notice the speed delta at the end of the main straights")
ax1.set_ylabel("Speed (km/h)")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2 = axes[1]
ax2.plot(tel_fp1['Distance'], tel_fp1['Throttle'],label='FP1 (Baseline Setup)', color='white', linewidth=2)
ax2.plot(tel_sprint['Distance'], tel_sprint['Throttle'], label='Sprint (Stiff Setup)', color='cyan', alpha=0.8, linewidth=2)
ax2.set_title("Throttle % - Look for 'feathering' or early lifts in the Sprint trace")
ax2.set_ylabel("Throttle (%)")
ax2.legend()
ax2.grid(True, alpha=0.3)


ax3 = axes[2]
ax3.plot(tel_fp1['Distance'], tel_fp1['Brake'],label='FP1 (Baseline Setup)', color='white', linewidth=2)
ax3.plot(tel_sprint['Distance'], tel_sprint['Brake'], label='Sprint (Stiff Setup)', color='magenta', alpha=0.8, linewidth=2)
ax3.set_title("Brake Application - Look for staggered/erratic braking zones vs smooth FP1 inputs")
ax3.set_xlabel("Track Distance (Meters)")
ax3.set_ylabel("Brake (On/Off)")
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('VerstappenCNGP26.png', dpi=300)
plt.show()

fp1_time = ver_fp1['LapTime'].total_seconds()
sprint_time = ver_sprint['LapTime'].total_seconds()
print(f"FP1 Fastest Lap: {fp1_time:.3f}s")
print(f"Sprint Fastest Lap: {sprint_time:.3f}s")
print(f"Time Delta: {sprint_time - fp1_time:+.3f}s")