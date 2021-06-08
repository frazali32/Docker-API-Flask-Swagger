from app import app
from flask import render_template
from flask import request
from flask_swagger_ui import get_swaggerui_blueprint

@app.route('/')
def home():
   return "hello no world!"

@app.route('/template',methods=['POST','GET'])
def template():
    output = request.args.values()
    return render_template('home.html',prediction_text="Hello {}?".format(list(output)[:]))
    

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Hello User"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

@app.route('/predict')
def predict():
    return render_template('index.html')


