import fastf1
import numpy as np
import  matplotlib.pyplot as plt
from fastf1 import plotting
import os

if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
fastf1.Cache.enable_cache('f1_cache')
plotting.setup_mpl()

session = fastf1.get_session(2026, 'Melbourne', 'Q')
session.load()

rus_lap = session.laps.pick_driver('RUS').pick_fastest()
ant_lap = session.laps.pick_driver('ANT').pick_fastest()

rus_tel = rus_lap.get_car_data().add_distance()
ant_tel = ant_lap.get_car_data().add_distance()


ref_distance = np.linspace(0,rus_tel['Distance'].max(),2000)

rus_time_fixed = np.interp(ref_distance, rus_tel['Distance'],rus_tel['Time'].dt.total_seconds())
ant_time_fixed = np.interp(ref_distance, ant_tel['Distance'], ant_tel['Time'].dt.total_seconds())

delta = ant_time_fixed - rus_time_fixed

fig, ax = plt.subplots(2, gridspec_kw={'height_ratios':[3,1]}, figsize=(12,8))

ax[0].plot(rus_tel['Distance'], rus_tel['Speed'], color='cyan', label='Russell')
ax[0].plot(ant_tel['Distance'], ant_tel['Speed'], color='green', alpha=0.5, label='Antonelli')
ax[0].set_title('Russell vs Antonelli - Delta Analysis (Melbourne 2026)')
ax[0].set_ylabel('Speed (km/h)')
ax[0].legend()


ax[1].plot(ref_distance, delta, color='yellow')
ax[1].axhline(0, color='white', linestyle='--')
ax[1].set_ylabel('Delta (s)')
ax[1].set_xlabel('Distance (m)')

plt.savefig('merc_delta_analysis.png')
plt.show()