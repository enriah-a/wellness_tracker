import streamlit as st
import pandas as pd
import plotly.express as px
from agent.loader import FoodDatabase  # Import the class
from agent.nutrition_agent import NutritionAgent

# Page Config
st.set_page_config(page_title="Wellness Agent", page_icon="🥗", layout="wide")

def run_app():
    st.title("🥗 Agentic Wellness Tracker")
    
    # 1. Initialize Data and Agent
    # Instantiate the class once at the start of the app
    @st.cache_resource
    def init_agent():
        db = FoodDatabase() # Uses default path from your loader.py
        return NutritionAgent(db.food_info)

    agent = init_agent()
    user_goal = st.number_input("Enter your daily protein target (g)", min_value=10, max_value=300, value=80)

    # 2. UI Inputs
    st.markdown("Enter meals using `+` to separate items (e.g., *2 eggs + 1 toast*)")
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1: b = st.text_input("☀️ Breakfast", key="b")
    with col_in2: l = st.text_input("🕛 Lunch", key="l")
    with col_in3: d = st.text_input("🌙 Dinner", key="d")

    if st.button("Analyze Meals", type="primary"):
        # Combine and clean inputs
        raw_input_string = f"{b}+{l}+{d}"
        # Filter out empty strings if user left a meal blank
        raw_log = [item.strip() for item in raw_input_string.split("+") if item.strip()]
        
        # 3. Agentic Observation
        total_p, breakdown, missing = agent.observe_intake(raw_log)

        if breakdown:
            # 4. Data Preparation
            df = pd.DataFrame(breakdown).groupby("Item")["Protein"].sum().reset_index()
            df_sorted = df.sort_values(by="Protein", ascending=False)
            
            # Prepare Stacked Data
            plot_df = df_sorted.head(5).copy()
            others_val = df_sorted.iloc[5:]["Protein"].sum()
            if others_val > 0:
                plot_df = pd.concat([plot_df, pd.DataFrame([{"Item": "Others", "Protein": others_val}])])
            plot_df["Label"] = "Current Intake"

            # 5. UI Layout
            st.divider()
            res_col1, res_col2 = st.columns([1, 2])

            with res_col1:
                st.metric("Total Protein", f"{total_p}g")
                
                if missing:
                    with st.expander("⚠️ Unmatched Items"):
                        for m in missing:
                            st.write(f"- {m}")
                
                if total_p < user_goal:
                    st.warning(f"🏃 {round(user_goal - total_p, 1)}g to go!")
                else:
                    st.success("Target Reached!")
                    st.balloons()

            with res_col2:
                fig = px.bar(
                    plot_df, x="Label", y="Protein", color="Item",
                    title="Daily Protein Stack", text_auto=True,
                    color_discrete_sequence=px.colors.qualitative.Vivid
                )
                fig.add_hline(y=user_goal, line_dash="dash", line_color="red", 
                             annotation_text=f"{user_goal}g Goal", annotation_position="top left")
                fig.update_layout(yaxis_range=[0, max(total_p + 10, user_goal + 10)], xaxis_title="")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No valid food items recognized. Please check your spelling or database.")

if __name__ == "__main__":
    run_app()