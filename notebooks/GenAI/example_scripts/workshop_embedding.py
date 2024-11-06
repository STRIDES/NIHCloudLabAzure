from openai import AzureOpenAI
import pandas as pd
import os
from dotenv import load_dotenv
import time


# load in variables from .env 
load_dotenv()

#create embeddings functions to apply to a given column
def get_embedding(text, engine):
    client = AzureOpenAI(
        api_key=os.getenv("Azure_OPENAI_KEY"),
        api_version=os.getenv('AZURE_OPENAI_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )
    embeddings = client.embeddings.create(input = [text], model=engine).data[0].embedding
    return embeddings

 
# read the data file to be embed 
df = pd.read_csv(os.path.join('..', 'microsoft-earnings.csv'))
print(df)

# calculate word embeddings
df['embedding'] = df['text'].apply(lambda x:get_embedding(x, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT")))
df.to_csv('.\\microsoft-earnings_embeddings.csv', index=False)
time.sleep(3)
print(df)



