import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt
import pandas as pd


fastf1.plotting.setup_mpl(misc_mpl_mods=False)
fastf1.Cache.enable_cache('f1_cache')


session = fastf1.get_session(2026, 'Miami', 'SQ')
session.load()


ver_lap = session.laps.pick_driver('VER').pick_fastest()
nor_lap = session.laps.pick_driver('NOR').pick_fastest()


def get_sectors(lap):
    return {
        'S1': lap['Sector1Time'].total_seconds(),
        'S2': lap['Sector2Time'].total_seconds(),
        'S3': lap['Sector3Time'].total_seconds(),
        'Total': lap['LapTime'].total_seconds()
    }

ver_sectors = get_sectors(ver_lap)
nor_sectors = get_sectors(nor_lap)


ver_tel = ver_lap.get_telemetry().add_distance()
nor_tel = nor_lap.get_telemetry().add_distance()

fig, ax = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [1, 3]})

ax[0].axis('tight')
ax[0].axis('off')
table_data = [
    ['Driver', 'Sector 1', 'Sector 2', 'Sector 3', 'Lap Time'],
    ['Verstappen', f"{ver_sectors['S1']:.3f}", f"{ver_sectors['S2']:.3f}", f"{ver_sectors['S3']:.3f}", f"{ver_sectors['Total']:.3f}"],
    ['Norris', f"{nor_sectors['S1']:.3f}", f"{nor_sectors['S2']:.3f}", f"{nor_sectors['S3']:.3f}", f"{nor_sectors['Total']:.3f}"]
]
ax[0].table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.15]*5)

ax[1].plot(ver_tel['Distance'], ver_tel['Throttle'], color='darkblue', label='Verstappen (Red Bull)')
ax[1].plot(nor_tel['Distance'], nor_tel['Throttle'], color='orange', label='Norris (McLaren)', alpha=0.7)

ax[1].set_xlabel('Distance in m')
ax[1].set_ylabel('Throttle %')
ax[1].set_title('Throttle Level Comparison: VER vs NOR')
ax[1].legend()

plt.tight_layout()
plt.savefig('miami_26_throttle_comparison.png')
plt.show()