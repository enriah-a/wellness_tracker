import subprocess
import os
import sys

def launch():
    # 1. Define Paths based on your setup
    project_root = "/Users/anujalele/PythonProjects/wellness_tracker"
    venv_python = os.path.join(project_root, ".venv/bin/python")
    app_path = os.path.join(project_root, "wellness-agent/app.py")
    
    # 2. Check if venv exists
    if not os.path.exists(venv_python):
        print(f"❌ Error: Virtual environment not found at {venv_python}")
        return

    # 3. Construct the Streamlit command
    # We run it as: .venv/bin/python -m streamlit run wellness-agent/app.py
    cmd = [venv_python, "-m", "streamlit", "run", app_path]

    print(f"🚀 Launching Wellness Tracker...")
    print(f"📂 App: {app_path}")
    
    try:
        # 4. Execute the command
        # We set the current working directory (cwd) to the folder containing app.py
        # so that imports like 'from agent.loader' work correctly.
        subprocess.run(cmd, cwd=os.path.join(project_root, "wellness-agent"))
    except KeyboardInterrupt:
        print("\n👋 Wellness Tracker stopped.")

if __name__ == "__main__":
    launch()