from flask import Flask

app=Flask(__name__)

@app.route('/') # home page
def home(): 
    return "Wensite content goes here!"

if __name__ == "__main__":
    app.run(debug=True)