import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores  import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI  
from htmlTemplates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator=" ",
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts= text_chunks, embedding = embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key= 'chat_history', return_messages= True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(), 
        memory= memory)
    return conversation_chain

def handle_userinput(user_question):
     if 'coverstation' in st.session_state and callable(st.session_state.coverstation):
        response = st.session_state.coverstation({"question": user_question})
        # st.write(response)
        st.session_state.chat_history = response['chat_history']
        
        for i, message in enumerate(st.session_state.chat_history[::-1]):
            if i % 2 == 0:
                st.write(bot_template.replace("{{MSG}}", message.content ), unsafe_allow_html=True)
            else:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def submit():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""



def main():
    load_dotenv()

    st.set_page_config(page_title="AbdulPDFs", page_icon=":robot_face:", layout="centered",initial_sidebar_state="expanded")
    st.write(css, unsafe_allow_html=True)
    st.image('https://raw.githubusercontent.com/toche7/DataSets/main/abdullogo.jpg', width=100)
    # st.image('pics/abdul.png', width=100)

    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    if "coverstation" not in st.session_state:
        st.session_state.coverstation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    
    st.header("AbdulPDFs")
        # Check if the button was clicked
    if st.button('Reset Chat History'):
        st.session_state.chat_history = []
        if st.session_state.vector_store:
            st.session_state.coverstation = get_conversation_chain(st.session_state.vector_store)

    st.text_input("Enter question here", key="widget", on_change=submit)
    my_text = st.session_state.my_text
    # st.write(my_text)
    if my_text != "" :
        handle_userinput(my_text)
        st.session_state.my_text = ""

    
    with st.sidebar:
        st.subheader("Your PDFs")
        pdf_docs = st.file_uploader("Upload PDF for asking question", type="pdf", accept_multiple_files=True)
        
        if st.button("Process PDFs"):
            with st.spinner("Processing..."):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write("text chunks :", len(text_chunks))
                # if chunk length more than 20, then it is too long
                if len(text_chunks) > 10:
                    st.error("The Demo Verion is limited the length of PDF.\
                             The PDF is too long. Please upload a shorter PDF.")
                    st.stop()
                # creat embeddings
                # create vector store
                vector_store = get_vectorstore(text_chunks)
                st.session_state.vector_store = vector_store

                # create conversation chain
                st.session_state.coverstation = get_conversation_chain(vector_store)

  #      st.write("AbdulPDF is a chatbot that can help you find information in your PDFs.")
        st.write("Upload your PDFs and ask questions about the content.")
        st.write("Developed by CBTU, ver 1.0")

        

if __name__ == "__main__":
    main()

