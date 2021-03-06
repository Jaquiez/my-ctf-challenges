from urllib import response
from flask import Flask, make_response, render_template, request
from bot import bot
from threading import Thread,active_count

admin_cookie = 'VEgxUzFTRDRTVVAzUlMzQ1IzVDRETTFOQzAwS0kzTDBMIQ'

app = Flask(__name__)


def check_for_cookie():
    if(request.cookies.get("admin")):
        return True
    return False

def add_resp_headers(response):
    response.headers['Content-Security-Policy']= "default-src 'self';script-src 'self' 'unsafe-eval'"

@app.route("/",methods=['GET'])
def get_main():
    response = make_response(render_template('index.html'))
    add_resp_headers(response)
    if(check_for_cookie()==False):
        response.set_cookie("auth","-1",secure=True,samesite=None)
    return response

@app.route("/register",methods = ['GET','POST'])
def get_register():
    if(request.method=='GET'):
        response = make_response(render_template('register.html'))
        add_resp_headers(response);
        if(check_for_cookie()==False):
            response.set_cookie("auth","-1",secure=True,samesite=None)
        return response
    elif(request.method=='POST'): 
        if(active_count()<6):
            data = request.form.to_dict()
            thread = Thread(target=bot.checkEssay,kwargs={'data':data})
            thread.start()
            return "We got your request and will read it shortly!",200
        else:
            return "We are recieving a lot of traffic, please try again in a bit. (Not part of the challenge btw)",200

@app.route("/review/essay",methods = ['GET','POST'])
def reviewEssay():
    essay = {"email":request.args.get("name"),"essay":request.args.get("essay")}
    response = make_response(render_template('essay_checker.html',essay=essay))
    add_resp_headers(response)
    if(request.remote_addr != '127.0.0.1'):
        return "Sorry pal you\'re not admin"
    try:
        return response
    except:
        return 'no essays to read',200

@app.route("/join",methods = ['GET'])
def get_play():
    if(request.cookies.get("auth")==admin_cookie):
        return "UMASS{NUMB3R_0N3_1N_$TUD3NT_D1N1NG_XD86543267!}",200
    return "You're not allowed here!",403