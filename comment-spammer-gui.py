import json
import re
import pyautogui
import time
import requests
import random

def getRandomQuote(): #Method to generate random quotes using public APIs
    randChooser = random.randint(1,100)
    if(randChooser%5 == 0):
        url = "https://officeapi.dev/api/quotes/random"
        response = requests.get(url) #Random Office Quote
        quote = json.loads(response.text)
        return quote["data"]["content"] + " - " + quote["character"]["firstname"] + " " + quote["character"]["lastname"]
    elif(randChooser%5 == 1):
        url = "https://api.kanye.rest/"
        response = requests.get(url) #Random Kanye Quote
        quote = json.loads(response.text)
        return quote["quote"] + " - Kanye"
    elif(randChooser%5 == 2):
        url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
        response = requests.get(url) #Random Ron Swanson Quote
        return response.text[2:len(response.text)-2] + " - Ron Swanson"
    elif(randChooser%5 == 3):
       url = "https://api.breakingbadquotes.xyz/v1/quotes"
       response = requests.get(url) #Random BB Quote
       quote = json.loads(response.text[1:len(response.text)-1])
       return quote["quote"] + " - " + quote["author"]
    else:
        url = "http://api.quotable.io/random"
        response = requests.get(url) #Random Quotes
        quote = json.loads(response.text)
        return quote["content"] + " - " + quote["author"]

start = time.time()
time.sleep(06) #Gives you 10 seconds to click on the comment box
count = 0

for j in range(100):
    for i in range(20): #Will post 20 comments in one iteration
        pyautogui.typewrite(getRandomQuote())
        pyautogui.typewrite("\n") #To enter and post the comment
        count += 1
        i = i + 1
        time.sleep(random.randint(5,10)) #Add a random delay
    time.sleep(random.randint(60,120)) # A random cooldown between two batches
    j = j + 1

end = time.time()
print("Total comments ", count)
print("Time taken %d seconds", end-start)

