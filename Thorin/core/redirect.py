from core import nano
from core import regex 
import threading
import queue
import requests
import re
import random
from core import bot

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

threads =10

def build_wordlist():
  
    words= queue.Queue()

    for word in regex.payloads_OR_p:
        word = word.rstrip()
        words.put(word)
        
    return words

def run(word_queue,url):
    url=str(url)
    for x in regex.parameters_OR:
            param=(x+"=")
            if url != None and  param in url:
                try:
                    base_link=url.split(param)[0]
                except:
                    pass
                f_link=base_link+param
                while not word_queue.empty():
                    attempt = word_queue.get()
                    attempt_list = []
                    attempt_list.append(attempt)
        
                    for brute in attempt_list:
                        user_agent=random.choice(regex.USR_AGENTS)
                        headers = {'User-Agent': user_agent } 
                        url = f_link+brute
                        
                       
                        try:         
                            r = requests.get(url, headers=headers,verify=False)
                            resp=r.content       
                            if  "Location" in r.headers and "google" in r.headers :
                                msg="Possibly open redirection vulnerability "+url
                                print('\033[91m Possibly open redirection vulnerability\033[00m\t'+url)
                                bot.telegram_bot_sendtext(msg)
                                break
                            else:
                                pass
                        except :
                            pass
           
word_queue = build_wordlist()
def redirect_(url):
    for i in range(threads):
        t = threading.Thread(target=run,args=(word_queue,url))
        t.start()
        


