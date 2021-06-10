from requests_html import HTMLSession
import smtplib
import threading


session = HTMLSession()
priorV = open("bojack.txt", "r")
v = priorV.read()

#email instance info

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<sender email>', '<password>')
server.sendmail( 'rondell', '<client email>', 'message' )


#getting version number from website

def get_site_version():
    try:
        r = session.get('https://eloquent-curie-58f1a3.netlify.app')
        resRoot = r.html.find('#vNum', first=True)
        innerRoot = resRoot.html

        return innerRoot

    except:
        print('did not work')
        print(r.status_code)

#grabbing the file that holds the current version

def find_version():
    print('hello')
    if priorV != get_site_version():
        with open("bojack.txt", "w") as f:
            f.write(get_site_version())

#calling both function

def main_func():
    get_site_version()
    find_version()

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(main_func, 5)

