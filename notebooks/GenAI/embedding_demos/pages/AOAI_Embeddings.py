from openai import AzureOpenAI
# from openai.embeddings_utils import get_embedding, cosine_similarity # must pip install openai[embeddings]
import pandas as pd
import numpy as np
import os
import streamlit as st
import time
from PIL import Image
from dotenv import load_dotenv
from styling import global_page_style

# load in .env variables
load_dotenv()

# configure azure openai keys
# openai.api_type = 'azure'
# openai.api_version = os.environ['AZURE_OPENAI_VERSION']
# openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
# openai.api_key = os.environ['AZURE_OPENAI_KEY']

def get_embedding(text, engine):
    client = AzureOpenAI(
        api_key=os.getenv("Azure_OPENAI_KEY"),
        api_version=os.getenv('AZURE_OPENAI_VERSION'),
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
    )

    embeddings = client.embeddings.create(input = [text], model=engine).data[0].embedding
    return embeddings

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def embedding_create():
    # acquire the filename to be embed
    st.subheader("Vector Creation")
    st.write('The process of vectorization involves creating embeddings from the [microsoft-earnings.csv](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/notebooks/GenAI/microsoft-earnings.csv) \
              file located in the specified directory, utilizing the data in the "text" column. These embeddings are derived from pre-chunked text, \
             indicating that the text has already been divided and formatted for embedding generation. The resultant embeddings will be \
             compiled into a new CSV file, which will serve as a vector store for future reference and utilization.')
    filename = st.text_input("Enter a file: ", key='filename', value="microsoft-earnings.csv")

    # start the embeddings process if filename provided
    if filename:
        file_path = os.path.join('..', filename)
        # read the data file to be embed 
        df = pd.read_csv(file_path)
        df_placeholder = st.empty()
        df_placeholder.dataframe(df, width=2000, height=350)
        button_placeholder = st.empty()
        if button_placeholder.button("Generate Embeddings"):
            # calculate word embeddings 
            df['embedding'] = df['text'].apply(lambda x:get_embedding(x, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT")))
            df.to_csv('.\\microsoft-earnings_embeddings.csv')
            time.sleep(3)
            button_placeholder.success('Embeddings Created Sucessfully!!')
            df_placeholder.dataframe(df)


def embeddings_search():

    # Streamlit configuration
    st.subheader("Vector Search")
    st.write('''
This process generates embeddings based on user queries, utilizing the compiled CSV that was created, to search for the most similar
documents within the vector store by employing cosine similarity. Example questions a user can ask about the microsoft-earnings.csv: 
- What was said about the budget?
- How many people utilize GitHub to build software?
- How many points did Microsoft Cloud gross margin percentage increase by?
- What are the expectations for the Q2 cash flow?''')
    
    if 'answer' not in st.session_state:
        st.session_state.answer = []  
    if 'score' not in st.session_state:
        st.session_state.score = []     
    if 'past' not in st.session_state:
        st.session_state.past = []  

    # read in the embeddings .csv 
    # convert elements in 'embedding' column back to numpy array
    df = pd.read_csv('.\\microsoft-earnings_embeddings.csv')
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)

    # caluculate user query embedding 
    search_term = st.text_area("Enter a search query: ", key='search_term', placeholder="")
    if search_term:
        st.session_state.past.append(search_term)
        search_term_vector = get_embedding(search_term, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"))

        # find similiarity between query and vectors 
        df['similarities'] = df['embedding'].apply(lambda x:cosine_similarity(x, search_term_vector))
        df1 = df.sort_values("similarities", ascending=False).head(5)

        # output the response 
        answer = df1['text'].loc[df1.index[0]]
        score = df1['similarities'].loc[df1.index[0]]
        st.session_state.answer.append(answer)
        st.session_state.score.append(score)
        with st.expander('Vector Search'):
            for i in range(len(st.session_state.answer)-1, -1, -1):
                st.info(st.session_state.past[i])
                st.write(st.session_state.answer[i])
                st.write('Score: ', st.session_state.score[i])
        with st.expander('Top 5 Results'):
            df1 = df1.reset_index(drop=True)   
            df1.index = df1.index + 1  
            df1 = df1.rename(columns={'Unnamed: 0': 'Row Number'})  
            print(df1)
            st.dataframe(df1)


def main():
    st.markdown(  
    f'<div style="text-align: center;"><img src="{"https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"  }" width="{60}"></div>',  
    unsafe_allow_html=True  
                )  
    st.title("Demo-Azure OpenAI Embeddings")
    # image = Image.open('image_logo2.png')
    # st.image(image, caption = '')
    st.sidebar.title('Embedding Function Selection')
    chat_style = st.sidebar.radio(  
    'Choose an Embedding function below:',  
    ['Vectorize', 'Retrieve']  
        )  
    if chat_style == 'Vectorize':
        embedding_create()
    elif chat_style == 'Retrieve':
        embeddings_search()

if __name__ == '__main__':
    global_page_style()
    main()
