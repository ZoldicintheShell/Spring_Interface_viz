import streamlit as st
# Install the plotly package
subprocess.check_call(['pip', 'install', 'plotly'])

import numpy as np
import plotly.graph_objects as go

# Define the Streamlit app
def app():
    # Set the title and page icon
    st.set_page_config(page_title="Mass Spring Simulation", page_icon=":weight_lifting:")

    # Add a title and description to the app
    st.title("Mass Spring Simulation")
    st.write("This app simulates a mass spring system using numerical integration.")

    # Define the parameters of the mass spring system
    m = st.slider("Mass (kg)", 0.1, 10.0, 1.0, 0.1)  # mass of the object in kg
    k = st.slider("Spring constant (N/m)", 0.1, 10.0, 1.0, 0.1)  # spring constant in N/m
    gamma = st.slider("Damping coefficient (Ns/m)", 0.1, 1.0, 0.1, 0.1)  # damping coefficient in Ns/m

    # Define the simulation parameters
    dt = 0.01  # time step in seconds
    t_end = 10.0  # end time of simulation in seconds

    # Define the initial conditions of the mass spring system
    x0 = 0.1  # initial position in m
    v0 = 0.0  # initial velocity in m/s

    # Initialize the time and position arrays
    t = np.arange(0, t_end, dt)
    x = np.zeros_like(t)
    x[0] = x0

    # Run the simulation using numerical integration
    for i in range(1, len(t)):
        x[i] = x[i-1] + dt * v0
        v0 = v0 - dt * (k * x[i] + gamma * v0) / m

    # Plot the position of the mass over time using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=x))
    fig.update_layout(
        xaxis_title="Time (s)",
        yaxis_title="Position (m)",
        title="Mass Spring Simulation"
    )
    st.plotly_chart(fig)

# Run the app
if __name__ == "__main__":
    app()
