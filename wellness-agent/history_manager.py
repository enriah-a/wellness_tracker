import pandas as pd
import datetime
import os

class HistoryManager:
    def __init__(self, filename="fitness_history.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["date", "calories", "protein", "day_type", "mood"])
            df.to_csv(self.filename, index=False)

    def log_day(self, calories, protein, day_type, mood):
        today = datetime.date.today().isoformat()
        df = pd.read_csv(self.filename)
        
        # Update if today exists, otherwise append
        if today in df['date'].values:
            df.loc[df['date'] == today, ["calories", "protein", "day_type", "mood"]] = [calories, protein, day_type, mood]
        else:
            new_row = {"date": today, "calories": calories, "protein": protein, "day_type": day_type, "mood": mood}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        df.to_csv(self.filename, index=False)

    def get_history(self):
        return pd.read_csv(self.filename)