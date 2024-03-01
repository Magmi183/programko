from flask import Flask, request
from flask.templating import render_template
import random

app = Flask(__name__)
# - - - - - - - - - - - - - - - -

pocet_navstev = 0

# - - - - - - - - - - - - - - - -


@app.route('/string')
def text():
  return "Zdar, tahle primitivní funkce prostě vrací normální string."


@app.route("/nahodny-cislo")
def nahodny_cislo():
  nahodny = random.randrange(10)

  return "Tvoje dnešní číslo je: " + str(nahodny)


@app.route("/pocitadlo")
def pocitadlo():
  # použití global umožňuje funkci změnit hodnotu globální proměnné
  # (proměnná, která je mimo funkci, společná pro všechny uživatele serveru)
  global pocet_navstev
  pocet_navstev += 1

  return f'Tato stránka byla navštívena {pocet_navstev} krát.'


@app.route("/ukazka")
def ukazkove_html():

  return render_template("ukazka.html")


@app.route("/hodiny")
def hodiny():

  return render_template("clock.html")


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


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
