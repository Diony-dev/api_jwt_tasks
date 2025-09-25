from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')
    MONGO_URI=config('MONGO_URI')
   
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    
    
config={
    'dev':DevelopmentConfig
}