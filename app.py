from flask import Flask,request,make_response
app=Flask(__name__)

@app.route('/')
def index():
    count= int(request.cookies.get('visit-cont',0))
    count+=1
    msg= "you have visited this page {c} times".format(c=count)

    response= make_response(msg)
    response.set_cookie('visit-cont', str(count))
    return response

app.config['DEBUG']=True
app.run()