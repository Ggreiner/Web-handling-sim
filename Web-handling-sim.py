import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
INCH_TO_FT = 1 / 12

st.sidebar.title("Web Handling System Inputs")

line_speed_ftmin = st.sidebar.slider("Line Speed (ft/min)", 50, 250, 100)
web_width_in = st.sidebar.slider("Web Width (inches)", 6, 36, 12)
initial_unwind_od_in = st.sidebar.slider("Initial Unwind OD (in)", 10, 18, 18)
final_unwind_od_in = st.sidebar.slider("Final Unwind OD (in)", 3, 9, 3)
initial_winder_od_in = st.sidebar.slider("Initial Winder OD (in)", 3, 9, 3)
final_winder_od_in = st.sidebar.slider("Final Winder OD (in)", 10, 18, 18)
nip_roll_od_in = 4
runtime_min = st.sidebar.slider("Simulated Runtime (minutes)", 1, 10, 5)

time_s = np.linspace(0, runtime_min * 60, 300)
unwind_od_in = np.linspace(initial_unwind_od_in, final_unwind_od_in, len(time_s))
winder_od_in = np.linspace(initial_winder_od_in, final_winder_od_in, len(time_s))

def calculate_rpm(speed_ftmin, diameter_in):
    diameter_ft = diameter_in * INCH_TO_FT
    circumference_ft = PI * diameter_ft
    return speed_ftmin / circumference_ft if circumference_ft != 0 else 0

unwind_rpm = [calculate_rpm(line_speed_ftmin, d) for d in unwind_od_in]
nip_rpm = calculate_rpm(line_speed_ftmin, nip_roll_od_in)
winder_rpm = [calculate_rpm(line_speed_ftmin, d) for d in winder_od_in]

st.title("Web Handling System - Dynamic Roll Simulation")

st.write(f"**Line Speed**: {line_speed_ftmin} ft/min")
st.write(f"**Web Width**: {web_width_in} in")
st.write(f"**Nip Roll OD**: {nip_roll_od_in} in (constant)")
st.write(f"**Runtime**: {runtime_min} minutes")

fig, ax = plt.subplots()
ax.plot(time_s / 60, unwind_rpm, label="Unwind RPM")
ax.plot(time_s / 60, [nip_rpm]*len(time_s), label="Nip RPM", linestyle="--")
ax.plot(time_s / 60, winder_rpm, label="Winder RPM")
ax.set_xlabel("Time (min)")
ax.set_ylabel("RPM")
ax.set_title("Roll RPM Over Time")
ax.legend()
ax.grid(True)
st.pyplot(fig)
