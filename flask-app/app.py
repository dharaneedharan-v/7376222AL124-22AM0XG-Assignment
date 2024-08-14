from flask import Flask


# Create an instance of the Flask class
app = Flask(__name__)


# Define a route for the root URL ('/')
@app.route('/')
def home():
    return "Hello, Flask!"
@app.route('/details')
def dd ():
   
    return"  DHARANEE DHARAN V - 7376222AL124"


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True,port=5001)  