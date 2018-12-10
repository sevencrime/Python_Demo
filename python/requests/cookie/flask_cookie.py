#coding:utf-8
from flask import session,Flask,redirect,make_response,request,render_template
app=Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route("/")
def index():
   try:
     t=request.cookies.get("your_name")  #读取cookie
     print (t)
     if t != None and t==session["your_name"]: #读取session
       return "you have logged in"
     else:
       return redirect("/login")
   except KeyError as e:
       return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
   if request.method=="GET":
        return render_template("login.html")
   elif request.method=="POST":
        n=request.form.get("name")
        print ("11111111111111111111111",n)
        session["your_name"]=n   #设置session
        response=make_response("logged in !")
        response.set_cookie("your_name",n) #设置cookie
        return response

@app.route("/logout")
def logout():
    session.pop("your_name",None) #删除session
    return "you have logged out!"


if __name__=="__main__":
    app.run(debug=True)