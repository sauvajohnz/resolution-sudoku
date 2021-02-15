import os
#resolveur de sudoku

#grille vierge:
"""
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],

exemple de grid resolvable
[0, 1, 0, 0, 2, 0, 0, 4, 0],
[9, 2, 4, 0, 3, 1, 0, 0, 0],
[0, 7, 6, 9, 0, 0, 2, 0, 0],
[1, 5, 0, 3, 4, 0, 0, 0, 6],
[0, 4, 0, 0, 6, 0, 0, 5, 0],
[6, 0, 0, 0, 7, 9, 0, 1, 4],
[0, 0, 5, 0, 0, 6, 9, 2, 0],
[0, 0, 0, 2, 9, 0, 4, 7, 8],
[0, 9, 0, 0, 8, 0, 0, 6, 0],
"""


#On demande d'abord à l'utilisateur sa grid, et on vérifie qu'elle est correcte
#exemple de grid: 010020040924031000076900200150340006040060050600079014005006920000290478090080060
input_sudoku = "0"
while len(input_sudoku) != 81:
    try:
        input_sudoku = input("Code sudoku (il doit faire 81 caractère): \nExemple: 010020040924031000076900200150340006040060050600079014005006920000290478090080060\n>")
        if len(input_sudoku) != 81:
            print("La grille n'est pas valable, recommencez")
            input_sudoku = "0"
    except ValueError:
        print("Il y a eu une erreur dans la valeur de cette grid")
        input_sudoku = "0"


#pour la grille du sudoku, on fait 9 tableau qui sont les lignes, dans un tableau qui est la grille totale
grid_sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

#on attribue la grid que l'utilisateur à entré à la grid du programme
ii = 0
for i in range(0,9):
    for y in range(0,9):
        grid_sudoku[i][y] = int(input_sudoku[ii])
        ii += 1

#la fonction scan determine la possibilitées de nombre qu'une case peut avoir, s'il n'y en a qu'une seule, elle est remplacée par ce nombre
def scan_case(ligne, case):
    # on attribue toutes les possibilitées qu'une case peut avoir comme nombre
    possibilitees = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #on scan d'abord sur la ligne horizontale
    for i in range(0,9):
        if grid_sudoku[i][case] != 0:
            try:
                possibilitees.remove(grid_sudoku[i][case])
            except ValueError:
                pass

    #on scan ensuite la ligne verticale
    for i in range(0,9):
        if grid_sudoku[ligne][i] != 0:
            try:
                    possibilitees.remove(grid_sudoku[ligne][i])
            except ValueError:
                pass

    #on scan pour finir le "carré"
    #on determine d'abors dans quel carré la case est située

    #on determine l'abscisse du carré
    if case >= 0 and case <= 2:
        x = 0
    elif case >= 3 and case <= 5:
        x = 3
    elif case >= 6 and case <= 8:
        x = 6
    else:
        print("erreur calcul du carré: axe des cases")

    #on determine l'ordonnée du carré
    if ligne >= 0 and ligne <= 2:
        y = 0
    elif ligne >= 3 and ligne <= 5:
        y = 3
    elif ligne >= 6 and ligne <= 8:
        y = 6
    else:
        print("erreur calcul du carré: axe des lignes")

    #on scan le carré
    for i in range(1,4): # on verifie les 3 prochaines lignes du carré
        for ii in range(1,4): # on verifie les 3 prochaines cases du carré
            if grid_sudoku[y][x] != 0:
                try:
                    possibilitees.remove(grid_sudoku[y][x])
                except ValueError:
                    pass
            x += 1
        #a chaque fois qu'on a verifié une ligne, on verifie la suivante, et on remet
        # la case a sa position de depart
        y += 1
        x -= 3

    #maintenant, s'il n'y a qu'une seule possibilitée on l'attribue a la grid sudoku
    if len(possibilitees) == 1:
        grid_sudoku[ligne][case] = possibilitees[0]
    elif len(possibilitees) == 0:
        print("Cette grid n'est pas valable, elle dispose de valeurs erronees")
        os.system("EXIT")


def resolve_sudoku():
    #on creer la variable grid_remplie pour verifier quand toute la grille aura été remplie.
    grid_remplie = False

    while grid_remplie is False:
        grid_remplie = True
        for i in range(0,9):
            for y in range(0,9):
                if grid_sudoku[i][y] == 0:
                    grid_remplie = False
                    scan_case(i, y)


#on affiche la grid
def afficher_grid():
    for i in range(0,9):
        for y in range(0,9):
            print(grid_sudoku[i][y], end=" ")
        print("")

print("Votre grille:")
afficher_grid() # on affiche la grille avant qu'elle soit résolue
print("\nGrille résolue :")
#on lance le programme de résolution
resolve_sudoku() # on resout la grille avec les scan
afficher_grid() # on affiche la grille finale

os.system("PAUSE") #permet de faire une pause pour ne pas quitter la fenetre