import requests

TOKEN = '7624777170:AAG6fQsdSt_xeJ97wmM1CqspaVElSr3RP5s'
CHAT_ID = 5737293433  # число, без кавычек
MESSAGE = '/start'  # или любое сообщение, чтобы «разбудить» бота

def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print('Сообщение отправлено успешно!')
    else:
        print('Ошибка при отправке:', response.text)

if __name__ == '__main__':
    send_message(TOKEN, CHAT_ID, MESSAGE)

