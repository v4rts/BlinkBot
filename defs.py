import requests
import datetime

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def invalid_command():
    return "Такой команды не существует, /help для просмотра доступных команд"

def check_commands(text):
    if text == "/help":
        return "Доступные команды бота: /date /image"
    elif text == "/date":
        return "Здесь пока ничего нет, но скоро точно будет, скоро, скоро, нет не будет"
    elif text == "/image":
        return "Здесь пока ничего нет, но скоро точно будет"
    else:
        return "666"

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def get_user_text(update):
    userText = update['message']['text']
    return userText

def send_mess(chat, text, url):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response