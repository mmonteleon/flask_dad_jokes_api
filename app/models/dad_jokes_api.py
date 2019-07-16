# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236
# https://icanhazdadjoke.com/api
# i can have a dad joke
import requests
import random
        
def getDadJoke(search):
    r = requests.get('https://icanhazdadjoke.com/search?term='+search, headers={"Accept":"application/json"})
    jokes = r.json()
    if jokes['total_jokes'] != 0:
        rando=random.randint(0,jokes['total_jokes']-1)
        joke_list=jokes["results"]
        return joke_list[rando]['joke']
    else:
        return "No jokes found with that keyword."