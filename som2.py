import numpy as np
from numpy import *
import math
import csv

class Neuronio:
    def __init__(self,name):
    		self.name = name

    def name(self,):
        return self.name


class SOM:
    def __init__(self,matrizi,matrizj,Rpontos):
        #self.Mneuronios = np.arange(matrizi*matrizj).reshape(matrizi,matrizj)
        #self.Mneuronios = np.empty(4,dtype=Neuronio)
        self.Mneuronios = []
        n = Neuronio("fa")

        teste = [n] * matrizj
        self.Mneuronios = [teste] * matrizi
        for i in range(0,matrizi):
            for j in range(0,matrizj):
                n = Neuronio("ij")
                self.Mneuronios[i][j] = n
                print self.Mneuronios[i][j].name ," ", i , j




a = SOM(3,4,3)
