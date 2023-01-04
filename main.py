PLATEAU = [[False, False, False],
           [False, False, False],
           [False, False, False]]

def affichage_matriciel(p):
  print('\n'.join('  ' + ' '.join('%s' % x for x in l) for l in p))


def coup_possible(p, coup):
  """
  Nous informe si un coup est possible
  Parameters: 
  p: plateau
  coup : tuple (i, j) c'est la position a laquelle le joeur souhaite placer son pion
  Output: Boolean
  True si le coup est possible, False sinon
  
  """
  i = coup[0]
  j = coup[1]
  if (i < 3) and (i >= 0)  and (j < 3) and (j >= 0) and (p[i][j] == False) :
    return True
  else:
    print('Coup impossible veuillez rejouer un autre coup')
    return False

def modifier_plateau(p, coup, joueur):
  """
  Modifie l'état du plateau après chaque coup
  Parameters: 
  p: plateau, liste de liste 
  coup : tuple (i, j) c'est la position a laquelle le joeur souhaite placer son pion
  joueur: string qui est le pseudo du joueur
  Outputs:
  Rien, mais modifie l'état du plateau en placant le nouveau pion joué si c'est possible. Pas d'effet si la position est déjà occupé
  
  """
  i = coup[0]
  j = coup[1]
  if coup_possible(p, coup):
    p[i][j] = joueur
    return True
  return False

def sont_adjacents(p, p1, p2):
  """
  Verifie si deux points du plateau sont adjacents 

  Parameters: 
  p : plateau
  p1, p2 : coordonnees des deux points a verifier

  Output:
  True si les deux points sont adjacents, False sinon
  
  """
  x_p1, y_p1 = p1[0], p1[1]
  x_p2, y_p2 = p2[0], p2[1]
  if p1 != p2:
    if p1 == (1, 1) or p2 == (1, 1):
      return True
    if abs(x_p1 - x_p2) == 0:  # Les deux points p1 et p2 sont sur la meme ligne
      if abs(y_p1 - y_p2) == 1:
        #print('Les deux ' + str(p1) + ' et ' + str(p2) + ' points sont adjacents')
        return True
      else:
        #print('Les deux points + str(p1) ' + ' et ' + str(p2) + ' ne sont pas adjacents')
        return False
    if abs(y_p1 - y_p2) == 0:  # Les deux points p1 et p2 sont sur la meme colonne
      if abs(x_p1 - x_p2) == 1:
        #print('Les deux points ' + str(p1) + ' et ' + str(p2) + ' sont adjacents')
        return True
      else:
        #print('Les deux points + str(p1) ' + ' et ' + str(p2) + ' ne sont pas adjacents')
        return False


def detecter_moulin(p, joueur):
  """
  Permet de detecter les moulins existants dans le plateau p

  Paramaeters : 
  p: plateau du jeu
  joueur : = string qui est le pseudo du joueur
  Outputs:
    True si moulin trouvé False sinon
  """
  points_joueur = []
  for i in range (len(p)):
    for j in range(len(p)):
      if p[i][j] == joueur:
        points_joueur.append((i,j))
  points_joueur = sorted(points_joueur)
  # Les moulins possibles (8 possibilités)
  m1 = [(0, 0), (0, 1), (0, 2)]
  m2 = [(1, 0), (1, 1), (1, 2)]
  m3 = [(2, 0), (2, 1), (2, 2)]
  m4 = [(0, 0), (1, 0), (2, 0)]
  m5 = [(0, 1), (1, 1), (2, 1)]
  m6 = [(0, 2), (1, 2), (2, 2)]
  m7 = [(0, 0), (1, 1), (2, 2)]
  m8 = [(0, 2), (1, 1), (2, 0)]
  moulins = [m1, m2, m3, m4, m5, m6, m7, m8]
  # detecter mouelins du joueur passé en paramétre
  if len(points_joueur) == 3:
    if points_joueur in moulins:
      return True
    else :
      False



def detecter_vitoire(p, joueur):
    if detecter_moulin(p, joueur):
        print('Victoire pour', joueur)
        return True
    else: 
        return False


def deplacer_pion(p, joueur, deplacement):
   """
   Permet de déplacer un pion au sein du plateau une fois tous les joueurs ont placer leurs pions
   Parameters: 
   p: plateau, liste de liste 
   deplacement : liste de deux points, le premier sera la position du pion à déplacer et le scond sera la position finale de ce pion 
                 apres ce déplacement
   joueur: string, 'j1' ou 'j2'
   """
   p_inial = deplacement[0]  
   p_final = deplacement[1]
   print('Déplacement choisi: ', p_inial, 'vers', p_final)
   i_ini = p_inial[0]
   j_ini = p_inial[1]
   i_final = p_final[0]
   j_final =p_final[1]
   val_inter = p[i_final][j_final]  # Pour ne pas écraser la valeur p[i_final][j_final]
   p[i_final][j_final] = p[i_ini][j_ini]
   p[i_ini][j_ini] = val_inter
   return p








