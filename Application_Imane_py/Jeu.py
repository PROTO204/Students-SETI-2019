
# -*- coding: utf8 -*-
# coding : utf8 

joueur1 = input ("quel est votre nom?")
joueur1_answer=input("%s quel est votre choix?" %joueur1)

joueur2 = input ("quel est votre nom?")
joueur2_answer=input("%s quel est votre choix?" %joueur2)

def comparaison(a1,a2):
	if(a1==a2):
		resultat = 1
	elif ((a1 == "ciseau" and a2 =="pierrre") or(a1 == "papier" and a2 =="pierrre")or (a1 == "papier" and a2 =="ciseau") or (a1 == "pierre" and a2 =="papier")):
		resultat = joueur2
	else:
		resultat = joueur1
	
	return resultat

if(comparaison(joueur1_answer,joueur2_answer) == 1):
	print("Egalité")
else:
	print("%s vous avez gagné" %comparaison(joueur1_answer,joueur2_answer))

