from bs4 import BeautifulSoup
import requests
import random

main_url="http://quotes.toscrape.com/"
response=requests.get(main_url)
next_page_url="/page/1"
quotes_plain_text_list=[]

#building the quotes list 
while next_page_url:
    response=requests.get(main_url+next_page_url)
    soup=BeautifulSoup(response.text,"html.parser")
    quotes_with_html=soup.find_all(class_="quote")#list of all the quotes
    #getting the information for every quote
    for quote in quotes_with_html:
        #getting the complete quote
        quote_text=quote.find(class_="text").get_text()
        #seperatting the values of the quote
        author=quote.find(class_="author").get_text()
        initials=author.split(" ")
        initials=initials[0][0]+" "+initials[1][0]
        about_href=quote.find("a")["href"]
        about_response=BeautifulSoup(requests.get(main_url+about_href).text,"html.parser")
        born_date=about_response.find(class_="author-born-date").get_text()
        born_location=about_response.find(class_="author-born-location").get_text()
        born_details=" ".join([born_date,born_location]) 
        #appending a dictionary to the list of quotes
        quotes_plain_text_list.append(
            {"quote":quote_text,"author":author,"initials":initials,"born_details":born_details})
    next_page_btn=soup.find(class_="next")
    next_page_url=next_page_btn.find("a")["href"] if next_page_btn else None


print("LETS START THE GUESSING GAME")
continue_playing="y"
guess_counter=4
while continue_playing=="y":
    rnd_quote=random.choice(quotes_plain_text_list)
    print("i have a quote for you:\n{}".format(rnd_quote["quote"]))
    while guess_counter>0:
        guess=input("who said this? guesses remaining:{} ".format(guess_counter))
        if guess==rnd_quote["author"]:
            print("well done")
            break
        else:
            guess_counter-=1
            if guess_counter==3:
                print("you got it wrong,here's a hint to help you:\nthe author initials are {}".format(rnd_quote["initials"]))
            elif guess_counter==2:
                print("you are wrong again, here's another hint to help you:\nthe author was born in {}".format(rnd_quote["born_details"]))
            elif guess_counter==1:
                print("please try harder")
            else :
                print("ahhhhh you lose")
    guess_counter=4
    continue_playing=input("do you want to keep playing?(y/n)")      

    
