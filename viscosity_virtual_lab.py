import streamlit as st
import numpy as np

st.set_page_config(page_title="Viscosity Virtual Lab", layout="centered")

st.title("🧪 Virtual Physics Lab – Viscosity")
st.write("Digital Twin Based Viscosity Experiments (B.Sc. Physics)")

method = st.selectbox(
    "Select Experiment",
    ["Poiseuille Method", "Stokes Method", "Ostwald Viscometer"]
)

g = 9.81

# -------------------------------------------------
# POISEUILLE METHOD
# -------------------------------------------------
if method == "Poiseuille Method":
    st.header("Poiseuille Capillary Flow Method")

    n = st.number_input("Number of observations", min_value=2, step=1)
    r = st.number_input("Capillary radius r (m)")
    l = st.number_input("Capillary length l (m)")
    V = st.number_input("Volume of liquid V (m³)")
    rho = st.number_input("Density of liquid ρ (kg/m³)")
    h = st.number_input("Pressure head h (m)")

    eta_values = []

    for i in range(int(n)):
        t = st.number_input(f"Flow time t (s) [{i+1}]", key=f"t{i}")
        delta_p = rho * g * h
        eta = (np.pi * r**4 * delta_p * t) / (8 * V * l)
        eta_values.append(eta)

    if st.button("Calculate Viscosity"):
        eta_avg = np.mean(eta_values)
        st.success(f"Viscosity η = {eta_avg:.4e} Pa·s")

# -------------------------------------------------
# STOKES METHOD
# -------------------------------------------------
elif method == "Stokes Method":
    st.header("Stokes’ Falling Sphere Method")

    n = st.number_input("Number of observations", min_value=2, step=1)
    r = st.number_input("Radius of sphere r (m)")
    rho_s = st.number_input("Density of sphere ρₛ (kg/m³)")
    rho_l = st.number_input("Density of liquid ρₗ (kg/m³)")
    d = st.number_input("Fall distance d (m)")

    eta_values = []

    for i in range(int(n)):
        t = st.number_input(f"Time to fall distance t (s) [{i+1}]", key=f"s{i}")
        v = d / t
        eta = (2 * r**2 * g * (rho_s - rho_l)) / (9 * v)
        eta_values.append(eta)

    if st.button("Calculate Viscosity"):
        eta_avg = np.mean(eta_values)
        st.success(f"Viscosity η = {eta_avg:.4e} Pa·s")

# -------------------------------------------------
# OSTWALD VISCOMETER
# -------------------------------------------------
else:
    st.header("Ostwald Viscometer Method")

    eta_water = 0.001
    rho_water = 1000.0

    t_water = st.number_input("Flow time of water t₁ (s)")
    t_liquid = st.number_input("Flow time of liquid t₂ (s)")
    rho_liquid = st.number_input("Density of liquid ρ₂ (kg/m³)")

    if st.button("Calculate Viscosity"):
        eta = eta_water * (rho_liquid * t_liquid) / (rho_water * t_water)
        st.success(f"Viscosity η = {eta:.4e} Pa·s")
