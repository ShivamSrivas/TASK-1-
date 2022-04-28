from flask import Flask,render_template,request
from Database import MongoDb
"""
importing Libraries 
"""
Data=MongoDb.Mongo()#Creating Objects of a class

app=Flask(__name__)#Creating Objects of Flask

@app.route("/",methods=["GET"])
def main():
    """
    This is a main route which will lead you to the landing page
    """
    return render_template("index.html")


@app.route("/input",methods=["GET"])
def Input():
    """
    This is a route which is responsible for fetching the data from form
    """
    if (request.method=="GET"):
        name = str(request.form["name"])
        email = str(request.form["email"])
        number = str(request.form["number"])
        password = str(request.form["password"])
        Data.insert({"Data":[name,email,number,password]})#This is responsible for the insertion of the data
    return "Thank You"

if __name__=="__main__":
    app.run(debug=True,port=4997)