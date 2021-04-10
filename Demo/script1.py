from flask import Flask, render_template # imports flask class from flask library
#render template acess html file and displays it

app=Flask(__name__)

@app.route('/') # home page
def home(): 
    return render_template("home.html")

@app.route('/about/') # home page
def about(): 
    return render_template("about.html")

if __name__ == "__main__":  # when executing, name is set equal to main
    app.run(debug=True)