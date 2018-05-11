#coding:utf8

import numpy as np
import math
import csv
import matplotlib.pyplot as plt
from PIL import Image




class Neuronio:
    def __init__(self,x, s,name):
    		pesos= []
    		self.name = name
    	##	if "step" in name:
    	##		self.name = 1
    		self.pesos=pesos
    		np.random.seed(s)
    		
   
    def pesos(self):





        return self.pesos

    def atualizarpesos(self,x):
        eta = 0.1 # taxa de aprendizagem
        w0 = 0.0
        w1 = 0.0
        w0 = self.pesos[0] + eta * self.h(self.pesos) * (x[0]-self.pesos[0])
        w1 = self.pesos[1] + eta * self.h(self.pesos) * (x[1]-self.pesos[1])
        self.pesos[0] += w0
        self.pesos[1] += w1

    def h(self,x): # funcao vizinhança 
        return 0

# numero de interações é sempre 100 x M x N (Altura Largura)
# vizinhança 10.0
# Taxa de aprendizagem 0.1

class SOM:
    #def __init__(self,nrNeuronios,LPontos):
    #    self.Neuroniovetor = []
    #    self.data = [[]]
    #    self.numero = nrNeuronios
    #    for i in range(0,nrNeuronios):
    #        string = "Neuronio " + i   #seed inicializar os pesos aleatoriamente?
    #        n = Neuronio(posX, posY, data[posX][posY]) # 3 corresponde a vetor de pesos e intensidade ? confirmar
    #        self.Neuroniovetor.append(n)



            def __init__(self,matrizi,matrizj,Rpontos):
        #self.Mneuronios = np.arange(matrizi*matrizj).reshape(matrizi,matrizj)
        #self.Mneuronios = np.empty(4,dtype=Neuronio)
        self.Mneuronios = []
        self.data = carregaImagem()
        n = Neuronio("fa")

        teste = [n] * matrizj
        self.Mneuronios = [teste] * matrizi
        for i in range(0,matrizi):
            for j in range(0,matrizj):
                n = Neuronio("ij")
                self.Mneuronios[i][j] = n
                print self.Mneuronios[i][j].name ," ", i , j


    def carregaImagem(self):
		img = Image.open('egg.jpg').convert('L')  # convert image to 8-bit grayscale
		self.WIDTH, self.HEIGHT = img.size
		self.numero = self.WIDTH * self.HEIGHT

		data = list(img.getdata()) # convert image data to a list of integers
		# convert that to 2D list (list of lists of integers)
		self.data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]



    def bestNeuron(self,RPontos): # pontos aos quais vamos ver a distancia do nosso neuronio

        for i in range(0,len(RPontos): # iterar pontos input
        minimD = 100 # verificar numero muito grande que necessitamos para começar
        vencedor = -1
                for j in range(0,self.numero): # iterarar vetor de neuronios
                    dist = self.Euclidiana(self.Neuroniovetor[j],RPontos[i])
                    if dist < minimD :
                        minimD = dist
                        vencedor = j
                self.Neuroniovetor[vencedor].atualizarpesos(RPontos[i])




    def Euclidiana(x,y):
        distance = 0.0
        distance = (float (x[0])- float (y[0]))**2
        distance = distance + (float (x[1]) -float (y[1] ) )**2
        return math.sqrt (distance)
