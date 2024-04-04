from flask import Flask, request, redirect, url_for
from flask.templating import render_template
import random

app = Flask(__name__)
# - - - - - - - - - - - - - - - -

@app.route('/')
def text():
  return "Zde nic není."





# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_calculator():
  height = ''
  weight = ''
  result = None
  if request.method == 'POST':
    height = request.form.get('height', '')
    weight = request.form.get('weight', '')
    if height and weight:
      bmi = float(weight) / (float(height)**2)
      result = round(bmi, 2)
  return render_template('bmi_form.html',
                         height=height,
                         weight=weight,
                         result=result)

# Představuje počet hlasů pro každou možnost
votes = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

@app.route('/anketa', methods = ['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        option = request.form['option']
        if option in votes:
            votes[option] += 1
    return render_template('anketa.html', votes=votes)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
