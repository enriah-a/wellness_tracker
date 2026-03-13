import streamlit as st
import datetime
from agent.loader import FoodDatabase 
from agent.nutrition_agent import NutritionAgent

# Page Config: Designed for mobile-first viewing
st.set_page_config(page_title="Q2 2026 System", page_icon="⚖️", layout="wide")

def run_app():
    now = datetime.datetime.now()
    today_name = now.strftime("%A")
    current_time = now.time()
    
    # Time-based state checks
    is_after_hours = current_time >= datetime.time(20, 30)
    is_morning = current_time < datetime.time(11, 0)

    # 1. VISUAL FRAME: BOUNDARY AWARENESS
    if is_after_hours:
        st.warning("🌙 **Post-8:30 PM: Work fully stopped.**")
        with st.expander("Bedtime Sequence", expanded=True):
            st.write("Warm oil → Warm milk (saffron/ghee) → Anulom Vilom")
            st.caption("Lights out by 10:45pm.")
    else:
        st.title("Q2 2026: The Vessel & The Architect")

    # 2. MORNING ANCHOR (Low-effort checklist)
    with st.expander("Morning Anchor", expanded=is_morning):
        c1, c2 = st.columns(2)
        c1.checkbox("Kesar water & Raisins")
        c1.checkbox("Multivitamins")
        c2.checkbox("Fruit")
        c2.checkbox("Hydration: 1L by Noon")

    # 3. NOURISHMENT & THE 6PM BLOCK
    st.divider()
    workout_days = ["Monday", "Wednesday", "Friday"]
    is_workout = today_name in workout_days
    
    col_block, col_daily = st.columns(2)
    with col_block:
        st.subheader(f"6pm Block: {today_name}")
        if is_workout:
            st.info("Gym or CULT (Strength) + Kegels")
        else:
            st.success("Restore (Walk/Dance/Book) + Kegels")

    with col_daily:
        st.subheader("Daily Requirements")
        st.checkbox("Ghee (1 tsp)")
        st.checkbox("3L Water Total")

    # 4. BRIDGESPAN FRIDAY
    if today_name == "Friday":
        st.info("📤 **Friday Manager Update:** 3 sentences on status & needs.")

    # 5. MEAL LOGGING (Functional/Direct)
    st.divider()
    meals = st.text_input("Log intake (+ separator)", placeholder="e.g. 2 eggs + chicken")
    
    if meals:
        db = FoodDatabase()
        agent = NutritionAgent(db.food_info)
        results = agent.observe_intake([m.strip() for m in meals.split("+")])
        
        # Displaying results with objective targets
        p_target = 75 if is_workout else 60
        
        m1, m2 = st.columns(2)
        m1.metric("Protein", f"{results['protein']}g / {p_target}g")
        m2.metric("Iron", f"{results['iron']}mg / 18mg")
        
        if not results['q2_checks']['meat_or_shake']:
            st.caption("⚠️ Daily meat or protein shake pending.")

    # 6. TTC GROUNDING
    if st.button("Grounding Action (Anti-Google)"):
        st.toast("Breath: Five minutes of silence. Focus on the Vessel.")

if __name__ == "__main__":
    run_app()
