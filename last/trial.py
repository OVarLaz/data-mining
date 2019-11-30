import numpy as np

import preprocess
import eros
import distance_metric
import pca
import mtsne
import graph_plot

from numpy import genfromtxt
#GENERACIoN DE DATOS SINTETICOS EN MEMORIA

def sintetica(var,nmts,depht): # Numero de variables, Numero de individuos o MTS,Profundidad de cada MTS
    #f_outp = open(outp, "w")
    sin = []
    labels=[]
    for i in  range(nmts):
        f = np.random.choice(5)
        labels.append(f)
        mts=[]
        for j in range(var):
            #a = np.random.rand(depht)#3000)
            b = np.random.choice(10,depht)
            v=b
            mts.append(v)
            #print v
        
        ss=np.array(mts)
        sin.append(mts)

    return np.array(sin),np.array(labels)

individuos=5
similarity_file='similarity_eros_'+str(individuos)


p_data,labels= sintetica(4,individuos,3)

data = p_data.mean(axis=2)
data2 = p_data.max(axis=2)
data3 = p_data.min(axis=2)


print p_data,data,data2
print np.concatenate((data, data2,data3), axis=1)

#dd=np.loadtxt('wave.csv')#loadtxt('wave.csv',delimiter=",")

dd = genfromtxt('wave.csv', delimiter=',')
dd=dd.reshape(5,7,3000)
print dd.shape
print dd