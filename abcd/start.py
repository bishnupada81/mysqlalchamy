from flask import Flask, render_template , url_for, request , flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/abcd'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)


 
# class Results(user):
#     id = Col('Id', show=False)
#     name = Col('name')
#     email = Col('email')
#     phone = Col('phone')
#     adderss = Col('address')


@app.route('/', methods = ['GET' , 'POST'])
def index():
    if(request.method == 'POST'):
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")

        entry = User(name = name , email = email , phone = phone , address = address)
        db.session.add(entry)
        # db.session.commit()
        flash('You were successfully submit')
    return render_template("index.html")



@app.route('/show')
def show():
    user=User.query.all()
    return render_template("show.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)


