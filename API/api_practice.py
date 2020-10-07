#so far the code is able to print data for any movie title + year requested


import requests, json

my_key = 'f7d58ebc'

def movie_search(query, year):
    api_key = my_key
    url = 'http://www.omdbapi.com/'
    title = query.replace(' ', '+')
    final_url = url + '?t=' + title + '&y=' + year + '&apikey=' + api_key
    req = requests.get(final_url)

    apiDict = json.loads(req.text)
    
    for key, value in apiDict.items():
        print(key + ":", value)

movie_search('Titanic', '1997')
