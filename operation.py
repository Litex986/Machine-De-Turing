from Machine_turing import Table_action

#Soustraire 1

soustraire_1 = Table_action('Soustraire 1')
soustraire_1.creer_etat('e1')
soustraire_1.add('e1', None, None, 'gauche', 'e2')
soustraire_1.creer_etat('e2')
soustraire_1.add('e2', 0, 0, 'gauche', 'e2')
soustraire_1.add('e2', 1, 1, 'gauche', 'e2')
soustraire_1.add('e2', None, None, 'droite', 'e3')
soustraire_1.creer_etat('e3')
soustraire_1.add('e3', 0, 1, 'droite', 'e3')
soustraire_1.add('e3', 1, 0, 'droite', 'fin')
soustraire_1.add('e3', None, None, 'droite', 'fin')



#Ajouter 1

ajoute_1 = Table_action('Ajouter 1')
ajoute_1.creer_etat('e1')
ajoute_1.add('e1', None, None, 'gauche', 'e2')
ajoute_1.creer_etat('e2')
ajoute_1.add('e2', 0, 0, 'gauche', 'e2')
ajoute_1.add('e2', 1, 1, 'gauche', 'e2')
ajoute_1.add('e2', None, None, 'droite', 'e3')
ajoute_1.creer_etat('e3')
ajoute_1.add('e3', 0, 1, 'droite', 'fin')
ajoute_1.add('e3', 1, 0, 'droite', 'e3')
ajoute_1.add('e3', None, 1, 'droite', 'fin')


#Multiplier par 2

multiple_x2 = Table_action('Mutiplier par 2')
multiple_x2.creer_etat('e1')
multiple_x2.add('e1', None, None, 'gauche', 'e2')
multiple_x2.creer_etat('e2')
multiple_x2.add('e2', 0, 0, 'gauche', 'e2')
multiple_x2.add('e2', 1, 1, 'gauche', 'e2')
multiple_x2.add('e2', None, 0, 'gauche', 'fin')

#Detecter un palindrome

palindrome = Table_action('Detecter un palindrome')
palindrome.creer_etat('e1')
palindrome.add('e1', None, None, 'gauche', 'e2')
palindrome.creer_etat('e2')
palindrome.add('e2', 0, None, 'gauche', 'e3')
palindrome.add('e2', 1, None, 'gauche', 'e6')
palindrome.add('e2', None, None, 'gauche', 'OUI')
palindrome.creer_etat('e3')
palindrome.add('e3', 0, 0, 'gauche', 'e3')
palindrome.add('e3', 1, 1, 'gauche', 'e3')
palindrome.add('e3', None, None, 'droite', 'e4')
palindrome.creer_etat('e4')
palindrome.add('e4', 0, None, 'droite', 'e5')
palindrome.add('e4', 1, 1, 'gauche', 'NON')
palindrome.add('e4', None, None, 'gauche', 'OUI')
palindrome.creer_etat('e5')
palindrome.add('e5', 0, 0, 'droite', 'e5')
palindrome.add('e5', 1, 1, 'droite', 'e5')
palindrome.add('e5', None, None, 'gauche', 'e2')
palindrome.creer_etat('e6')
palindrome.add('e6', 0, 0, 'gauche', 'e6')
palindrome.add('e6', 1, 1, 'gauche', 'e6')
palindrome.add('e6', None, None, 'droite', 'e7')
palindrome.creer_etat('e7')
palindrome.add('e7', 0, 0, 'gauche', 'NON')
palindrome.add('e7', 1, None, 'droite', 'e5')
palindrome.add('e7', None, None, 'gauche', 'OUI')


#Doubler une liste de 1

double = Table_action('Doubler une liste de 1')
double.creer_etat('e1')
double.add('e1', None, None, 'gauche', 'e2')
double.creer_etat('e2')
double.add('e2', 0, 0, 'gauche', 'e2')
double.add('e2', 1, 0, 'droite', 'e3')
double.add('e2', None, None, 'droite', 'e4')
double.creer_etat('e3')
double.add('e3', 0, 0, 'droite', 'e3')
double.add('e3', None, 0, 'gauche', 'e2')
double.creer_etat('e4')
double.add('e4', 0, 1, 'droite', 'e4')
double.add('e4', None, None, 'droite', 'fin')


#Inverser les 0 et les 1

inverse = Table_action('Inverser les 0 et les 1')
inverse.creer_etat('e1')
inverse.add('e1', None, None, 'gauche', 'e2')
inverse.creer_etat('e2')
inverse.add('e2', 0, 1, 'gauche', 'e2')
inverse.add('e2', 1, 0, 'gauche', 'e2')
inverse.add('e2', None, None, 'gauche', 'fin')