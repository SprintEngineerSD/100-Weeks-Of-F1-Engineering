import fastf1
import os
from fastf1 import plotting
import matplotlib.pyplot as plt


cache_path = r'TELEMETRY ANALYSIS/f1_cache'
if not os.path.exists(cache_path):
    os.makedirs(cache_path)

fastf1.Cache.enable_cache(cache_path)


plotting.setup_mpl(misc_mpl_mods=False)
session = fastf1.get_session(2024, 'Spain', 'Q')
session.load(telemetry=True)

lap_nor = session.laps.pick_driver('NOR').pick_fastest()
lap_ver = session.laps.pick_driver('VER').pick_fastest()

tel_nor = lap_nor.get_telemetry().add_distance()
tel_ver = lap_ver.get_telemetry().add_distance()

color_nor = '#FF8700'
color_ver = '#0600EF'

fig, (ax_speed, ax_throttle, ax_brake) = plt.subplots(
    nrows=3, ncols=1, figsize=(12, 10), sharex=True,
    gridspec_kw={'height_ratios': [3, 1, 1]}
)


ax_speed.plot(tel_nor['Distance'], tel_nor['Speed'], color=color_nor, label='Norris (Pole)')
ax_speed.plot(tel_ver['Distance'], tel_ver['Speed'], color=color_ver, label='Verstappen', linestyle='--')
ax_speed.set_ylabel('Speed (km/h)')
ax_speed.set_title('Spain 2024 Qualifying: Norris vs Verstappen')
ax_speed.legend(loc='lower right')
ax_speed.grid(True, linestyle=':', alpha=0.7)


ax_throttle.plot(tel_nor['Distance'], tel_nor['Throttle'], color=color_nor)
ax_throttle.plot(tel_ver['Distance'], tel_ver['Throttle'], color=color_ver, linestyle='--')
ax_throttle.set_ylabel('Throttle (%)')
ax_throttle.set_ylim(0, 105)
ax_throttle.grid(True, linestyle=':', alpha=0.7)


ax_brake.plot(tel_nor['Distance'], tel_nor['Brake'], color=color_nor)
ax_brake.plot(tel_ver['Distance'], tel_ver['Brake'], color=color_ver, linestyle='--')
ax_brake.set_ylabel('Brake')
ax_brake.set_xlabel('Distance in meters')
ax_brake.grid(True, linestyle=':', alpha=0.7)

plt.xlim(0, 1500)

plt.tight_layout()
plt.show()
fig.savefig('Spain_2024_Full_Telemetry.png', dpi=300)