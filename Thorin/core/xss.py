import re 
import requests
import random
from core import regex
from core import nano
from core import bot
    
def xss_(link):
   
    if nano.reflection(link) == True:
        for rg,p in regex.XSS.items():
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent } 
            url=nano.inject_param(link,p)
            try:
                r = requests.get(url ,headers=headers ,verify=False )       
                resp = r.content
                ContentType=r.headers.get('Content-Type')
                x = re.findall(rg, str(resp))
                if (x):
                    if 'text/html' in str(ContentType):
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                        msg="Possibly XSS vulnerability "+url
                        bot.telegram_bot_sendtext(msg)
                        break
                    else:
                        print('\033[33;1mWarning can be false positives \033[00m')
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                        msg="Possibly XSS vulnerability "+url
                        bot.telegram_bot_sendtext(msg)
                        break
                else:
                    pay={'X=GtR"Nv>Yt':'&X=GtR%22Nv>Yt','X=Gt"RNbv>DR':'&X%3DGt%22RNbv%DR','XGt"RNbv>DR':'&XGt%22RNbv%DR'}
                    for rg,p in pay.items():
                        user_agent=random.choice(regex.USR_AGENTS)
                        headers = {'User-Agent': user_agent }
                        url=nano.inject(link,p)
                        try:
                            r = requests.get(url ,headers=headers ,verify=False )
                            resp = r.content 
                            ContentType=r.headers.get('Content-Type')   
                            x = re.findall(rg, str(resp))
                            if (x):
                                if 'text/html' in str(ContentType):
                                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                    msg="Possibly XSS vulnerability "+url
                                    bot.telegram_bot_sendtext(msg)
                                    break
                                else:
                                    print('\033[33;1mWarning can be false positives \033[00m')
                                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                    msg="Possibly XSS vulnerability "+url
                                    bot.telegram_bot_sendtext(msg)
                                    break
                            else:
                                r = requests.post(url ,headers=headers ,verify=False )
                                resp = r.content 
                                ContentType=r.headers.get('Content-Type')   
                                x = re.findall(rg, str(resp))
                                if (x):
                                    if 'text/html' in str(ContentType):
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                        msg="Possibly XSS vulnerability "+url
                                        bot.telegram_bot_sendtext(msg)
                                        break
                                    else:
                                        print('\033[33;1mWarning can be false positives \033[00m')
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                        msg="Possibly XSS vulnerability "+url
                                        bot.telegram_bot_sendtext(msg)
                                
                        except:
                            pass     
            except:
                pass


