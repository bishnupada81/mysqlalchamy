from flask import Flask, render_template , url_for, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/abcd'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)


@app.route('/', methods = ['GET' , 'POST'])
def index():
    if(request.method == 'POST'):
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")

        entry = User(name = name , email = email , phone = phone , address = address)
        db.session.add(entry)
        db.session.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)