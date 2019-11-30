import numpy as np

import preprocess
import eros
import distance_metric
import pca
import mtsne
import graph_plot
import connection

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
            a = np.random.rand(depht)#3000)
            b = np.random.choice(100,depht)
            v=a+b
            mts.append(v)
            #print v
        
        ss=np.array(mts)
        sin.append(mts)

    return np.array(sin),np.array(labels)

individuos=30
similarity_file='similarity_eros_'+str(individuos)

# def read_data(labels,files,var,muestras,depht):
#     dd = genfromtxt(files[0]+'.csv', delimiter=',')
#     data=dd.reshape(muestras,var,depht)
#     #print data.reshape
#     l=np.repeat(labels,muestras)
#     for i in range(1,len(files)):
#         dd = genfromtxt(files[i]+'.csv', delimiter=',')
#         dd=dd.reshape(muestras,var,depht)
#         #print files[i]
#         #print dd.shape
#         data=np.append(data,dd)
#         #print data.shape
#     data=data.reshape(muestras*len(files),var,depht)
#     print data.shape,l
#     return data,l


#files=['n/uno','n/dos','n/tres','n/cuatro','n/rem','n/wave']
#files=['j/uno','j/dos','j/tres','j/cuatro','j/rem','j/wave']
files=['ondas/uno','ondas/dos','ondas/tres','ondas/cuatro','ondas/rem','ondas/wave']
lab=[1, 2 ,3 ,4, 'R','W']
patients = ["SC4031E0","SC4032E0","SC4051E0","SC4052E0","SC4071E0","SC4072E0","SC4121E0","SC4122E0","ST7132J0","ST7141J0","ST7201J0","ST7022J0","ST7071J0"]
#"SC4052E0","SC4072E0",,"SC4121E0","SC4122E0","ST7022J0"
patientsfordtw = ["SC4032E0"]#,"SC4051E0","SC4071E0","ST7132J0","ST7141J0","ST7201J0","ST7071J0"]

#p_data,labels= sintetica(4,individuos,300)
# data,labels=connection.get_data_pp(patients[1],3)
# #data,labels=read_data(lab,files,3,10,3000)#connection.get_data_1v()#read_data(lab,files,1,20,3000)
# print "original", data.shape
# p_data=[ np.transpose(i) for i in data]
# p_data=np.array(p_data)
# print "originaltransp",p_data.shape

# #print labels
# print len(labels)
# m=np.min(p_data)
# r=np.max(p_data)-m
# p_data= (np.abs(p_data)-m)/r
# print p_data
# print p_data.shape
#print labels

#np.savetxt(similarity_file, eros.eros(p_data).reshape((len(p_data), 1, len(p_data))))
#print 'eros finished'
# np.savetxt(aggregate_file, p_aggregated_values)
# np.savetxt(normed_aggregate_file, p_normed_aggregated_values)
# np.savetxt(order_file, range(1, len(visit_label) + 1))

# a list of annotations, each is associated with one data point
# annotations = [str(i + 1) + "_" + str(int(p_aggregated_values[i][0])) for i in range(len(chemo_label))]
# annotations = [str(int(p_aggregated_values[i][0])) for i in range(len(chemo_label))]

#mtsne using DTW distance metric
# distance_file="dist"
# dtw_square_distance_matrix = distance_metric.dtw_distance_matrix(p_data, distance_file + '_dtw', recompute=True)
# Y_2 = mtsne.distance_tsne(dtw_square_distance_matrix, 2)
# Y_3 = mtsne.distance_tsne(dtw_square_distance_matrix, 3)

# mtsne using Euclidean distance metric
# labels="s_euclidean_"
# eu_square_distance_matrix = distance_metric.eu_distance_matrix(p_data, distance_file, squared=True)
# tsne.tsne(eu_square_distance_matrix, labels, gfile, labels, 2)
# tsne_old.tsne_old(eu_square_distance_matrix, labels, gfile, labels, 3)

#tsne using EROS similarity
# similarity_matrix = np.loadtxt(similarity_file);
# print 'matrix loaded'
# #Y_2_d = mtsne.distance_tsne(similarity_matrix, 2) 
# Y_2_s = mtsne.similarity_tsne(similarity_matrix, 2) 
# print labels
#2 dimensional
# print Y_2
# print Y_2[:, 0]
# print Y_2[:, 1]

# print Y_2.shape 
# print 'y_2'
# Y_3 = mtsne.similarity_tsne(similarity_matrix, 3)     #3 dimensional
# print 'y_3'
# PCA
# Y_2 = pca.do_pca(p_normed_aggregated_values, 2)
# Y_3 = pca.do_pca(p_normed_aggregated_values, 3)       
#
#graph_plot.graf_with_scale(Y_2_d, labels,'s_3v_eros'+str(individuos))
# graph_plot.graf_with_scale(Y_2_s, labels,'s_3v_eros'+str(individuos))
# graph_plot.dump_graph(Y_3, labels,'dtw_3v_20'+str(individuos),labels,3)     #mtsne in 3-D space

def eross(patient):

    print "------patient------------",patient
    data,labels=connection.get_data_pp(patient,4)
    #data,labels=read_data(lab,files,3,10,3000)#connection.get_data_1v()#read_data(lab,files,1,20,3000)
    print "original", data.shape
    p_data=[ np.transpose(i) for i in data]
    p_data=np.array(p_data)
    print "originaltransp",p_data.shape

    np.savetxt(similarity_file, eros.eros(p_data).reshape((len(p_data), 1, len(p_data)))) 
    similarity_matrix = np.loadtxt(similarity_file)

    print  'matrix loaded' #Y_2_d = mtsne.distance_tsne(similarity_matrix, 2)  
    Y_2_s = mtsne.similarity_tsne(similarity_matrix, 2)  
    print labels
    #Y_3 = mtsne.similarity_tsne(similarity_matrix, 3)
    graph_plot.graf_with_scale('eros_4v_scaled'+patient,Y_2_s, labels)
    #graph_plot.dump_graph(Y_3, labels,'eros_4v_'+patient,labels,3)
    Y_2_s=[]
    p_data=[]
    labels=[]
    #graph_plot.dump_graph(Y_3, labels,'dtw_3v_20'+str(individuos),labels,3) 



def dtw(patient):
    print "-----DTW-patient------------",patient
    data,labels=connection.get_data_pp(patient,4)
    print "original", data.shape
    p_data=[ np.transpose(i) for i in data]
    p_data=np.array(p_data)
    print "originaltransp",p_data[0]
    print "originaltransp",p_data.shape

    distance_file="dist"
    dtw_square_distance_matrix = distance_metric.dtw_distance_matrix(p_data, distance_file + '_dtw', recompute=True)
    print  'matrix loaded'
    Y_2 = mtsne.distance_tsne(dtw_square_distance_matrix, 2)
    print labels
    #Y_3 = mtsne.similarity_tsne(similarity_matrix, 3)
    graph_plot.graf_with_scale('Ldtw_4v_'+patient,Y_2, labels)
    #graph_plot.dump_graph(Y_3, labels,'eros_4v_'+patient,labels,3)
    Y_2=[]
    p_data=[]
    labels=[]


#for i in patients:
#    eross(i)

for i in patientsfordtw:
    dtw(i)
