from openai import AzureOpenAI
import pandas as pd
import os
from dotenv import load_dotenv
import time
import threading
import itertools

# Load in variables from .env 
load_dotenv()

# Create embeddings function to apply to a given column
def get_embedding(text, engine):
    client = AzureOpenAI(
        api_key=os.getenv("Azure_OPENAI_KEY"),
        api_version=os.getenv('AZURE_OPENAI_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )
    embeddings = client.embeddings.create(input=[text], model=engine).data[0].embedding
    return embeddings

# Function to display loading pattern
def loading_pattern():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        print('\rLoading ' + c, end='')
        time.sleep(0.1)
    print('\rDone!     ')

# Start the loading pattern in a separate thread
done = False
loading_thread = threading.Thread(target=loading_pattern)
loading_thread.start()

# Read the data file to be embedded
df = pd.read_csv(os.path.join('..', 'microsoft-earnings.csv'))
print(df)

# Calculate word embeddings
df['embedding'] = df['text'].apply(lambda x: get_embedding(x, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT")))

# Save the DataFrame with embeddings to the specified path
file_path = os.path.join('.', 'microsoft-earnings_embeddings.csv')
df.to_csv(file_path, index=False)

# Stop the loading pattern
done = True
loading_thread.join()

# Print the DataFrame with embeddings
time.sleep(3)
print(df)
