from requests_html import HTMLSession

session = HTMLSession()
priorV = open("bojack.txt", "r")
v = priorV.read()
print(v)




def getSiteVersion():
    try:
        r = session.get('https://eloquent-curie-58f1a3.netlify.app')
        resRoot = r.html.find('#vNum', first=True)
        innerRoot = resRoot.html

        return innerRoot

    except:
        print('did not work')
        print(r.status_code)

getSiteVersion()


def findVersion():
    if priorV != getSiteVersion():
        with open("bojack.txt", "w") as f:
            f.write(getSiteVersion())

    

findVersion()

#TODO fix flow of save and compare
