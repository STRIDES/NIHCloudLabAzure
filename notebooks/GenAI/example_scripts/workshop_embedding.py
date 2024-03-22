import openai
import pandas as pd
import numpy as np
import os
import streamlit as st
from dotenv import load_dotenv
import time


# load in variables from .env 
load_dotenv()


# set keys and configure Azure OpenAI
os.environ["AZURE_OPENAI_ENDPOINT"] = "<YOUR OPENAI ENDPOINT>"
os.environ["AZURE_OPENAI_KEY"] = "<YOUR OPENAI KEY>"

#create embeddings functions to apply to a given column
    
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2023-05-15",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )]

 
# read the data file to be embed 
df = pd.read_csv('microsoft-earnings.csv')
print(df)

#embeddings function
def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding


# calculate word embeddings
df['embedding'] = df['text'].apply(lambda x: get_embedding(x))
df.to_csv('microsoft-earnings_embeddings.csv', index=False)
time.sleep(3)
print(df)



