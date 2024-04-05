"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

Úlohy bez Jinja2
  ---> v úlohách níže nemusíte používat render_template, abyste vrátili HTML jako odpověď na POST

  Stačí, když si HTML "postavíte" sami přímo uvnitř funkce a vrátíte STRING, např.:

   return f"<h1>Ahoj {michal}e!</h1>"


"""

"""
Úloha 1: BMI

Udělejte stránku s formulářem, kde uživatel zadá svojí výšku a váhu.
Po stisknutí tlačítka submit mu stránka vypočítá a ukáže jeho BMI.

Můžete se inspirovat stránkou "kalkulator" v ukázce.

BONUS:
 a) Dejte uživateli na výběr, jestli chce zadat výšku v METRECH nebo CENTIMETRECH.
    - použijte např. checkbox, nebo radio button

"""


"""
Úloha 2: Převodník jednotek

Realizujte stránku na převod jednotek.
Uživatel si bude moci vybrat ze seznamu jednotek ODKUD a KAM chce převádět.
Např.: mm, cm, m, km

"""

"""
Úloha 3: Kurz Krypta

Udělejte stránku, kde uživatel bude moci zadat JAKOU a KOLIK kryptoměny vlastní.
Stránka mu následně ukáže celkovou hodnotu.

Kurz kryptoměny si buď můžete vymyslet, nebo (těžší ale lepší verze) udělejte API call na stránku, na které se nachází opravdový kurz,
a ten potom použijte (podobně jako v úlohách na téma klient). 

"""
