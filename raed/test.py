joueur1 = input("J_1 : sasir votre nom")
print ("joueur_1")
joueur1_answer = input( "%s J_1 : sasir votre choix" % joueur1)
print ("joueur1_answer")
joueur2 = input ("J_2 : sasir votre nom")
print ("joueur2")
joueur2_answer = input ("%s J_1 : sasir votre choix"% joueur2)
print ("joueur2_answer")
def comparaison(a1,a2):
    if (a1 == a2):
        print ("egalité, jouez encore une fois")
    elif (a1 == 'pierre' and a2 == 'feuille') :
        print (" joueur 2 à gagné ")
    elif (a1 == 'pierre)' and a2 == 'ciseaux'): 
        print (" joueur 1 à gagné ")
    elif (a1 == 'feuille') and (a2 == 'ciseaux'):
        print (" joueur 2 à gagné ")

#main = ["pierres", "feuille", "ciseaux"]
