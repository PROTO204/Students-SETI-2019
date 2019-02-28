#Exercice Shifumi avec 2 joueurs

list_elements = ["pierre","papier","ciseau"]

joueur1 = input("joueur 1 quel est votre nom? ")
joueur1_answer = input("\n%s quel est votre choix? " % joueur1)
while (joueur1_answer not in list_elements):
	joueur1_answer = input("\n%s, votre choix n'est pas dans la liste, veuillez choisir entre pierre papier et ciseau : " % joueur1)

joueur2 = input("\n joueur 2 quel est votre nom? ")
joueur2_answer = input("\n%s quel est votre choix? " % joueur2)
while (joueur2_answer not in list_elements):
	joueur2_answer = input("\n%s, votre choix n'est pas dans la liste, veuillez choisir entre pierre papier et ciseau : " % joueur2)

victoire ="personne"
if joueur1_answer == joueur2_answer:
	print("\nresultat identique, recommencez\n")

if joueur1_answer == "pierre" and joueur2_answer == "papier":
	victoire = joueur2

elif joueur1_answer == "pierre" and joueur2_answer == "ciseau":
	victoire = joueur1

elif joueur1_answer == "papier" and joueur2_answer == "ciseau":
	victoire = joueur2

elif joueur1_answer == "papier" and joueur2_answer == "pierre":
	victoire = joueur1

elif joueur1_answer == "ciseau" and joueur2_answer == "pierre":
	victoire = joueur2

elif joueur1_answer == "ciseau" and joueur2_answer == "papier":
	victoire = joueur1

if victoire != "personne":
	print("\n\n       Le joueur %s remporte la partie\n\n" % victoire)