# 🧠 Personal Wellness Agent (Python)

A local, agentic Python application that helps improve daily wellness by tracking **protein intake from Indian meals**, adjusting nutrition for a **Vata body type**, and **reducing stress** using Samsung Watch data — all using **free tools and APIs only**.

This is a hobby project focused on learning **agentic application design** (observe → reason → act).

---

## ✨ Features

### 🍽️ Protein Tracking (Indian Meals)

* Log daily meals (e.g., idli, dal, paneer, roti)
* Estimate protein intake using a **local food database**
* Track daily and weekly protein totals

### 🌿 Vata-Friendly Nutrition Suggestions

* Rule-based Ayurveda-inspired logic
* Detects imbalances like:

  * Low protein intake
  * Excess dry/cold foods
* Suggests warm, easy-to-digest, protein-rich Indian meals

### 🧘 Stress Monitoring & Breathing Nudges

* Reads stress data exported from **Samsung Health (Watch 5)**
* Detects moderate or high stress levels
* Suggests quick breathing exercises to reduce stress

---

## 🧠 Agentic Design

The app follows a simple agent loop:

```
Observe  →  Reason  →  Act
```

* **Observe:** meals, stress data
* **Reason:** protein targets, Vata rules, stress thresholds
* **Act:** nutrition advice, breathing exercises, reminders

This keeps the system modular and easy to extend.

---

## 🛠️ Tech Stack

All tools are **free** and run locally:

* Python 3.10+
* SQLite (local storage)
* Pandas
* CSV / JSON file inputs
* Optional:

  * Streamlit (dashboard)
  * Rich (better CLI output)
  * Telegram Bot API (notifications)

---

## 📁 Suggested Project Structure

```
wellness-agent/
│
├── data/
│   ├── food_protein.json
│   └── stress_exports/
│
├── agent/
│   ├── observer.py
│   ├── reasoner.py
│   └── actor.py
│
├── database/
│   └── wellness.db
│
├── rules/
│   ├── vata_rules.py
│   └── stress_rules.py
│
├── main.py
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone <repo-url>
cd wellness-agent
```

### 2️⃣ Install Dependencies

```bash
pip install pandas
```

(Optional dependencies can be added later.)

### 3️⃣ Run the Agent

```bash
python main.py
```

---

## 📊 Data Inputs

### Meal Logging

Meals can be logged via:

* CLI input
* JSON / CSV file
* (Future) UI or chatbot

Example:

```
Breakfast: 2 idli + sambar
Lunch: dal chawal
Dinner: paneer sabzi + roti
```

---

### Stress Data

* Export stress data from **Samsung Health**
* Place CSV/JSON files in `data/stress_exports/`
* The agent reads the latest available data

---

## 🧘 Breathing Exercises (Examples)

* 4–6 breathing
* Box breathing
* 1-minute grounding technique

Triggered automatically when stress is moderate or high.

---

## 🔮 Future Extensions

* Weekly wellness summary report
* Telegram or desktop notifications
* LinkedIn conversation topic generator
* LLM-based reasoning (optional, still free)

---

## 🎯 Why This Project?

* No paid APIs
* Practical and personal
* Clear agent architecture
* Beginner-friendly but expandable
* Great learning project for agentic systems

---

## 📜 Disclaimer

This project is **not medical advice**.
It is a personal wellness assistant meant for learning and self-reflection only.