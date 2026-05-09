import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import os

if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
fastf1.Cache.enable_cache('f1_cache')

plotting.setup_mpl()

session = fastf1.get_session(2024, 'Jeddah', 'Q')
session.load()

# Comparing Verstappen (Blue) vs Leclerc (Red)
ver_lap = session.laps.pick_driver('VER').pick_fastest()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()

ver_tel = ver_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(ver_tel['Distance'], ver_tel['Speed'], color='cyan', label='VER')
ax.plot(lec_tel['Distance'], lec_tel['Speed'], color='red', label='LEC')

ax.set_title('Jeddah 2024: Verstappen vs Leclerc Fastest Lap')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.legend()
plt.savefig('fastest_lap_lestappen.png')
plt.show()