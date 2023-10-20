from configparser import ConfigParser
import os

config = ConfigParser()
config.read(f'/home/{os.environ.get("USER")}/.config.ini')

credentials_auth = {
    'username' : config.get('CREDENTIALS', 'CREDENTIALS_USERNAME'),
    'password' : config.get('CREDENTIALS', 'CREDENTIALS_PASSWORD'),
    }

smtp_auth = {
    'server' : config.get('SMTP', 'SMTP_SERVER'),
    'port' : config.get('SMTP', 'SMTP_PORT'),
    'email' : config.get('SMTP', 'SMTP_EMAIL'),
    'password' : config.get('SMTP', 'SMTP_PASSWORD'),
    }

mysql_db_auth = {
    'user' : config.get('MYSQL', 'MYSQL_DB_USERNAME'),
    'password' : config.get('MYSQL', 'MYSQL_DB_PASSWORD'),
    'host' : config.get('NETWORK', 'IP_ADDRESS'),
    'port' : '3306',
    'database' : 'contacts',
    }

network_auth = {
    'ip_address' : config.get('NETWORK', 'IP_ADDRESS')
    }
