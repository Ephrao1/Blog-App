import os
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SECRET_KEY = os.environ.get('SECRET_KEY') 
   SQLALCHEMY_TRACK_MODIFICATIONS = False

#    email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ephraim:12345678@localhost/blog'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ephraim:12345678@localhost/pitch_test'
        


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}  
