import streamlit as st
import datetime
from agent.loader import FoodDatabase 
from agent.nutrition_agent import NutritionAgent
import history_manager

st.set_page_config(page_title="Fitness Tracker 2026", page_icon="💪")
history = HistoryManager()

st.title("Fitness & Nutrition Tracker")

# --- SECTION 1: LOGGING MEALS ---
st.subheader("Log Intake")
meals = st.text_input("Items (e.g., 2 boiled_egg + 1 protein_powder)", placeholder="Use + to separate")

total_p = 0
total_c = 0

if meals:
    db = FoodDatabase()
    agent = NutritionAgent(db.food_info)
    # Note: Update your NutritionAgent to also return 'calories' from the JSON
    results = agent.observe_intake([m.strip() for m in meals.split("+")])
    
    total_p = results['protein']
    # If you added calories to your JSON:
    total_c = sum([db.food_info[item['Item'].lower().replace(' ', '_')].get('calories', 0) for item in results['breakdown']])
    
    col1, col2 = st.columns(2)
    col1.metric("Protein", f"{total_p}g")
    col2.metric("Est. Calories", f"{total_c} kcal")

st.divider()

# --- SECTION 2: DAY STATUS & MOOD ---
st.subheader("End of Day Status")
col_a, col_b = st.columns(2)

with col_a:
    day_type = st.selectbox("Activity Level", ["Gym Day", "Activity Day (Walk/Run)", "Rest Day"])
with col_b:
    mood = st.select_slider("How are you feeling?", options=["Exhausted", "Tired", "Neutral", "Energetic", "Peak"])

if st.button("Save Daily Log"):
    history.log_day(total_c, total_p, day_type, mood)
    st.success("Stats recorded for today!")

# --- SECTION 3: RECENT HISTORY ---
st.divider()
st.subheader("Progress Log")
st.dataframe(history.get_history().tail(7), use_container_width=True)