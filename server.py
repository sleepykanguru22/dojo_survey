
from flask import Flask, render_template
app = Flask (__name__)



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")
    
@app.route('/result')
def results():
    return render_template("index.html")

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  