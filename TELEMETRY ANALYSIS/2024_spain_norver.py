import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt


plotting.setup_mpl(misc_mpl_mods=False)


session = fastf1.get_session(2024, 'Spain', 'Q')
session.load()


lap_nor = session.laps.pick_driver('NOR').pick_fastest()
lap_ver = session.laps.pick_driver('VER').pick_fastest()


tel_nor = lap_nor.get_telemetry().add_distance()
tel_ver = lap_ver.get_telemetry().add_distance()


fig, ax = plt.subplots(figsize=(12, 6))


ax.plot(tel_nor['Distance'], tel_nor['Speed'], color='#FF8700', label='Norris (Pole)')
ax.plot(tel_ver['Distance'], tel_ver['Speed'], color='#0600EF', label='Verstappen', linestyle='--')


ax.set_xlabel('Distance in meters')
ax.set_ylabel('Speed in km/h')
ax.set_title(f"2024 Spanish GP Qualifying: \n {lap_nor.Driver} vs {lap_ver.Driver}")
ax.legend()
ax.grid(True, linestyle=':', alpha=0.7)


ax.set_xlim(0, 1000)
plt.savefig('2024_spain_norver.png')
plt.show()

