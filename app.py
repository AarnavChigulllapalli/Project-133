# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aarnav" # write your name
    age = "13" # write your age
    relation="Me"
    return render_template('index.html' , name = name , age = age , relation=relation)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Anil" # write your name
    age = "51" # write your age
    relation= 'Father'
    return render_template('index.html' , name = name , age = age , relation=relation)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Sridevi" # write your name
    age = "50" # write your age
    relation="Mother"
    return render_template('index.html' , name = name , age = age , relation=relation)

# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Vrushabh" # write your name
    age = "14" # write your age
    relation='Friend'
    return render_template('index.html' , name = name , age = age, relation=relation)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
