from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") #make sure to save  a folder with name templaets
# UI: How many inputs you have (You will be taking from user), dropdown , text
# Be ready model.pkl
# 3 steps: 1. Take input from USer
#          2. Pass that input to the model
#          3. Take the result received from model and display it

if __name__ == "__main__":
    app.run(debug=True)
