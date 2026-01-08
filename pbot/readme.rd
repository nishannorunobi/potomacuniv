UI technology - streamlit
Initial scripts on my machine.
-------------------------------------
sudo apt update
sudo apt install python3-venv
python3 -m venv .venv
# create .gitignore file
added .venv under gitignore

source .venv/bin/activate


pip install streamlit
pip install streamlit requests

pip freeze > requirements.txt


git push

streamlit run ui.py
deactivate

#########################
Core services technology - Fast API
Initial scripts on my machine.
-------------------------------------
pip install fastapi uvicorn pydantic

python backend.py
deactivate


################################
LLM model used 




