import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import os

# 1. Prepare the 'Garage' (Cache)
# This saves the data locally so it runs 10x faster next time.
if not os.path.exists('f1_cache'):
    os.makedirs('f1_cache')
fastf1.Cache.enable_cache('f1_cache')

# 2. Setup the Visuals
plotting.setup_mpl()

# 3. Load the Session
# Let's look at 2024 Saudi Arabia Qualifying
session = fastf1.get_session(2024, 'Jeddah', 'Q')
session.load()

# 4. Select Drivers
# Comparing Verstappen (Blue) vs Leclerc (Red)
ver_lap = session.laps.pick_driver('VER').pick_fastest()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()

# 5. Extract Telemetry
ver_tel = ver_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()

# 6. Create the Plot
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(ver_tel['Distance'], ver_tel['Speed'], color='cyan', label='VER')
ax.plot(lec_tel['Distance'], lec_tel['Speed'], color='red', label='LEC')

ax.set_title('Jeddah 2024: Verstappen vs Leclerc Fastest Lap')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.legend()

# 7. Save and Show
plt.savefig('fastest_lap_comparison.png') # This saves the image for GitHub
plt.show()