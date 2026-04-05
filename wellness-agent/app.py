import streamlit as st
import datetime
from agent.loader import FoodDatabase 
from agent.nutrition_agent import NutritionAgent
from history_manager import HistoryManager

st.set_page_config(page_title="Fitness 2026", page_icon="💪")
history = HistoryManager()

st.title("Fitness & Nutrition Tracker")

# 1. LOGGING
st.subheader("Log Intake")
meals = st.text_input("Items (e.g. 2 roti + 1 chicken_gravy)", placeholder="Use + to separate")

current_p = 0
current_c = 0

if meals:
    db = FoodDatabase()
    agent = NutritionAgent(db.food_info)
    results = agent.observe_intake([m.strip() for m in meals.split("+")])
    
    current_p = results.get('protein', 0)
    # Calculate calories from the updated JSON
    current_c = sum([db.food_info[item['Item'].lower().replace(' ', '_')].get('calories', 0) for item in results['breakdown']])
    
    col1, col2 = st.columns(2)
    col1.metric("Logged Protein", f"{current_p}g")
    col2.metric("Logged Calories", f"{current_c} kcal")

st.divider()

# 2. STATUS & SAVE
st.subheader("Daily Status")
c1, c2 = st.columns(2)
with c1:
    day_type = st.selectbox("Activity", ["Gym Day", "Activity Day", "Rest Day"])
with c2:
    mood = st.select_slider("Mood", options=["Tired", "Neutral", "Energetic"])

if st.button("Save to History"):
    history.log_day(current_c, current_p, day_type, mood)
    st.success(f"Added {current_p}g protein to today's log.")

# 3. HISTORY TABLE
st.divider()
st.subheader("Weekly Progress")
st.dataframe(history.get_history().tail(7), use_container_width=True)