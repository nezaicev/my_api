import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL = 'https://api.github.com/repos/django/django/pulls'

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://login:pass@localhost/test'

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class PullRequest(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    id_pr = db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    title_rus = db.Column(db.String(255), nullable=True)

PullRequest.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/list/api/v1.0/django', methods=['GET'])
def get_pulls():
    r = requests.get(URL)
    result = r.json()
    pr = session.query(PullRequest).all()
    for idx,i in enumerate(result):
        if pr[idx].id_pr== i['id']:
            i['title_rus']=pr[idx].title_rus
    session.commit()
    return jsonify(result)


if __name__ == '__main__':
    app.run()
