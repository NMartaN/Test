"""
 Hustokrutopřísná kalkulačka
"""

class Kalkulacka:

    def scitani(a, b):

        return a + b

    def odcitani(a, b):
        return a - b
    def nasobeni(a, b):
        return a * b

    def deleni(a, b):
        if b == 0:
            return "Nelze dělit nulou!"
        else:
            return a / b
