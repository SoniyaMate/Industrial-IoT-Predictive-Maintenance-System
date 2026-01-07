## 🎯 Overview

**Industrial-IoT-Predictive-Maintenance-System** is a real-time monitoring and predictive maintenance system designed for manufacturing environments. The dashboard simulates sensor data from factory machines and uses an AI-driven health scoring algorithm to predict equipment failures before they occur, enabling proactive maintenance scheduling.

### 💼 Business Impact

- **Reduces unplanned downtime** by up to 50%
- **Lowers maintenance costs** through predictive scheduling
- **Extends equipment lifespan** with early intervention
- **Improves production efficiency** and customer satisfaction

---

## 🚨 Problem Statement

In modern manufacturing, unexpected machine breakdowns lead to:

- 💰 **Production Loss**: Halted assembly lines cost thousands per hour
- 🔧 **Emergency Repair Costs**: Rush repairs are 3-5x more expensive
- 📦 **Customer Delays**: Late deliveries damage business relationships
- ⚠️ **Safety Risks**: Sudden failures can endanger workers

**Solution**: Predict failures 24-48 hours in advance using sensor data and AI health scoring.

---

## ✨ Key Features

### 🔍 Real-Time Monitoring
- Live sensor tracking for temperature, vibration, and health scores
- Multi-machine dashboard with simultaneous monitoring of 6+ machines
- Instant alerts for critical, warning, and healthy states

### 🤖 Predictive Analytics
- AI-driven health scoring algorithm
- Trend analysis showing gradual degradation patterns
- Early warning system triggers alerts before failure occurs

### 📊 Interactive Visualization
- Dynamic charts with temperature vs health correlation
- Vibration trend analysis for bearing/alignment issues
- Historical data view covering 120-hour operational windows

### 💡 Actionable Insights
- Color-coded status indicators (Critical 🚨 / Warning ⚠️ / Healthy ✅)
- Maintenance recommendations based on severity
- Diagnostic simulation with progress tracking

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive web dashboard |
| **Data Processing** | Pandas, NumPy | Sensor data manipulation |
| **Visualization** | Streamlit Charts | Real-time trend plotting |
| **Language** | Python 3.8+ | Core application logic |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Anaconda (optional but recommended)





### Navigating the Interface

1. **Overview Panel**: View summary metrics for all machines
   - Total machines monitored
   - Critical/Warning/Healthy counts

2. **Machine Selection**: Choose specific machine to analyze
   - Select from dropdown (Machines 101-106)
   - View live sensor readings

3. **Health Assessment**: Review AI-generated recommendations
   - 🚨 Critical: Immediate shutdown required
   - ⚠️ Warning: Schedule inspection
   - ✅ Healthy: Continue normal operations

4. **Historical Analysis**: Toggle between chart views
   - Temperature vs Health Score
   - Vibration Trend Analysis

5. **Diagnostics**: Run simulated diagnostic tests
   - Click "Run Diagnostics" button
   - Monitor progress in real-time

### Understanding the Data

- **Temperature**: Normal range 68-72°C, Critical >100°C
- **Vibration**: Normal range 0.4-0.6g, Critical >1.5g
- **Health Score**: 
  - 90-100%: Healthy ✅
  - 60-89%: Warning ⚠️
  - 0-59%: Critical 🚨

---



### Data Flow
```
Sensor Data Generation → Health Score Calculation → Alert System → Visualization
         ↓                        ↓                      ↓              ↓
    NumPy Random          Algorithmic Scoring      Threshold Check   Streamlit UI
```

### Health Score Algorithm
```python
health = 100 - (temp_deviation * 2.2) - (vibration_deviation * 15)
```

The algorithm penalizes temperature and vibration deviations from baseline values, producing a 0-100% health score.

---

## 📸 Screenshots

### Main Dashboard
<img width="1881" height="814" alt="image" src="https://github.com/user-attachments/assets/d3bba50e-d8e7-471f-b035-bea53e7cad99" />

## 🎬 Demo

### Sample Scenarios

**Scenario 1: Healthy Machine (Machine 101)**
- Temperature: 70°C
- Vibration: 0.52g
- Health: 98%
- Action: Normal monitoring

**Scenario 2: Failing Machine (Machine 104)**
- Temperature: 143°C
- Vibration: 2.86g
- Health: 0%
- Action: Immediate shutdown and maintenance

---

## 🔮 Future Enhancements

- [ ] **Machine Learning Integration**: Train LSTM model on historical failure data
- [ ] **Real-time Alerts**: Email/SMS notifications for critical events
- [ ] **IoT Integration**: Connect to actual sensor APIs
- [ ] **Database Storage**: PostgreSQL for historical data
- [ ] **Advanced Analytics**: Root cause analysis and correlation matrices
- [ ] **Mobile App**: iOS/Android app for maintenance teams
- [ ] **Multi-plant Support**: Monitor multiple factory locations







<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**



</div>

✅ smart_factory_sentinel.py
✅ requirements.txt
✅ README.md

