
# run_app.py
# import threading
# import os
# import time
# import streamlit.web.cli as stcli
# import sys

# # Import your Flask backend
# from server import app

# # Backend port (internal only)
# BACKEND_PORT = int(os.getenv("BACKEND_PORT", "5001"))

# def run_backend():
#     """Run Flask backend inside the same container (background thread)."""
#     app.run(host="0.0.0.0", port=BACKEND_PORT, debug=False, use_reloader=False)

# if __name__ == "__main__":
#     # Start backend in a background thread
#     backend_thread = threading.Thread(target=run_backend, daemon=True)
#     backend_thread.start()

#     # Give backend a moment to start
#     time.sleep(2)

#     # Start Streamlit on Render's $PORT
#     sys.argv = [
#         "streamlit",
#         "run",
#         "login.py",
#         "--server.port",
#         os.getenv("PORT", "8501"),
#         "--server.address",
#         "0.0.0.0",
#         "--server.headless",
#         "true",
#     ]
#     stcli.main()


# # run_app.py
import subprocess
import os
import time
import platform
import streamlit as st

# Backend port
BACKEND_PORT = os.getenv("BACKEND_PORT", "5001")

if platform.system() == "Windows":
    # On Windows, run Flask directly
    subprocess.Popen(["python", "server.py"])
else:
    # On Linux (Render/production), use Gunicorn
    subprocess.Popen([
        "gunicorn",
        "server:app",
        "--bind", f"0.0.0.0:{BACKEND_PORT}"
    ])

# Wait a few seconds to ensure backend is up
time.sleep(3)

# Now start Streamlit frontend
st.run = True  # optional flag if needed in your code
subprocess.run([
    "streamlit",
    "run",
    "landing.py",
    "--server.port",
    os.getenv("FRONTEND_PORT", "8501"),
    "--server.address",
    "0.0.0.0",
    "--server.headless",
    "true"
])






