# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, url_for, request, redirect

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

def dyn():
   return f'Dynamically added route<br><a href={ url_for("hello_world") }>take me home</a>'
app.add_url_rule('/dynamic', 'dynamic_route', dyn)

# The route() function of the Flask class is a decorator
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    content = f'''<html>
      <body>     
      <form action = { url_for("login") } method = "post">
      <p>Enter Name:</p>
      <p><input type = "text" name = "nm" /></p>
      <p><input type = "submit" value = "submit" /></p>
      </form>     
      </body>
      </html>
'''

    return f'Hello (6) World<br><a href={ url_for("dynamic_route") }>click me</a><br>{content}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
    return f'welcome {name} <br><a href={ url_for("hello_world") }>take me home</a>'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()