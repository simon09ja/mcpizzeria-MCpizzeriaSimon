# Dit bestand zorgt voor de gebruikersinterface (GUI) van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Simon Janssen
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    if gevonden_klanten == []:
        labelResultaat.config(text="Geen klant gevonden.")
    else:
        labelResultaat.config(text="Gevonden: " + str(gevonden_klanten))


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico")
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")
knopSluit = Button(venster, text="Sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=17, column=2)

labelNaam = Label(venster, text="Klantnaam:")
labelNaam.grid(row=1, column=0)

ingevoerde_klantnaam = StringVar()

invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

knopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
knopZoekOpKlantnaam.grid(row=1, column=14)

labelResultaat = Label(venster, text="")
labelResultaat.grid(row=2, column=0, columnspan=5, sticky="W")

venster.mainloop()