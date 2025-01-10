from openai import AzureOpenAI  
import pandas as pd  
import numpy as np  
import os  
import streamlit as st  
import time  
from dotenv import load_dotenv  
from styling import global_page_style  
  
# Load environment variables from .env file  
load_dotenv()  
  
def get_embedding(text, engine):  
    """  
    Generate embeddings for a given text using Azure OpenAI.  
  
    This function utilizes the Azure OpenAI service to generate embeddings  
    for the provided text. It retrieves the necessary API key, version, and  
    endpoint from environment variables loaded using load_dotenv().  
  
    Environment Variables:  
        Azure_OPENAI_KEY: Your Azure OpenAI API key.  
        AZURE_OPENAI_VERSION: The version of the Azure OpenAI API you are using.  
        AZURE_OPENAI_ENDPOINT: The endpoint for your Azure OpenAI instance.  
  
    Args:  
        text (str): The text for which to generate embeddings.  
        engine (str): The deployment model to use for generating embeddings.  
  
    Returns:  
        list: A list representing the generated embeddings.  
    """  
    client = AzureOpenAI(  
        api_key=os.getenv("AZURE_OPENAI_KEY"),  # Your Azure OpenAI API key  
        api_version=os.getenv('AZURE_OPENAI_VERSION'),  # The version of the Azure OpenAI API you are using  
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')  # The endpoint for your Azure OpenAI instance  
    )  
    embeddings = client.embeddings.create(input=[text], model=engine).data[0].embedding  
    return embeddings  
  
def cosine_similarity(a, b):  
    """  
    Calculate the cosine similarity between two vectors.  
  
    Cosine similarity is a metric used to measure how similar two vectors are.  
    It is calculated as the dot product of the vectors divided by the product  
    of their magnitudes.  
  
    Args:  
        a (np.ndarray): The first vector.  
        b (np.ndarray): The second vector.  
  
    Returns:  
        float: The cosine similarity between the two vectors.  
    """  
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))  
  
