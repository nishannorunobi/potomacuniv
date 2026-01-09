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

After updating requirements.txt manually
#########################################
deactivate
rm -rf .venv
python3 -m venv .venv
pip install -r requirements.txt 


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



Docker
#####################
sudo docker images
docker image prune -a

sudo docker compose build --no-cache
sudo docker images

sudo docker compose up --force-recreate
sudo docker ps
sudo docker compose down
