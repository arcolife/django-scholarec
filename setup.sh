# install requirements
sudo pip install -r requirements.txt --use-mirrors
# go to src
cd scholarec_web/
# add permission: executable to server script
chmod +x manage.py
# start server on default port 8000
# to change port, specify port as argument
./manage.py runserver 
