import requests
import datetime
from defs import *
from time import sleep
url = "https://api.telegram.org/bot912956226:AAHbSPPUbAkLmm2j38A2JSiiHgO_983J4NQ/"

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:

        if update_id == last_update(get_updates_json(url))['update_id']:  
            if check_commands(get_user_text(last_update(get_updates_json(url)))) == "666":
                send_mess(get_chat_id(last_update(get_updates_json(url))), invalid_command(),url)
            else:
                send_mess(get_chat_id(last_update(get_updates_json(url))), check_commands(get_user_text(last_update(get_updates_json(url)))),url)
            update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()
