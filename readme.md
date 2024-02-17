* select python version by pyevn 
pyevn local 3.10

* create virsual env.
python -m venv venv 

* activate env. 
source venv/bin/activate 

* Need to install lib
pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai
pip install tiktoken
pip install InstructorEmbedding sentence_transformers

* create the config files
touch .gitignore
touch .env

* add ignore file to gitignore 
.env
/venv

* Add git 
git init 


sentence-transformers==2.3.1

https://www.youtube.com/watch?v=dXxQ0LR-3Hg
