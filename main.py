# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 07:46:03 2020

@author: david
"""

# Implementación de los tableros semánticos (tableaux)
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria tableaux
import tableaux as T

# Fórmula (en notación polaca inversa)
# para obtener uno de sus tableaux
formula = "pq>-rO"

# Se crea el tableau
ta = T.Tableaux(formula)

# Imprime el resultado en consola
if len(ta) == 0:
    print('La fórmula es insatisfacible')
else:
    print('La fórmula es satisfacible.')
    print('Las hojas abiertas del tableaux son:')
    for l in ta:
        print(T.imprime_hoja(l))

