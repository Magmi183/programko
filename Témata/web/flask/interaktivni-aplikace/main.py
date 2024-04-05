from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


# - - - - - - - - - - - - - - - -

@app.route('/')
def text():
    return "Zde nic není."


@app.route('/priklad', methods=['GET', 'POST'])
def priklad():
    # Pokud je požadavek typu POST, znamená to, že uživatel poslal své odpovědi
    if request.method == 'POST':
        # Získáme data z formuláře
        hra = request.form.get('name')

        # Ukážeme data (nebo cokoliv jiného, můžeme to dále zpracovat atd.)
        return f"<h1>Ahoj {hra}e!</h1>"

    # Jinak, pokud ještě neodeslal formulář, ukážeme mu prázdný formulář, aby mohl odpovědět
    return '''<form method="POST">
                <label for="name">Jméno:</label>
                <input type="text" id="name" name="name">
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
            bmi = float(weight) / (float(height) ** 2)
            result = round(bmi, 2)
    return render_template('bmi_form.html',
                           height=height,
                           weight=weight,
                           result=result)


# Představuje počet hlasů pro každou možnost
votes = {'A': 0, 'B': 0, 'C': 0, 'D': 0}


@app.route('/anketa', methods=['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        option = request.form['option']
        if option in votes:
            votes[option] += 1
    return render_template('anketa.html', votes=votes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
