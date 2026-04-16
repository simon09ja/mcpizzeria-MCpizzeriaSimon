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
    invoerveldKlantnaam.delete(0, END)  #invoerveld voor naam leeg maken 
    invoerveldKlantNr.delete(0, END)  #invoerveld voor klantNr leeg maken 
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert 
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld 
        invoerveldKlantNr.insert(END, rij[0])  
        
        #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld 
        invoerveldKlantnaam.insert(END, rij[1])

def toonMenuInListbox(): 
    listboxMenu.delete(0, END)  #maak de listbox leeg 
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel() 
    for regel in pizza_tabel: 
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu 
    listboxMenu.insert(0, "ID Gerecht Prijs")

def haalGeselecteerdeRijOp(event): 
    #bepaal op welke regel er geklikt is 
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0]  
    #haal tekst uit die regel 
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
     #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat 
    invoerveldGeselecteerdePizza.delete(0, END)  
    #zet tekst in veld 
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst) 

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

listboxMenu = Listbox (venster, height=6, width=50)
listboxMenu.grid(row=4,column=1,rowspan=6,columnspan=2, sticky="w")

labelMogelijkheden = Label(venster, text="Mogelijkheden:")
labelMogelijkheden.grid(row=4, column=0, sticky="W")

knopToonPizzas = Button(venster, text="Toon alle pizza’s", width=12, command=toonMenuInListbox) 
knopToonPizzas.grid(row=3, column=4)

labelGekozenPizza = Label(venster, text="Gekozen pizza:")
labelGekozenPizza.grid(row=15, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()

invoerveldGeselecteerdePizza = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldGeselecteerdePizza.grid(row=15, column=1, sticky="W")

venster.mainloop()