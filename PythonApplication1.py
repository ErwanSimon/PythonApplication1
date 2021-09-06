#!/usr/bin/python3

#encoding: utf-8

import numpy as np
from scipy.stats.distributions import norm

# calcul du tableau des relations-croisées (odds-ratio) à l'instar de la fonction twoby2() du langage R via la librairie Epi

def twoby2():
    #parametrer la fonction avec a,b,c et d des cas-temoins (application : glaucome et cataracte du diabetique, DOI?)
    # renvoyer le ratio et le petit p 
    
    # calcul du ratio
    # print(a * c / b * d)

    # calcul de l'intervalle de confiance à 95% 5SE : Standart Error): SE = sqrt(1/a + 1/b + 1/c + 1/d) ln(OR) <= ln(OR2) + 1.96 * SE
    # print ( exp(ln(OR))


    return(0)
    


print("hello world !")

