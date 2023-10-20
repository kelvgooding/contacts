from configparser import ConfigParser
import os

config = ConfigParser()
config.read(f'/home/{os.environ.get("USER")}/.config.ini')

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
