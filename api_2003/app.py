#app.py


import config
from models import User

# initialize flask app using connextion framework
app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    
