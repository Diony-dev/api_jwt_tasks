from decouple import config
import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MONGO_URI=os.environ.get('MONGO_URI')


class DevelopmentConfig(Config):
    DEBUG=True
    
    
class ProduccionConfig(Config):
    DEBUG=False
    
    
config={
    'dev':DevelopmentConfig,
    'prod':ProduccionConfig
}