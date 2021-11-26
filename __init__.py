

from flask import Flask

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'Cyborg'

# --------------- DATABASE

app.config['SECRET_KEY'] = 'mykeyasdfghjklsdfghnjm'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cloud_dev:ep66w?WR$GfWesv4@http://mysql-58440-0.cloudclusters.net:10669/development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
