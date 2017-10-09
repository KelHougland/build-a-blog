from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:BlogStuffs@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog = db.Column(db.Text(65000))

    def __init__(self,title,blog):
        self.title=title
        self.blog=blog



@app.route('/blog', methods=['POST'])
def showblogs():
    return print('fix this')



@app.route('/newpost', methods=['POST'])
def addpost():
    return print('fix this')








if __name__ == "__main__":
    app.run()