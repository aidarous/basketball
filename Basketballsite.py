from flask import Flask, render_template , request, escape
from Basketball_quiz import *

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def home():
    
    return render_template('bballquiz.html',name='ball is life', score= score)

if __name__=="__main__":
    app.run(debug=True)


