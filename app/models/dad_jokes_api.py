# https://icanhazdadjoke.com/api

import requests
import random

# INPUT: A search term
# OUPTUT: A dad joke containing the search term.
# This is a function that takes in a search term and outputs a dad joke that 
# contains the search term.
def getDadJoke(search):
    # Get a list of dad jokes containing the input
    r = requests.get('https://icanhazdadjoke.com/search?term='+search, headers={"Accept":"application/json"})
    jokes = r.json()
    # IF jokes with the INPUT exist, pick a random joke from the list to
    # return as OUTPUT
    if jokes['total_jokes'] != 0:
        rando=random.randint(0,jokes['total_jokes']-1)
        joke_list=jokes["results"]
        return joke_list[rando]['joke']
    # ELSE no jokes were found with the given INPUT send a message back.
    else:
        return "No jokes found with that keyword."
        