def embedding_create():  
    """  
    Create embeddings from a specified CSV file and save them.  
  
    This function reads a CSV file specified by the user, generates embeddings  
    for the text data in the "text" column, and saves the embeddings to a new  
    CSV file. The user is prompted to provide the filename, and the embeddings  
    are created using the Azure OpenAI service.  
  
    The function utilizes Streamlit for the user interface:  
        - Displays the input CSV file in a Streamlit dataframe.  
        - Prompts the user to generate embeddings by clicking a button.  
        - Displays the updated dataframe with embeddings.  
        - Saves the embeddings to a new CSV file.  
    """  
    st.subheader("Vector Creation")  
    st.write('''The process of vectorization involves creating embeddings from the 
             [microsoft-earnings.csv](https://github.com/STRIDES/NIHCloudLabAzure/blob/main/notebooks/GenAI/microsoft-earnings.csv) file located in 
             the specified directory, utilizing the data in the "text" column. These embeddings are derived from pre-chunked text, 
             indicating that the text has already been divided and formatted for embedding generation. The resultant embeddings will be 
             compiled into a new CSV file, which will serve as a vector store for future reference and utilization.''')  
      
    # Prompt the user to enter the filename  
    filename = st.text_input("Enter a file: ", key='filename', value="microsoft-earnings.csv")  
      
    # If a filename is provided, proceed to generate embeddings  
    if filename:  
        file_path = os.path.join('..', filename)  
          
        # Read the CSV file into a DataFrame  
        df = pd.read_csv(file_path)  
          
        # Display the DataFrame in the Streamlit app  
        df_placeholder = st.empty()  
        df_placeholder.dataframe(df, width=2000, height=350)  
          
        button_placeholder = st.empty()  
          
        # When the "Generate Embeddings" button is clicked  
        if button_placeholder.button("Generate Embeddings"):  
            with st.spinner("Generating Embeddings. Please hold..."):
                # Calculate word embeddings for each text entry in the DataFrame  
                df['embedding'] = df['text'].apply(lambda x: get_embedding(x, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT")))  
                
                # Save the embeddings to a new CSV file  
                df.to_csv('./microsoft-earnings_embeddings.csv')  
                
                # Display success message after a short delay  
                time.sleep(3)  
                button_placeholder.success('Embeddings Created Successfully!!')  
              
            # Update the displayed DataFrame to include the new embeddings  
            df_placeholder.dataframe(df, width=2000, height=350)  
            print(df)
  
def embeddings_search():  
    """  
    Search for similar documents based on user query embeddings.  
  
    This function generates embeddings for a user-provided search query and  
    compares them with pre-generated embeddings from a CSV file. The most  
    similar documents are identified using cosine similarity, and the top  
    results are displayed to the user.  
  
    The function utilizes Streamlit for the user interface:  
        - Prompts the user to enter a search query.  
        - Generates embeddings for the search query.  
        - Calculates cosine similarity between query embeddings and document embeddings.  
        - Displays the search query, top match, and similarity score.  
        - Displays the top 5 most similar documents in a Streamlit dataframe.  
    """  
    st.subheader("Vector Search")  
    st.write('''This process generates embeddings based on user queries, utilizing the compiled CSV that was created, to search for the most similar 
             documents within the vector store by employing cosine similarity. Example questions a user can ask about the microsoft-earnings.csv: 
             - What was said about the budget? 
             - How many people utilize GitHub to build software? 
             - How many points did Microsoft Cloud gross margin percentage increase by? 
             - What are the expectations for the Q2 cash flow?''')  
      
    # Initialize session state variables if they don't exist  
    if 'answer' not in st.session_state:  
        st.session_state.answer = []  
    if 'score' not in st.session_state:  
        st.session_state.score = []  
    if 'past' not in st.session_state:  
        st.session_state.past = []  
      
    # Read the embeddings CSV and convert the 'embedding' column back to numpy arrays  
    df = pd.read_csv('./microsoft-earnings_embeddings.csv')  
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)  
      
    # Prompt the user to enter a search query  
    search_term = st.text_area("Enter a search query: ", key='search_term', placeholder="")  
      
    if search_term:  
        # Store the user's search query  
        st.session_state.past.append(search_term)  
          
        # Generate the embedding for the search query  
        search_term_vector = get_embedding(search_term, engine=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"))  
          
        # Calculate similarity between the query embedding and document embeddings  
        df['similarities'] = df['embedding'].apply(lambda x: cosine_similarity(x, search_term_vector))  
          
        # Get the top 5 most similar documents  
        df1 = df.sort_values("similarities", ascending=False).head(5)  
          
        # Extract the most similar document and its similarity score  
        answer = df1['text'].iloc[0]  
        score = df1['similarities'].iloc[0]  
          
        # Store the answer and score in session state  
        st.session_state.answer.append(answer)  
        st.session_state.score.append(score)  
          
        # Display the search history and results  
        with st.expander('Vector Search'):  
            for i in range(len(st.session_state.answer) - 1, -1, -1):  
                st.info(st.session_state.past[i])  
                st.write(st.session_state.answer[i])  
                st.write('Score: ', st.session_state.score[i])  
          
        # Display the top 5 search results in a DataFrame  
        with st.expander('Top 5 Results'):  
            df1 = df1.reset_index(drop=True)  
            df1.index = df1.index + 1  
            df1 = df1.rename(columns={'Unnamed: 0': 'Row Number'})  
            st.dataframe(df1)  
  
def main():  
    """  
    Set up the Streamlit app and handle user interactions.  
  
    This function sets up the main interface of the Streamlit app, including  
    the title, sidebar, and embedding function selection. Based on the user's  
    selection, it calls either the embedding_create() or embeddings_search() 
    function to perform the respective actions.  
  
    The function also displays the Microsoft logo at the top of the app.  
  
    The function utilizes Streamlit for the user interface:  
        - Provides a sidebar for the user to select the embedding function.  
        - Calls the appropriate function based on user selection.  
    """  
    st.markdown(  
        f'<div style="text-align: center;"><img src="{"https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"}" width="{60}"></div>',  
        unsafe_allow_html=True  
    )  
    st.title("Demo-Azure OpenAI Embeddings")  
      
    # Sidebar for selecting the embedding function  
    st.sidebar.title('Embedding Function Selection')  
    chat_style = st.sidebar.radio(  
        'Choose an Embedding function below:',  
        ['Vectorize', 'Retrieve']  
    )  
      
    # Call the appropriate function based on user selection  
    if chat_style == 'Vectorize':  
        embedding_create()  
    elif chat_style == 'Retrieve':  
        embeddings_search()  
  
# Entry point of the script  
if __name__ == '__main__':  
    global_page_style()  
    main()  