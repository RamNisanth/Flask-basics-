from flask import Flask,render_template
app=Flask(__name__)

posts=[
    {
       'author':'corey schafer',
       'title':'Blag post 1',
       'content':'First post content',
       'date_posted':'April 22 2018'
    },
    {
       'author': 'Ram Nisanth',
       'title':'Blog post 2',
       'content':'Second ostr content',
       'date_posted':'April 23 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return  render_template('home.html',posts=posts)

@app.route('/about')
def about():    
    return render_template('about.html',title='About')

