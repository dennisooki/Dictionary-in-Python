import time
import urllib.request, urllib.error
import json


def getWord():
    word = input("Enter word to Search: ")
    word=word.replace(' ','%20')
    resp = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    #return resp
    evalWord(resp)


def evalWord(url):
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('Word not found, Search another word \nHTTPError: {} '.format(e.code))
        time.sleep(1)
        searchagn=input("Search another word?(Y/N): ")

        while searchagn[0].lower() != 'y' and searchagn[0].lower()!='n':
            searchagn = input("Invalid input, type Y or N: ")
        if searchagn[0].lower()=='y':
            getWord()

    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}\nCheck your internet connection and try again'.format(e.reason))
    else:
        # 200
        response = urllib.request.urlopen(url)
        data_json = json.loads(response.read())
        defintion = data_json[0]['meanings'][0]['definitions'][0]['definition']

        print(defintion)
        time.sleep(1.5)

        searchagn = input("Search another word?(Y/N): ")
        while searchagn[0].lower() != 'y' and searchagn[0].lower() != 'n':
            searchagn = input("Invalid input, type Y or N: ")
        if searchagn[0].lower() == 'y':
            getWord()


getWord()