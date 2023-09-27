from flask import Flask , render_template
import datetime
app = Flask(__name__)
User = ["Tanmay"]
secUser = ["Sita" ,"Gita" ,"Chalita" ,"Lata"]
@app.route('/')
def index():
  N = User
  sn = secUser
  return render_template("index.html" , N=N, sN=sn)
@app.route('/base')
def base():
  return render_template("base.html")

@app.route('/time')
def timewe():
  curr_clock = datetime.datetime.now()
  N = User
  return render_template("time.html" , N=N , T=curr_clock)

app.run(host='0.0.0.0', port=81)
