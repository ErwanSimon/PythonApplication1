#!/usr/bin/env python3
# coding: utf-8

import math

import numpy as np

import scipy
import scipy.stats as stats

import matplotlib.pyplot as plt

#from scipy.stats.distributions import norm

# calcul du tableau des relations-croisées (odds-ratio) à l'instar de la fonction twoby2() du langage R via la librairie Epi

def twoby2():
    #parametrer la fonction avec a,b,c et d des cas-temoins (application : glaucome et cataracte du diabetique, DOI?)
    # renvoyer le ratio et le petit p 
    
    # calcul du ratio
    # print(a * c / b * d)

    # calcul de l'intervalle de confiance à 95% 5SE : Standart Error): SE = sqrt(1/a + 1/b + 1/c + 1/d) ln(OR) <= ln(OR2) + 1.96 * SE
    # print ( exp(ln(OR))

    # stats.fish-exact(input)
    # return (oddsratio, pvalue)

    return(0)
    

#def carre(x)
# return x*x

#x=2
#print  carre(x);

# (lecture du fichier CSV comme dataframe avec pandas)


# INTERVALLES DE CONFIANCE
# calcul simple d'un intervalle de confiance à 95%

moyenne = 38.9
ecart_type = 13.28
effectif = 797 # echantillon effectivement mesuree , c.à.d sans les NA !

intervalle_inf = moyenne - 1.96 * ecart_type / math.sqrt(effectif)
intervalle_sup = moyenne + 1.96 * ecart_type / math.sqrt(effectif)

print("intervalle inferieur : ", intervalle_inf, "intervalle superieur : ", intervalle_sup)

# Score de relations croisées - étude cas-témoins
# Odds-Ratio

a = np.array([[840, 51663],[32, 5053]])
oddsratio, pvalue = stats.fisher_exact(a)
print("OddsR: ", oddsratio, "p-Value:", pvalue)
#>>> OddsR:  2.56743220487 p-Value: 2.72418938361e-09

# ecriture du ficher dataframe avec des entiers
np.savetxt("calcul_oddsratio.csv", a, delimiter=';',fmt='%d')

# affichage des donnees (histogramme ou boite a moustache pour l'etude dont l'odds-ratio (score de relations croisées) a été calculé
# x = np.linspace(-5,5,100)
# plt.plot(x,np.sin(x))
# plt.show()
