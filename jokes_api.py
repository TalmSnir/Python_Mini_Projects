import requests
import pyfiglet 
import random as rnd
import colorama
import termcolor

url="https://www.icanhazdadjoke.com/search"
print(pyfiglet.figlet_format("dad jokes 3000"))
topic=input("let me tell you a joke, give me a topic: ")

response=requests.get(url,
    headers={"Accept":"application/json"}
    ,params={"term":topic})

data=response.json()['results']
jokes_count=len(data)

if jokes_count==0:
    print (f"sorry ive got no jokes about {topic}")
elif jokes_count==1:
    joke= data[0]['joke']
    print (f"ive got one joke about {topic}. here it is:\n {joke}") 
else:
    joke=rnd.choice(data)['joke']
    print(f"i've got {jokes_count} jokes for you about {topic}. here is one:\n {joke}")







