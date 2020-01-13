from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('adl01_streamlit-demo/demos')
    Popen(["streamlit", "run", "demo1_philippines.py", "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"])
