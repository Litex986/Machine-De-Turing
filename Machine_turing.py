import tkinter as tk
import operation


class Etats:
    def __init__(self, nom):
        '''
        name = nom de l'état
        ligne = contient les lignes de l'état
        '''
        self.name = nom
        self.ligne = []
    
    def print_(self):
        '''affiche l'etat en console'''
        for i in self.ligne:
            print([self.name, i[1], i[2], i[3], i[4]])
    
    def print_list(self):
        '''renvoie l'état sous forme de liste'''
        res = []
        for i in self.ligne:
            res.append([self.name, i[1], i[2], i[3], i[4]])
        return res
    
    def add(self, lit, ecrit, deplace, suivant):
        '''ajoute une ligne à l'état'''
        self.ligne.append([len(self.ligne), lit, ecrit, deplace, suivant])
    
    def insert(self, index, lit, ecrit, deplace, suivant):
        '''insert une ligne dans l'etat'''
        self.ligne.insert(index, [index, lit, ecrit, deplace, suivant])
        for i in range(index + 1, len(self.ligne)):
            self.ligne[i][0] = i
    
    def sup(self, index):
        '''supprime une ligne dans l'état'''
        self.ligne.pop(index)
        for i in range(index, len(self.ligne)):
            self.ligne[i][0] = i
    
    def return_lire(self):
        '''renvoie les valeurs 'lit' de l'état'''
        res = []
        for i in self.ligne:
            res.append(i[1])
        return res
    
    def return_ligne(self, index):
        '''renvoie une ligne de l'état'''
        return self.ligne[index]



class Ruban:
    '''permet de creer un ruban avec une taille e 100 par défaut'''
    def __init__(self, defaut=100):
        self.donne = [None for i in range(defaut)]
        self.index = 0
    
    def aggradir(self, taille_suplementaire):
        for i in range(taille_suplementaire):
            self.donne.append(None)



class Table_action:
    def __init__(self, nom):
        '''
        name = donne un nom a la table
        etat = regroupe les différents états
        '''
        self.name = nom
        self.etat = []
    
    def __str__(self):
        print(['Etat', 'Lit', 'Ecrit', 'Deplace', 'Suivant'])
        for i in self.etat:
            i.print_()
        return "\n=> Tableau d'éxécution."
    
    def print_list(self):
        '''revoie une liste contenant les etats dans des listes'''
        res = []
        for i in self.etat:
            res.append(i.print_list())
        return res
    
    def add(self, etat, lit, ecrit, deplace, suivant):
        '''permet d'ajouter un etat'''
        res = 'a'
        for i in range(len(self.etat)):
            if self.etat[i].name == etat:
                res = i
        if res == 'a':
            print(f"L'etat {etat} n'existe pas, pensez à le créer avant avec la méthode <.creer_etat(nom)>.")
        else:
            self.etat[res].add(lit, ecrit, deplace, suivant)
    
    def creer_etat(self, nom):
        '''permet de creer un nouvelle etat'''
        self.etat.append(nom)
        self.etat[-1] = Etats(nom)



