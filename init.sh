git clone https://github.com/IgorianS/StepikNginx.git /home/box/web

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

cd ~/web/ask
python3 manage.py makemigrations qa
python3 manage.py migrate
