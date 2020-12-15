#!/usr/bin/env python
# coding: utf-8

# In[1]:

# TRANSPOSER CE CODE DANS UN FICHIER .PY ET TROUVER COMMENT L'EXECUTER DEPUIS UN TERMINAL
import random
name1 = 'name1'
name2 = 'name2'
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'
names = [name1, name2, name3, name4, name5, name6]
names_total = []  
nombre = names
nb_groups = 3

max_nb_groups = int(len(names) / nb_groups)

for i in range(1, nb_groups+1):
    selected = random.sample(names, k=max_nb_groups)   
    print("GROUP #%s : %s" % (i, selected))

    for sel in selected:
        names.remove(sel)
        names_total.append(sel)    
        
print("ETUDIANTS: %s" %(names_total))

        


# In[2]:


# EXPLIQUEZ CE QUE FAIT RANDOM.SAMPLE ET LES ALTERNATIVES QUI EXISTENT EN CHERCHANT SUR INTERNET

''' Random simple est un module qui permet choisir aléatoirement un K numero d'items dans une liste, la syntax est
random.simple(population,k) '''

import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
new = random.sample(letters,3) #Cree une liste de 3 lettres aleatoires avec la population 'letters'
print(new)

''' random choice pour un seul string, choices pour une nouvelle liste '''


# In[ ]:


# EXPLIQUEZ LE %S DU PRINT, QUELS SONT LES AUTRES POSSIBILITES
'''il permet de formateer les strings avec des variables dedans.
il existe %s pour les strings  %d pour les integers  %f - Floating point numbers '''

a = "bernard"
b = "ca va?"
c = "tout va bien!"

print("hey %s %s %s" %(a,b,c))


# In[ ]:


# EXPLIQUEZ LE BUT DE CE SCRIPT
''' Creer nb_groups (3) dans une liste d'etudiants, de façon aleatoire, 
chaque groupe doit avoir le meme nombre d'integrants '''


# In[ ]:


# CORRIGEZ LES ERREURS CE SCRIPT
''' float conversion en integer, des ":" qui manquait, et des '""' qui manquait ''' 


# In[ ]:


# RAJOUTER AU SCRIPT UNE PARTIE QUI AFFICHE TOUS LES NOMS
'''creer une nouvelle liste names_total = [] 
dans un for loop selected, a la place de remove, il ajoute. '''
names_total = []
for sel in selected:
    names_total.append(sel)    
        


# In[ ]:


# FAITES EN SORTE QUE LE RESULTAT RESSEMBLE A
    # GROUP #1:  ['nameX', 'nameX']
    # GROUP #2:  ['nameX', 'nameX']
    # GROUP #3:  ['nameX', 'nameX']
    """modifier le range entre 1, et nombre de groupes + 1   (1,4) vu que le  4 n'est pas inclus """
    
    #for i in range(1, nb_groups+1):


# In[4]:


# MODIFIEZ LE SCRIPT PRECEDANT POUR OBTENIR LE MEME FONCTIONNEMENT SANS AVOIR A DETERMINER LE NOMBRE DE GROUPES

import random 
#Je declare tous les etudiants dans un seul string
x = "name1, name2, name3, name4, name5, name6" 
#Je separe le string en diferents elements et je les transforme en une liste
names = list(x.split(", ")) 

# je define le nombre d'etudiants par groupe
n_integrantes = 2
i = 0
#pendant que la liste d'etudiantes n'est pas vide, executer ceci:
while len(names)>0:
    selected = random.sample(names,k=n_integrantes)
    i+=1
    for sel in selected:
        names.remove(sel)
    print("Groupe %s: %s" %(i,selected))



# In[5]:


# MODIFIEZ LE PRINT POUR REVENIR A LA LIGNE AVANT D'AFFICHER LES GROUPES

import random 
#Je declare tous les etudiants dans un seul string
x = "name1, name2, name3, name4, name5, name6" 
#Je separe le string en diferents elements et je les transforme en une liste
names = list(x.split(", ")) 

# je define le nombre d'etudiants par groupe
n_integrantes = 2
i = 0

while len(names)>0:
    selected = random.sample(names,k=n_integrantes)
    i+=1
    for sel in selected:
        names.remove(sel)
    print("Groupe %s: %s" %(i,selected), end="\r")


# In[ ]:


# xxxxxx MODIFIEZ LE SCRIPT POUR SELECTIONNER UN A UN LES MEMBRES DE LA LISTE "selected"

