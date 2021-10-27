#eerste 5 vragen

import sys

i = 11.81
def checkNumber(opgegevenGetal,vereistGetal,string):
    if int(opgegevenGetal) <= vereistGetal:
        print(string)
        exit()

prijs = input(f'ben je bereid om {str(i)} te betalen ')
if prijs == "ja":
    print('oke je kunt nu naar de vragen')
else:
    print('sorry als u dit niet wil betalen kunt u niet mee')
    exit()

leeftijdvraag = input('wat is je leeftijd ? ')
checkNumber(leeftijdvraag, 15, "sorry je bent niet oud genoeg")

sporten = input('hoeveel minuten sport je per dag ? ')
checkNumber(sporten, 60, "helaas bent u niet sportief genoeg luie ! ")

flexibel = input('op een schaal van 10 hoe flexibel bent u ? ')
checkNumber(flexibel,5,'helaas bent u niet flexibel genoeg ! ')

blijzijn  = input('op een schaal van 10 hoe positief bent u ? ')
checkNumber(blijzijn, 5, "helaas bent u niet positief genoeg")

doorzetting = input('hoeveel keer zet u door is u leven')
checkNumber(doorzetting, 10, "helaas zet u niet genoeg door")

# de beervragen
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('oke u bent door naar de eerste vragen de beer vragen ++')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
liften = input('hoeveel kilo kunt u benchen')
beerervaring = input('hoeveel jaar met trainen ervaring heeft u')

#beergedeelte
if int(liften) >= 100 and int(beerervaring) >= 4:
    print('gefeliciteerd je gaat de beer worden van het team')
    exit()
else:
    print('je hoort niet bij de beer team')

#de vosvragen
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+++++++++++++ oke nu bent u bij de vos vragen +++++++++')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
voservaring = input('hoeveel jaar heeft u in het bos gedaan')
metdieren = input('hoeveel jaar heb je met de dieren gewerkt')

#vosgedeelte
if int(voservaring) >= 4 and int(metdieren) >= 4:
    print('gefeliciteerd je gaat de vos worden van het team')
    exit()
else:
    print('je hoort niet bij de vos team')

#de bevervragen
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+++++++ nu zijn de bevervragen aan de beurt +++++++++++')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
bouwervaring = input('hoeveel jaar heb je ervaring met de bouw gewerkt')
matrialen = input('met hoeveel verschillende matrialen heeft u gewerkt')

#bevergedeelte
if int(bouwervaring) >= 4 and int(matrialen) >= 4:
    print('gefeliciteerd je gaat de bever worden van het team')
    exit()
else:
    print('je hoort niet bij de vos team')

#de uilvragen
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+++++ nu komen de uilvragen aan de tafel ++++++++++++++')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
eten = input('hoe snel in minuten kan je eten maken')
kennis = input('hoeveel jaar kennis heb je met eten en drinken')

#uilgedeelte
if int(eten) <= 10 and int(kennis) >= 4:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(' + gefeliciteerd je gaat de uil worden van het team +++')
    print('je hoort nu bij het team en het gaat een hele reis worden')
    print('maar maak je maar geen zorgen der komen ook mensen nog mee met ervaring')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    exit()
else:
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('je hoort niet bij de uil team')
    print('sorry je kan niet bij het team horen vanwege de de antwoorden op de vragen')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    


    




    



