# potomacuniv
sudo apt update

sudo apt install python3-venv

python3 -m venv myenv

source myenv/bin/activate



# for project specific
pip install scalene
pip freeze > requirements.txt

scalene --profile-memory comp712_dis_1.3.py
