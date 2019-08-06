import os

# grab the folder of the top-level directory of this project
basedir = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nifdl>jfdf@md!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')or 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Uploads
    UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/app/static/img/products'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/products'
 
    UPLOADED_PHOTOS_DEST = TOP_LEVEL_DIR + '/app/static/img/products'
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/products'

    # ALLOWED_HOSTS = 'mytieclub.herokuapp.com'

    # Mail -  not working
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    #MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('mytieclub@gmail.com')
    MAIL_PASSWORD = os.environ.get('!SomeArbitraryPassword123')


    



