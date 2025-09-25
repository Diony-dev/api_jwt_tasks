from config import config
from __init__ import create_app

app=create_app(config['prod'])

if __name__=='__main__':
    app.run()