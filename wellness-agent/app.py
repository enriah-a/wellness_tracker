import streamlit as st
import json
from agent.loader import load_food_data
from agent.observer import calculate_total_protein_intake

# Page Config
st.set_page_config(page_title="Wellness Agent", page_icon="🥗")

def run_app():
    st.title("🥗 Personal Wellness Agent")
    st.markdown("Log your meals below to calculate your daily protein intake.")

    # 1. Load Data
    food_category, food_info = load_food_data()

    # 2. UI Inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("☀️ Breakfast")
        b_input = st.text_input("e.g. 2 idli + sambar", key="b")
    with col2:
        st.subheader("🕛 Lunch")
        l_input = st.text_input("e.g. 3 roti + chicken_gravy", key="l")
    with col3:
        st.subheader("🌙 Dinner")
        d_input = st.text_input("e.g. grilled_chicken_breast", key="d")

    if st.button("Calculate Daily Total", type="primary"):
        # 3. Parsing Logic (same as your loader but simplified for UI)
        def parse_text(text):
            if not text: return []
            items = text.split('+')
            parsed = []
            for item in items:
                parts = item.strip().split(' ')
                if parts[0].isdigit():
                    qty = int(parts[0])
                    food = "_".join(parts[1:]).strip().lower()
                else:
                    qty = 1
                    food = "_".join(parts).strip().lower()
                parsed.append((food, qty))
            return parsed

        # Flatten inputs for the observer
        all_meals = parse_text(b_input) + parse_text(l_input) + parse_text(d_input)
        flat_log = {}
        for food, qty in all_meals:
            flat_log[food] = flat_log.get(food, 0) + qty

        # 4. Calculate Protein
        total_protein = calculate_total_protein_intake(food_info, flat_log)

        # 5. Display Results
        st.divider()
        st.metric(label="Total Protein Intake", value=f"{total_protein}g")

        if total_protein < 80:
            st.warning(f"You are {80 - total_protein}g away from your 80g goal.")
            
            # 6. Suggestions UI
            st.subheader("💪 High Protein Snack Suggestions")
            suggestions = []
            for food, info in food_info.items():
                if "snack" in info.get("meal_type", []):
                    suggestions.append((food.replace('_', ' ').title(), info["protein"]))
            
            suggestions.sort(key=lambda x: x[1], reverse=True)
            
            # Display suggestions in a clean list
            for name, prot in suggestions[:5]:
                st.write(f"• **{name}**: {prot}g protein")
        else:
            st.success("Target Reached! You've hit your protein goal for the day.")

if __name__ == "__main__":
    run_app()