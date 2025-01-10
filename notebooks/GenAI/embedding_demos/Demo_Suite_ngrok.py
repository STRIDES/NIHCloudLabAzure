import os  
from pyngrok import ngrok, conf  
from dotenv import load_dotenv  
import subprocess  
  
# Load environment variables from .env file  
load_dotenv()  
  
# Set up Ngrok configuration  
ngrok_config = conf.PyngrokConfig()  
conf.set_default(ngrok_config)  
  
# Authenticate with Ngrok using the auth token  
ngrok.set_auth_token(os.getenv("ngrok_key"))  
  
# Create a public URL for your local Streamlit app  
public_url = ngrok.connect(8501)  
print("Ngrok Tunnel URL:", public_url)  
  
# Run your Streamlit app  
subprocess.run(["streamlit", "run", "Demo_Suite.py"])  