def retirer_pion(p, pion_a_retirer, joueur):
  """
  Retire un pion du plateau suite à la formation d'un moulin 
  Parameters: 
  p: plateau, liste de liste 
  pion_a_retirer : tuple (i, j) c'est la position du pion à retirer
  joueur: string, 'j1' ou 'j2'
  Outputs:
  Rien, mais modifie l'état du plateau en retirant pion passé en parametre du joueur adverse au joeuru passé en parametre 
  """
  i = pion_a_retirer[0]
  j = pion_a_retirer[1]
  if detecter_moulin(p, joueur) and pion_a_retirer != False:
    if joueur == 'j1':
      p[i][j] = False
    elif joueur == 'j2':
      p[i][j] = False

  return p

def verifier_victoire_apres_coup(plateau, joueur1, joueur2):
  # vérifier si on a victoire après un coup
      victoire1 = detecter_vitoire(plateau, joueur1)
      victoire2 = detecter_vitoire(plateau, joueur2)
      if victoire1 or victoire2:
        return True
      return False


def jouer():
    print('Bonjour et bienvenu dans cette nouvelle partie du meilleur jeu au monde: Les moulins!\n')
    plateau = [[False, False, False],
                [False, False, False],
                [False, False, False]]
    print("Voici l'état initial du plateau de jeu variante à 3:\n")
    affichage_matriciel(plateau)
    print('Merci de donner vos noms \n')
    joueur1= input() #j1
    joueur2= input() #j2
    print("\n Veuillez commencer à placer vos pions! \n")
    nbr_pions_j1 = 1
    nbr_pions_j2 = 1
    while (detecter_vitoire(plateau, joueur1) == False) and (detecter_vitoire(plateau, joueur1) == False) and nbr_pions_j1 <= 3 and nbr_pions_j2 <= 3:
        # Joueur 1
        print('Tour du joueur', joueur1)
        coup = input()
        coup = tuple(int(x) for x in coup.split(","))  # transforme l'entrée en tuple ex: 1,1 ==> (1,1)
        modification =  modifier_plateau(plateau, coup, joueur1)
        while modification == False:
            print('Tour du joueur', joueur1)
            coup = input()
            coup = tuple(int(x) for x in coup.split(","))
            modification =  modifier_plateau(plateau, coup, joueur1)
        nbr_pions_j1 += 1
        affichage_matriciel(plateau)
        # vérifier si on a victoire après ce coup
        if verifier_victoire_apres_coup(plateau, joueur1, joueur2):
            break

        # Joueur 2
        print('Tour du joueur', joueur2)
        coup = input()
        coup = tuple(int(x) for x in coup.split(","))
        modification =  modifier_plateau(plateau, coup, joueur2)
        while modification == False:
            print('Tour du joueur', joueur2)
            coup = input()
            coup = tuple(int(x) for x in coup.split(","))
            modification =  modifier_plateau(plateau, coup, joueur2)
        nbr_pions_j2 += 1
        affichage_matriciel(plateau)
        # vérifier si on a victoire après ce coup
        if verifier_victoire_apres_coup(plateau, joueur1, joueur2):
            break
    print("Tous les pions ont été bien placés, vous pouvez commencer à les dépalcer!")

    while (detecter_vitoire(plateau, joueur1) == False) and (detecter_vitoire(plateau, joueur1) == False) :
        # Joueur 1
        print('Tour du joueur', joueur1)
        print('Entrez la position du pion à déplacer')
        p_ini = input()
        p_ini = tuple(int(x) for x in p_ini.split(","))  # transforme l'entrée en tuple ex: 1,1 ==> (1,1)
        print('Entrez la position à laquelle vous voulez mettre votre pion')
        p_final = input()
        p_final = tuple(int(x) for x in p_final.split(","))  # transforme l'entrée en tuple ex: 1,1 ==> (1,1)
        deplacement = [p_ini, p_final]
        modification =  deplacer_pion(plateau, joueur1, deplacement)
        affichage_matriciel(plateau)
        # vérifier si on a victoire après ce coup
        if verifier_victoire_apres_coup(plateau, joueur1, joueur2):
             break

        # Joueur 2
        print('Tour du joueur', joueur2)
        print('Entrez la position du pion à déplacer')
        p_ini = input()
        p_ini = tuple(int(x) for x in p_ini.split(","))  # transforme l'entrée en tuple ex: 1,1 ==> (1,1)
        print('Entrez la position à laquelle vous voulez mettre votre pion')
        p_final = input()
        p_final = tuple(int(x) for x in p_final.split(","))  # transforme l'entrée en tuple ex: 1,1 ==> (1,1)
        deplacement = [p_ini, p_final]
        modification =  deplacer_pion(plateau, joueur2, deplacement)
        affichage_matriciel(plateau)
        # vérifier si on a victoire après ce coup
        if verifier_victoire_apres_coup(plateau, joueur1, joueur2):
            break

if __name__ == "__main__":
    jouer()