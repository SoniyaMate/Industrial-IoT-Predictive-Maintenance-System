import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="SmartFactory Sentinel",
    page_icon="🛠️",
    layout="wide"
)

# --- SIDEBAR / BRANDING ---
st.sidebar.title("🛠️ SmartFactory Sentinel")
st.sidebar.caption("AI-powered predictive maintenance dashboard")
st.sidebar.markdown("---")
st.sidebar.info("System Status: CONNECTED 🟢")
st.sidebar.markdown("**Mode:** Demo (Simulated Sensor Stream)")

# --- 1. THE PROBLEM (BUSINESS CONTEXT) ---
st.title("🛠️ SmartFactory Sentinel – AI Maintenance System")
st.markdown(
    """
    In manufacturing, unexpected machine breakdowns cause **production loss**, **urgent repair costs**, 
    and **customer delays**.  
    This dashboard simulates an AI maintenance system that predicts failures **before** they happen.
    """
)

# --- 2. GENERATE DATA (DATA ENGINEER PART) ---
@st.cache_data
def get_sensor_data(num_machines: int = 6, hours: int = 120) -> pd.DataFrame:
    records = []
    critical_machine = 104  # This one will gradually fail in the simulation
    for machine_id in range(101, 101 + num_machines):
        for hour in range(hours):
            is_breaking = (machine_id == critical_machine) and (hour >= 80)
            base_temp = 70
            base_vib = 0.5

            temp = base_temp + np.random.normal(0, 2)
            vib = base_vib + np.random.normal(0, 0.08)

            if is_breaking:
                temp += (hour - 80) * 1.8
                vib += (hour - 80) * 0.06

            # Simple "AI" style health score
            health = max(0, 100 - (temp - base_temp) * 2.2 - (vib - base_vib) * 15)

            records.append(
                {
                    "Machine_ID": machine_id,
                    "Hour": hour,
                    "Temperature": temp,
                    "Vibration": vib,
                    "Health_Score": health,
                }
            )

    df_local = pd.DataFrame(records)
    return df_local

df = get_sensor_data()

# --- 3. GLOBAL SUMMARY CARDS (MANAGEMENT VIEW) ---
latest = df.sort_values("Hour").groupby("Machine_ID").tail(1)

total_machines = latest["Machine_ID"].nunique()
critical_count = (latest["Health_Score"] < 60).sum()
warning_count = ((latest["Health_Score"] >= 60) & (latest["Health_Score"] < 90)).sum()
healthy_count = (latest["Health_Score"] >= 90).sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Machines", total_machines)
c2.metric("Critical", critical_count)
c3.metric("Warning", warning_count)
c4.metric("Healthy", healthy_count)

st.markdown("---")

# --- 4. MACHINE-LEVEL DASHBOARD ---
col_left, col_right = st.columns([2, 3])

with col_left:
    st.subheader("🔎 Machine Selection")

    selected_machine = st.selectbox(
        "Select Machine ID",
        options=sorted(df["Machine_ID"].unique()),
        index=3  # default to 104 (failing)
    )

    machine_data = df[df["Machine_ID"] == selected_machine].sort_values("Hour")
    current = machine_data.iloc[-1]

    st.markdown("#### Live Sensor Snapshot")
    m1, m2, m3 = st.columns(3)
    m1.metric("Temperature", f"{current['Temperature']:.1f} °C")
    m2.metric("Vibration", f"{current['Vibration']:.3f} g")
    m3.metric("Health Score", f"{int(current['Health_Score'])}%")

    st.markdown("#### AI Health Assessment")
    if current["Health_Score"] < 60:
        st.error(
            f"🚨 CRITICAL: Machine {selected_machine} is in failure zone.\n\n"
            "Recommended action: Schedule **immediate shutdown and maintenance** "
            "to avoid unplanned downtime."
        )
    elif current["Health_Score"] < 90:
        st.warning(
            f"⚠️ WARNING: Machine {selected_machine} shows early risk.\n\n"
            "Recommended action: Plan **inspection in next maintenance window**."
        )
    else:
        st.success(
            f"✅ Machine {selected_machine} is operating within safe limits.\n\n"
            "Recommended action: Continue **normal monitoring**."
        )

    st.markdown("#### Diagnostics Simulation")
    if st.button("Run Diagnostics"):
        progress = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
            status.text(f"Running diagnostics... {i + 1}%")
        status.text("Diagnostics complete. Report synced to server.")
        st.toast("Diagnostics Complete ✅")

with col_right:
    st.subheader(f"📈 Sensor History – Machine {selected_machine}")

    view = st.radio(
        "Select view",
        ["Temperature vs Health", "Vibration Trend"],
        horizontal=True
    )

    machine_data_plot = machine_data.set_index("Hour")

    if view == "Temperature vs Health":
        st.line_chart(
            machine_data_plot[["Temperature", "Health_Score"]],
            height=350
        )
        st.caption(
            "Temperature should stay stable while Health_Score should remain close to 100%. "
            "In the failing machine, temperature climbs while health degrades."
        )
    else:
        st.line_chart(
            machine_data_plot[["Vibration"]],
            height=350
        )
        st.caption(
            "Abnormal rise in vibration often indicates bearing or alignment issues."
        )

st.markdown("---")
st.markdown(
    """
    **How you explain in interview:**  
    “This dashboard simulates multiple factory machines and computes a Health Score from sensor data.  
    When the score drops below a threshold, it raises alerts so the maintenance team can act **before** breakdown.”
    """
)
