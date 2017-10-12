from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:BlogStuffs@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog = db.Column(db.Text(65000))

    def __init__(self,title,blog):
        self.title=title
        self.blog=blog






@app.route('/blog', methods=['POST', 'GET'])
def showblogs():
    blog_id=request.args.get('blog_id')
    if blog_id != None:
        blog_id=int(blog_id)
    blogs=Blog.query.all()
    return render_template('blog.html',blogs=blogs,blog_id=blog_id)



@app.route('/newpost', methods=['POST', 'GET'])
def addpost():
    title = 'Entry Title'
    entry = 'Share your thoughts'
    
    if request.method == 'POST':
        title = request.form['title']
        entry = request.form['blogentry']
        error = 0
        if title == 'Entry Title':
            flash("Please Title Your Thoughts", 'error')
            error = 1
        if entry == 'Share your thoughts':
            flash("Please Enter Your Thoughts", 'error')
            error = 1
        if error == 1:
            return render_template('post.html',title=title,entry=entry)
        blog = Blog(title,entry)
        db.session.add(blog)
        db.session.commit()
        blog_id=Blog.query.order_by(Blog.blog_id.desc()).first().blog_id
        return redirect('/blog?blog_id={0}'.format(blog_id))


    return render_template('post.html',title=title,entry=entry)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return redirect('blog')




app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == "__main__":
    app.run()