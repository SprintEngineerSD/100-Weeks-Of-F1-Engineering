import fastf1
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF


fastf1.Cache.enable_cache('f1_cache')


session = fastf1.get_session(2023, 'Monaco', 'R')
session.load()
telemetry = session.laps.pick_fastest().get_telemetry()
telemetry['v_ms'] = telemetry['Speed'] / 3.6
telemetry['dt'] = telemetry['Date'].diff().dt.total_seconds()


telemetry['accel_ms2'] = telemetry['v_ms'].diff() / telemetry['dt']
telemetry['G_long'] = telemetry['accel_ms2'] / 9.81

telemetry['dx'] = telemetry['X'].diff()
telemetry['dy'] = telemetry['Y'].diff()
telemetry['heading'] = np.arctan2(telemetry['dy'], telemetry['dx'])
telemetry['d_heading'] = telemetry['heading'].diff()
telemetry['G_lat'] = (telemetry['v_ms'] * telemetry['d_heading'] / telemetry['dt']) / 9.81

telemetry = telemetry.dropna(subset=['G_lat', 'G_long'])

telemetry = telemetry[(telemetry['G_lat'].abs() < 6) & (telemetry['G_long'].abs() < 6)]


plt.figure(figsize=(8, 8))
plt.scatter(telemetry['G_lat'], telemetry['G_long'], c=telemetry['Speed'], cmap='magma', s=2, alpha=0.5)
plt.title('G-G Diagram: Monaco 2023')
plt.xlabel('Lateral G')
plt.ylabel('Longitudinal G')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.colorbar(label='Speed (km/h)')
plt.savefig('gg_diagram.png', dpi=300)

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'F1 Performance Engineering Report', 0, 1, 'C')
pdf.ln(5)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Session Details:', 0, 1)
pdf.set_font('Arial', '', 11)
pdf.cell(0, 7, 'Circuit: Monaco Street Circuit', 0, 1)
pdf.cell(0, 7, 'Analysis: Grip Utilization (G-G Diagram)', 0, 1)
pdf.ln(5)


pdf.image('gg_diagram.png', x=15, w=180)
pdf.ln(5)


pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Engineering Summary:', 0, 1)
pdf.set_font('Arial', '', 11)

summary_text = (
    "The G-G diagram indicates high longitudinal grip during braking, but a notable "
    "narrowing of the friction circle during high-speed transitions. This suggests "
    "potential under-utilization of the tire contact patch in mid-corner phases. "
    "Recommendation: Further analyze damper velocities to improve mechanical grip stability."
)
pdf.multi_cell(0, 8, summary_text)

pdf.output('Monaco_2023_Analysis.pdf')