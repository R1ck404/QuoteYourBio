#from threading import Timer
import requests, datetime, os

def saveKey(key):
    with open('api_data.txt', 'w') as f:
        f.write(key)
        f.close()
    
def getKey():
    if os.path.isfile("api_data.txt"):
        with open("api_data.txt", "r") as f:
            text = f.read()
            f.close()
            return text
    else:
        return ""

def updateBio(bio):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + api_key,
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = str('{"bio": "' + bio + '"}').encode('utf-8')

    response = requests.patch('https://api.github.com/user', headers=headers, data=data)
    return response == 200

def fetchQuote():
    request = requests.get('https://programming-quotesapi.vercel.app/api/random')
    return request.json()

def styleQuote(quoteR):
    author = quoteR['author']
    quote = quoteR['quote']

    return '`' + quote + '` - ' + author

input = input('Please enter your Github API key. (Leave empty if you want to use cached key)\n')
api_key = ''

if input == "":
    key = getKey()
    print(key)

    if key != "":
        api_key = key
    else:
        print("No api key cached.")
        exit()
else:
    api_key = input
    saveKey(input)


quote = styleQuote(fetchQuote())
updateBio(quote)
print('New quote fetched: ' + quote)

# nextDay = datetime.datetime.now() + datetime.timedelta(days=1)
# dateString = nextDay.strftime('%d-%m-%Y') + " 01-00-00"
# newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
# delay = (newDate - datetime.datetime.now()).total_seconds()

# Timer(delay, updateBio(styleQuote(fetchQuote()))).start()