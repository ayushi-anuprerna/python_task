from flask import Flask,render_template,request 
import  requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/",
methods=["GET","POST"])
def index():
    title = ""
    anchorslist=[] 
    headings=[]
    if request.method == "POST":
        url=request.form["url"]
        response = requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        title=soup.title.string
        anchorsList=soup.find_all('a')
        headings=soup.find_all('h3')
    return render_template("index.html",anchor=anchorslist,heading=headings, title=title)
if __name__=="__main__":
    app.run(debug=True)






































































# from pyscript import document
# import requests
# from bs4 import BeautifulSoup

# def clickme(event):
#     storeurl=document.getElementById("url").value
#     mainPage=requests.get(storeurl)
#     parsed=BeautifulSoup(mainPage.text,"html.parser")
#     print(parsed.title)
#     anchorsList=parsed.find_all('a')
#     for anchor in anchorsList:
#      print(anchor.string)
# #print(parsed.find_all('a'))
#     print(parsed.find('h1'))
#     print(parsed.find('img')["src"])
#     print(parsed.find('img').get("src"))
    
    
