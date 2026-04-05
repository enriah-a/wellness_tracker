import pandas as pd
import datetime
import os

class HistoryManager:
    def __init__(self, filename="fitness_history.csv"):
        # Use a relative path that works on both local and Cloud
        self.filename = filename
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["date", "calories", "protein", "day_type", "mood"])
            df.to_csv(self.filename, index=False)

    def log_day(self, calories, protein, day_type, mood):
        today = datetime.date.today().isoformat()
        df = pd.read_csv(self.filename)
        
        if today in df['date'].values:
            # Increment existing values for the day
            df.loc[df['date'] == today, "calories"] += calories
            df.loc[df['date'] == today, "protein"] += protein
            # Update status/mood to the latest selection
            df.loc[df['date'] == today, ["day_type", "mood"]] = [day_type, mood]
        else:
            new_row = {"date": today, "calories": calories, "protein": protein, "day_type": day_type, "mood": mood}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        df.to_csv(self.filename, index=False)

    def get_history(self):
        return pd.read_csv(self.filename)