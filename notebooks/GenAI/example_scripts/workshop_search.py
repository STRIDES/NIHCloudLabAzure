import openai
import pandas as pd
import numpy as np
import os
import streamlit as st
from dotenv import load_dotenv



load_dotenv()

# set keys and configure Azure OpenAI
os.environ["AZURE_OPENAI_ENDPOINT"] = "<YOUR OPENAI ENDPOINT>"
os.environ["AZURE_OPENAI_KEY"] = "<YOUR OPENAI KEY>"

#create embeddings functions to apply to a given column
    
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2023-05-15",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

#create cosine function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# read in the embeddings .csv 
# convert elements in 'embedding' column back to numpy array
df = pd.read_csv('microsoft-earnings_embeddings.csv')
df['embedding'] = df['embedding'].apply(eval).apply(np.array)

# caluculate user query embedding 
search_term = input("Enter a search term: ")
if search_term:
    search_term_vector = get_embedding(search_term, engine='text-embedding-ada-002')

    # find similiarity between query and vectors 
    df['similarities'] = df['embedding'].apply(lambda x:cosine_similarity(x, search_term_vector))
    df1 = df.sort_values("similarities", ascending=False).head(5)

    # output the response 
    print('\n')
    print('Answer: ', df1['text'].loc[df1.index[0]])
    print('\n')
    print('Similarity Score: ', df1['similarities'].loc[df1.index[0]]) 
    print('\n')
