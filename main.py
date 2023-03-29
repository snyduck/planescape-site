from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv('.env')

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:3306/{os.getenv('MYSQL_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class pla(db.Model):
    charID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.Integer)
    charName = db.Column(db.String)
    charBio = db.Column(db.String)
    charBlurb = db.Column(db.String)
    charFaction = db.Column(db.String)
    charImg = db.Column(db.String)
    deadbook = db.Column(db.String)
    epitaph = db.Column(db.String)
     
    
with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():

    return render_template('index.html')


@app.route("/character/<string:charName>")
def char_page(charName):
    charinfo = db.session.execute(db.select(pla).where(
    pla.charName.like(f'{charName}%')
)).scalar()
    print(charinfo)
    return render_template('character_template.html',charinfo=charinfo)


@app.route("/story")
def story():
    return render_template('story.html')


# 404 app handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')