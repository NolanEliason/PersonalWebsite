from flask import Flask  # imports flask class from flask library

app=Flask(__name__)

@app.route('/') # home page
def home(): 
    return "Homepage here!"

@app.route('/about/') # home page
def about(): 
    return "About Page!"

if __name__ == "__main__":  # when executing, name is set equal to main
    app.run(debug=True)