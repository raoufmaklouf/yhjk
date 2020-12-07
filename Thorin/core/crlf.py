import requests
import threading
import queue
from core import nano
from core import regex
from core import bot




threads =10
def build_wordlist():
  
    words= queue.Queue()

    for word in regex.payload_crlf:
        word = word.rstrip()
        words.put(word)
        
    return words


word_queue = build_wordlist()

def run_(word_queue,url):
    if url != None :
        while not word_queue.empty():
            attempt = word_queue.get()
            attempt_list = []
            attempt_list.append(attempt)
        
            for brute in attempt_list:
                try:
                    session = requests.Session()
                    url=nano.inject_param(url,brute)
                    session.get(url)
                    if 'crlf' in session.cookies.get_dict() and 'injection' in session.cookies.get_dict().values():
                        msg="Possibly CRLF injection vulnerability "+url
                        print('\033[91m Possibly CRLF injection vulnerability\033[00m  '+url)
                        bot.telegram_bot_sendtext(msg)
                        break
                    else :
                        pass
                except :
                    pass
    else:
        pass

def crlf_(url):
    for i in range(threads):
        t = threading.Thread(target=run_,args=(word_queue,url))
        t.start()
        




