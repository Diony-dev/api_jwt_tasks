from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')
    MONGO_URI=config('MONGO_URI')
   
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    
    
class ProduccionConfig(Config):
    DEBUG=False
    
    
config={
    'dev':DevelopmentConfig,
    'prod':ProduccionConfig
}