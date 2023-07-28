from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitted')
def submitted():
   return render_template('submitted.html')

if __name__ == '__main__':
  app.run(debug=True)