class Machine_turing:
    def __init__(self, table_action):
        '''
        tableau = table d'action
        ruabn = ruban d'éxécution
        nombre = nombre binaire entrée par l'utilisateur
        fin = indique si l'écécution est terminé 
        auto = indique si l'utilisateur fait dérouler le programme automatiquement
        avancement [0] 
        =	0  -> Etat
        	1 -> Lit
        	2 -> Ecrit
        	3 -> Déplace
        	4 -> Suivant
        avancement [1] = l'etat en éxécution 
        avancement [2] = index ruban
        avacement [3] = etat, lit, ecrit, deplace, suivant
        '''
        self.tableau = table_action
        self.ruban = Ruban()
        self.interface = None
        self.nombre = 0
        self.fin = False
        self.auto = False
        self.avancement = [-1,self.tableau.print_list()[0][0][0], 0, [1,2,3,4,5]]
    
    def creer_liste_ruban(self, x):
        '''insère dans le ruban le nombre binaire'''
        for i in range(len(str(x))):
            self.ruban.donne[40 + i] = int(str(x)[i])
    
    def recup_res(self, x):
        '''a la fin de l'éxécution en console renvoie le résultat'''
        if x != "fin":
            return x
        res = ""
        for i in range(len(self.ruban.donne)):
            if self.ruban.donne[i] != None:
                res += str(self.ruban.donne[i])
        return res
    
    def check_etat(self, nom):
        '''défini l'etat suivant à éxécuter'''
        for i in range(len(self.tableau.etat)):
            if self.tableau.etat[i].name == nom:
                return i
        return None
    
    def run_console(self, nombre_binaire):
        '''execute la machine de Turing en console'''
        self.creer_liste_ruban(nombre_binaire)
        if self.tableau.etat == []:
            return nombre_binaire
        end = False
        self.ruban.index = 39
        etat = 0
        while not end:
            res = []
            for i in range(len(self.tableau.etat[etat].return_lire())):
                if self.tableau.etat[etat].return_lire()[i] == self.ruban.donne[self.ruban.index]:
                    res.append(i)
            if len(res) > 1:
                print(f"{self.tableau.etat[etat].name} n'est pas conforme.")
                return None
            elif len(res) < 1:
                print(f"{self.tableau.etat[etat].name} ne prend pas en compte si il est écrit {self.ruban.donne[self.ruban.index]}.")
                return None
            else:
                temp = self.tableau.etat[etat].return_ligne(res[0])
                self.ruban.donne[self.ruban.index] = temp[2]
                if temp[3] == 'gauche':
                    self.ruban.index += 1
                elif temp[3] == 'droite':
                    self.ruban.index -= 1
                else:
                    print(f"{temp[3].name} n'est pas roconnu comme deplacement.")
                    return None
                etat = self.check_etat(temp[4])
                if etat == None:
                    end = temp[4]
        return self.recup_res(temp[4])
    
    def run_interface(self):
        '''lance l'interface graphique '''
        self.interface = Interface(self.tableau.name, self)
        self.interface.start(self.tableau)
    
    def interface_exe(self, nombre):
        '''initialise pour pouvoir commencer l'éxécution en interface graphique'''
        if self.avancement[0] == -1:
            self.auto = True
            self.fin = False
            self.interface.change_couleur(self.avancement[1], 'black')
            self.interface.ruban_reset()
            self.nombre = ' ' * 50 + str(nombre) + ' ' * 50
            self.avancement = [0,self.tableau.print_list()[0][0][0], 0, [1,2,3,4,5]]
            self.interface_boucle()
        elif self.auto == False:
            self.auto = True
            self.interface_boucle()
    
    def interface_boucle(self):
        '''repète l'action toute les x secondes après le démarage de l'éxécution en automatique'''
        if not self.fin:
            self.interface.fen.after_idle(self.interface_deroulement)
            self.interface.fen.after(int(2000 / (self.interface.vitesse + 1)), self.interface_boucle)
        else:
            self.auto = False
    
    def interface_pasapas(self):
        '''initialiste pour pouvoir commencer l'éxécution en pas à pas en interface graphique'''
        if self.avancement[0] == -1:
            self.fin = False
            self.interface.change_couleur(self.avancement[1], 'black')
            self.interface.ruban_reset()
            self.nombre = ' ' * 50 + str(self.interface.saisie_nb) + ' ' * 50
            self.avancement = [0,self.tableau.print_list()[0][0][0], 0, [1,2,3,4,5]]
        elif self.auto == False:
            self.interface_deroulement()
    
    def interface_deroulement(self):
        '''éxécute une étapes de la machine de Turing'''
        if self.avancement[0] == 0:
            self.interface.change_couleur(str(self.avancement[3][0]) + '_lit_' + ('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_suivant_' + str(self.avancement[3][4]), 'black')
            a = []
            for i in self.tableau.print_list():
                if i[0][0] == self.avancement[1]:
                    a.append(i)
                    self.avancement[3] = i
            if len(a) > 1:
                print(f"Il y a deux états nommé {self.avncement[1]}.")
                return None
            self.interface.change_couleur(str(self.avancement[1]))
            self.avancement[0] += 1
        elif self.avancement[0] == 1:
            a = []
            for i in self.avancement[3]:
                if i[1] == None:
                    if self.nombre[49 + self.avancement[2]] == ' ':
                        a.append(i)
                elif str(i[1]) ==  self.nombre[49 + self.avancement[2]]:
                    a.append(i)
            if len(a) > 1:
                print(f"Il y a deux 'lit' {a[0][1]}.")
                return None
            self.avancement[3] = a[0]
            self.interface.change_couleur(str(self.avancement[1]),'black')
            self.interface.change_couleur(str(self.avancement[1]) + '_lit_' + str('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])))
            self.avancement[0] += 1
        elif self.avancement[0] == 2:
            if self.avancement[3][2] == None:
                self.nombre =  self.nombre[:(49 + self.avancement[2])] + ' ' + self.nombre[(50 + self.avancement[2]):]
                self.interface.can.itemconfig(self.interface.ruban_item[30 + self.avancement[2]][0], text=' ')
            else:
                self.nombre =  self.nombre[:(49 + self.avancement[2])] + str(self.avancement[3][2]) + self.nombre[(50 + self.avancement[2]):]
                self.interface.can.itemconfig(self.interface.ruban_item[30 + self.avancement[2]][0], text=self.avancement[3][2])
            self.avancement[0] += 1
            self.interface.change_couleur(str(self.avancement[1]) + '_lit_' + str('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])), 'black')
            self.interface.change_couleur(str(self.avancement[1]) + '_lit_' + str('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_ecrit_' + str('Vide' if self.avancement[3][2] == None else str(self.avancement[3][2])))
        elif self.avancement[0] == 3:
            if self.avancement[3][3] == 'gauche':
                self.avancement[2] += 1
            elif self.avancement[3][3] == 'droite':
                self.avancement[2] -= 1
            else:
                print(f"{self.avancement[3][3]} n'est pas roconnu comme deplacement.")
                return None
            self.interface.ruban_decal(self.avancement[3][3])
            self.avancement[0] += 1
            self.interface.change_couleur(str(self.avancement[1]) + '_lit_' + str('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_ecrit_' + str('Vide' if self.avancement[3][2] == None else str(self.avancement[3][2])), 'black')
            self.interface.change_couleur(self.avancement[1] + '_lit_' + ('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_deplace_' + str(self.avancement[3][3]))
        elif self.avancement[0] == 4:
            self.interface.change_couleur(self.avancement[1] + '_lit_' + ('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_deplace_' + str(self.avancement[3][3]), 'black')
            a = []
            for i in self.tableau.print_list():
                for j in i:
                    a.append(j[0])
            res = []
            for i in a:
                if self.avancement[3][4] == i:
                    res.append(i)
                    self.avancement[1] = i
            self.interface.change_couleur(str(self.avancement[3][0]) + '_lit_' + ('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_suivant_' + str(self.avancement[3][4]))
            if len(res) == 0:
                self.avancement[1] = str(self.avancement[3][0]) + '_lit_' + ('Vide' if self.avancement[3][1] == None else str(self.avancement[3][1])) + '_suivant_' + str(self.avancement[3][4])
                self.avancement[0] = -1
                self.fin = True
            else:
                self.avancement[0] = 0



class Interface:
    def __init__(self, nom, machine):
        '''
        name = nom de la machine
        machine = contient la machine de Turing
        fen = contient la fenetre de l'interface
        can = contient le canvas de l'interface
        saisie = contient la zone de saisie de l'interface
        saisie_nb = stock le nombre entré par l'utilisateur
        nombre = dans le canvas contient le nombre entré par l'utilisateur
        bouton = contient le bouton 'ok' pour valider le nombre
        vitesse = dans le canvas contient la vitesse d'éxécution
        vitesse_xy = dans le canvas contient les restangles pour illustrer la vitesse
        ruban_item = contient les rectangles et les chiffres du ruban
        tabl = contient la table d'action de l'interface
        '''
        self.name = nom
        self.machine = machine
        self.fen = None
        self.can = None
        self.saisie = None
        self.saisie_nb = None
        self.nombre = None
        self.bouton = None
        self.vitesse = -1
        self.vitesse_xy = []
        self.ruban_item = []
        self.tabl = []
    
    def start(self, table_exe):
        self.tabl = table_exe.print_list() #récupère la table d'action
        self.fen = tk.Tk() #créer la fenètre
        self.fen.title(f"Machine_Turing - {table_exe.name}") #done un nom a la fenètre
        self.creer_hors_can()
        self.can = tk.Canvas(self.fen, height=600, width=900) #créer le canvas de l'interface
        self.can.pack(side='bottom') #place le canvase sur l'interface 
        self.creer_tabl()
        self.creer_interraction(table_exe)
        self.ruban_exe()
        self.can.tag_bind("bouton_moins", "<Button-1>", self.vitesse_case_sup) #détecte le click sur le '+' du canvas
        self.can.tag_bind("bouton_plus", "<Button-1>", self.vitesse_case_add) #détecte le click sur le '-' du canvas
        self.can.tag_bind("bouton_commencer", "<Button-1>", self.commencement) #détecte le click sur le 'Commencer' du canvas
        self.can.tag_bind("bouton_pasapas", "<Button-1>", self.pasapas) #détecte le click sur le 'Pas à pas' du canvas
        self.fen.mainloop()
    
    def creer_tabl(self):
        '''permet de créer le tableau contenant la table d'action'''
        x = 540
        y = 60
        a = 2
        for i in self.tabl:
            for j in i:
                a += 1
        #créer les lignes du tableau
        for i in range(a):
            y += 30
            #ligne horizontale
            self.can.create_line(x, y, x + 340, y)
        if i > 10:
            self.can.config(height=800)
        for i in range(6):
            #ligne verticale
            self.can.create_line(x - 85, 90, x - 85, y)
            x += 85
        a = [[1, 'Etat']]
        x = 540
        y = 90
        self.can.create_line(x - 85, y, x + 340, y, width=3)
        self.can.create_text(x + 40, y + 15, text='Lit', font=28)
        self.can.create_text(x + 125, y + 15, text='Ecrit', font=28)
        self.can.create_text(x + 210, y + 15, text='Deplace', font=28)
        self.can.create_text(x + 295, y + 15, text='Suivant', font=28)
        for i in self.tabl:
            a.append([len(i), i[0][0]])
        for i in a:
            y += i[0] * 30
            #ajoute des lignes plus épaisse pour délimiter les états
            self.can.create_line(x - 85, y, x + 340, y, width=3)
            self.can.create_text(x - 50, y - i[0] * 30 + 15, text=i[1], font=28, tag=str(i[1]))
        a = []
        y = 105
        for i in self.tabl:
            for j in i:
                a.append([j[1] if j[1] != None else 'Vide', j[2] if j[2] != None else 'Vide', j[3], j[4], j[0]])
        for i in a:
            y += 30
            #met le texte dans le tableau avec un tag pour permettre de changer la couleur par la suite
            self.can.create_text(x + 40, y, text=i[0], font=28, tag=str(i[4]) + '_lit_' + str(i[0]))
            self.can.create_text(x + 125, y, text=i[1], font=28, tag=str(i[4]) + '_lit_' + str(i[0]) + '_ecrit_' + str(i[1]))
            self.can.create_text(x + 210, y, text=i[2], font=28, tag=str(i[4]) + '_lit_' + str(i[0]) + '_deplace_' + str(i[2]))
            self.can.create_text(x + 295, y, text=i[3], font=28, tag=str(i[4]) + '_lit_' + str(i[0]) + '_suivant_' + str(i[3]))
 
    def vitesse_case(self):
        '''place les carrés pour illustré la vittesse'''
        for i in range(10):
            self.vitesse_xy.append(self.can.create_rectangle(105 + i * 22, 257, 105 + i * 22 + 22, 263, fill='white'))
    
    def creer_interraction(self, table):
        '''créer la partie du canvas gérabble par l'utilisateur'''
        self.can.create_rectangle(15, 90, 430, 360, width=3) #contour
        self.can.create_text(430 / 2, 120, text='Vous avez choisit le programme:', font=28) #indique la table d'action choisit
        self.can.create_text(430 / 2, 140, text=table.name, font=30, fill='blue')
        self.can.create_text(430 / 2, 180, text='Valeur entrée:', font=28) #indique la valeur entré par l'utilisateur
        self.nombre = self.can.create_text(430 / 2, 200, text='Vide', font=28, fill='blue')
        self.can.create_text(430 / 2, 240, text='Vitesse:', font=28) #indique la valeur de la vitesse
        self.can.create_rectangle(103 , 255, 327, 265) 
        self.vitesse_case()
        self.vitesse_xy.append(self.can.create_text(430 / 2, 275, text='x', font=28, fill='blue'))
        self.vitesse_case_add(1)
        self.can.create_text(95, 260, text='-', font=28, tags='bouton_moins') #creer un bouton '-'
        self.can.create_text(335, 260, text='+', font=28, tags='bouton_plus') #creer un bouton '+'
        self.can.create_text(120, 320, text='Commencer', font=28, tags='bouton_commencer') #creer un bouton 'Commencer'
        self.can.create_text(310, 320, text='Pas à pas', font=28, tags='bouton_pasapas') #creer un bouton 'Pas à pas'
        self.can.create_rectangle(65, 305, 175, 335)
        self.can.create_rectangle(255, 305, 365, 335)
    
    def actualisation_nombre(self):
        '''récupère le nombre entré par l'utilisateur'''
        if self.machine.avancement[0] != -1:
            print('La machine est en marche.')
        self.saisie_nb = self.saisie.get()
        for i in self.saisie_nb:
            if i != '1' and i != '0':
                print("Le nombre entré n'est pas un nombre bianire")
                self.saisie_nb = None
                return None
        self.can.itemconfig(self.nombre, text=self.saisie_nb) #change la valeur dans l'interface
        self.ruban_reset()
    
    def ruban_reset(self):
        '''remet le ruban en place et entre le nombre dedans'''
        for j in range(len(self.ruban_item)):
            self.can.itemconfig(self.ruban_item[j][0], text='')
            self.can.coords(self.ruban_item[j][0], 7 + 15 * j, 40)
            self.can.coords(self.ruban_item[j][1], -300 + 15 * j, 30, -300 + 15  + 15 * j, 50)
        for i in range(len(self.saisie_nb)):
            self.can.itemconfig(self.ruban_item[31 + i][0], text=self.saisie_nb[i], tag='ruban_' + str(i))

    def creer_hors_can(self):
        cadre = tk.Frame(self.fen) #créer une boite
        cadre.pack(side='top') #place la boite
        saisie_entre = tk.StringVar() 
        saisie_entre.set("Entrer un nombre binaire") #définit le texte par défaut de la zone de saisie
        self.saisie = tk.Entry(cadre, textvariable=saisie_entre, width=30) #créer la zone de saisie dans la boite
        self.saisie.pack(side='left') #place la zone de saisie
        self.bouton = tk.Button(cadre, text="OK", command=self.actualisation_nombre) #créer le bouton 'ok' dans la boite
        self.bouton.pack(side='left') #place le bouton
    
    def vitesse_case_add(self, event):
        '''augmente la représentation de la vitesse'''
        if self.vitesse < 9:
            self.vitesse += 1
            self.can.itemconfig(self.vitesse_xy[self.vitesse], fill='green')
            self.can.itemconfig(self.vitesse_xy[10], text=f'x{self.vitesse + 1}')
    
    def vitesse_case_sup(self, event):
        '''diminue la représentation de la vitesse'''
        if self.vitesse > 0:
            self.can.itemconfig(self.vitesse_xy[self.vitesse], fill='white')
            self.vitesse -= 1
            self.can.itemconfig(self.vitesse_xy[10], text=f'x{self.vitesse + 1}')
    
    def ruban_exe(self):
        '''créer le ruban'''
        for i in range(100):
            self.ruban_item.append([self.can.create_text(7 + 15 * i, 40, text=''), self.can.create_rectangle(-300 + 15 * i, 30, -300 + 15  + 15 * i, 50)])
        self.can.create_rectangle(450, 30, 465, 50, width=2, outline='red')
    
    def ruban_decal(self, deplace):
        '''décale le ruban'''
        if deplace == 'gauche': #a gauche  
            for i in range(len(self.ruban_item)):
                for j in range(5):
                    self.can.move(self.ruban_item[i][0], -3, 0)
                    self.can.move(self.ruban_item[i][1], -3, 0)
        elif deplace == 'droite': #a droite
            for i in range(len(self.ruban_item)):
                self.can.move(self.ruban_item[i][0], +15, 0)
                self.can.move(self.ruban_item[i][1], +15, 0)
        else:
            print(f"{deplace} n'est pas roconnu comme deplacement.")
            return None
    
    def commencement(self, event):
        '''lance l'éxécution de la machine de Turing automatique'''
        if self.saisie_nb != None:
            self.machine.interface_exe(self.saisie_nb)
    
    def pasapas(self, event):
        '''lance l'éxécution de la machine de Turing pas à pas'''
        if self.saisie_nb != None:
            self.machine.interface_pasapas()
        else:
            print("Aucun nombre n'a été entré.")
    
    def change_couleur(self, tag, color='red'):
        '''change la couleur grace au tag'''
        self.can.itemconfig(tag, fill=color)






a = Machine_turing(operation.palindrome)
a.run_interface()

