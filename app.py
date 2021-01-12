import requests
from flask import Flask,render_template
from bs4 import BeautifulSoup as bs
app= Flask(__name__)

@app.route("/<query>")
def id(query):
    
    a = "https://telegram.dog/"+query
    
    res= requests.get(a).content
    
    soup = bs(res,'html')
    dp = soup.find("img",class_="tgme_page_photo_image")['src']
    
    channel_name = soup.find("div", class_="tgme_page_title").text.replace("\n","")
    
    User = soup.find("div", class_="tgme_page_extra").text

    return render_template("main.html",dp=dp,channel_name=channel_name,User=User,des=description)
    
if __name__ == "__main__":
    app.run()