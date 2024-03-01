"""

                                    ██╗░░░██╗██╗░░░░░░█████╗░██╗░░██╗██╗░░░██╗
                                    ██║░░░██║██║░░░░░██╔══██╗██║░░██║╚██╗░██╔╝
                                    ██║░░░██║██║░░░░░██║░░██║███████║░╚████╔╝░
                                    ██║░░░██║██║░░░░░██║░░██║██╔══██║░░╚██╔╝░░
                                    ╚██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░
                                    ░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
"""
# Úlohy na proměnné v názvu cesty

"""
ÚLOHA 1: Pozdrav uživatele

Vytvořte endpoint /pozdrav/<jmeno>, který přijme uživatelské jméno jako parametr v URL a vrátí pozdrav s tímto jménem.
Například, pokud uživatel navštíví /pozdrav/Petr, stránka by měla vrátit "Ahoj Petr!".
"""

"""
ÚLOHA 2: Obrácený řetězec

Vytvořte endpoint /obratit/<retezec>, který přijme libovolný řetězec jako parametr, obrátí jeho znaky a vrátí výsledek.
Například, pokud uživatel navštíví /obratit/ahoj, stránka by měla vrátit "joha".
"""

"""
ÚLOHA 3: Předpověď počasí

Vytvořte stránku /pocasi/<mesto>, který přijme název města jako parametr, a vrátí jednoduchou zprávu s "předpovídaným" počasím.
Počasí si můžete vymyslet, neboť tento příklad nemá reálné připojení k meteorologické službě. Můžete použít slovník níže:
"""

# Tento slovník použijte ve vaší službě.
# Pokud uživatel zadá neplatné počasí, tak mu vraťte "předpověď neznámá".

predpoved = {
    "Praha": "Slunečno s občasnými přeháňkami",
    "Brno": "Zataženo s možností deště",
    "Ostrava": "Částečně zataženo",
    "Plzeň": "Jasno"
}
