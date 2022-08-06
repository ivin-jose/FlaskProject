from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField,IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
#import MySQLdb
import datetime
# Create a Flask Interface
app = Flask(__name__)

# add databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sanyosamsung22mysqldatabasecom@localhost/login_datas'
# secrete key
app.config['SECRET_KEY'] = "something fishy"
# initialising databse
db = SQLAlchemy(app)




# create a route decorator
@app.route('/')
def index():
    list=['mustang','shelby','gtr']
    return render_template('index.html',list=list)

# passing a name with the route
@app.route('/user/<name>')
def user(name):
    name='ivin'
    return render_template('user.html',name=name)

# invalid url error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

# setting database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "sanyosamsung22mysqldatabasecom",
    database = "login_datas",
    )
cursor = mydb.cursor()
# creating class for login page
class loginForm(FlaskForm):
    name = StringField('Enter name')
    password = PasswordField('Enter passwd')
    hobby = StringField('Enter hobby ')
    age = IntegerField('Enter age .')
    submit = SubmitField('Login')



# login page
@app.route('/login',methods=['GET','POST'])
def login():
    name = ''
    password = ''
    hobby = ''
    age = ''
    l = 'love'
    form = loginForm()
    if request.method == "POST":
        name = form.name.data
        password = form.password.data
        hobby = form.hobby.data
        age = form.age.data
        form.name.data = ''
        form.hobby.data = ''
        cursor.execute("INSERT INTO login_datas.user_info(name,password,hobby,age) VALUES(%s,%s,%s,%s)",(name,password,hobby,age))
        mydb.commit()

    return render_template('login.html',form=form,name=name,hobby=hobby,age=age,password=password,l=l)

@app.route('/login datas',methods=['GET','POST'])
def login_datas():
    cursor.execute("select * from user_info")
    data = cursor.fetchall()

    return render_template('login_data.html',data=data)

# update form
class updateform(FlaskForm):
    id = IntegerField('ID ')
    name = StringField('Name ')
    password = PasswordField('password')
    hobby = StringField('hobby')
    age = IntegerField('age')
    submit = SubmitField('Update')


@app.route('/update', methods=['GET', 'POST'])
def update():
    form = updateform()
    name = ''
    age = ''
    password = ''
    hobby = ''
    id=''
    try:
        if request.method == 'POST':
            id = form.id.data
            name = form.name.data
            password = form.password.data
            hobby = form.hobby.data
            age = form.age.data
            updation= ("UPDATE user_info SET name=%s,password=%s, hobby=%s, age=%s WHERE(id=3)")
            values = (name,password,hobby,age)
            cursor.execute(updation,values)
            mydb.commit()
        return render_template('update.html',form=form,name=name,age=age,password=password,hobby=hobby,id=id)
    except:
        return render_template("404.html")


# deleting class
''' Deleting the user details from database '''

class logoutform(FlaskForm):
    id = IntegerField('ID ')
    name = StringField('Name ')
    password = PasswordField('password')
    submit = SubmitField('Log out')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    form = logoutform('/logout')
    id = " "
    name = " "
    password = " "
    if request.method == "POST":
        id = form.id.data
        name = form.name.data
        password = form.password.data
        form.id.data=""
        form.name.data=""
        sid = 10
        delete = """DELETE from user_info WHERE id=%s"""
        cursor.execute(delete,(id, ))
        mydb.commit()



    return render_template('logout.html',form=form,id=id,name=name,password=password)