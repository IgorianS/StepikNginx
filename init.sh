sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database web;"
sudo mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
sudo mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

cd ~/web/ask
sudo python3 manage.py makemigrations qa
sudo python3 manage.py migrate
