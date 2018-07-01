import numpy as np

import preprocess
import eros
import distance_metric
import pca
import mtsne
import graph_plot

#GENERACIÓN DE DATOS SINTETICOS EN MEMORIA

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




individuos=50
similarity_file='similarity_eros_'+str(individuos)


p_data,labels= sintetica(4,individuos,3000)
print labels

np.savetxt(similarity_file, eros.eros(p_data).reshape((len(p_data), 1, len(p_data))))
print 'eros finished'
# np.savetxt(aggregate_file, p_aggregated_values)
# np.savetxt(normed_aggregate_file, p_normed_aggregated_values)
# np.savetxt(order_file, range(1, len(visit_label) + 1))

# a list of annotations, each is associated with one data point
# annotations = [str(i + 1) + "_" + str(int(p_aggregated_values[i][0])) for i in range(len(chemo_label))]
# annotations = [str(int(p_aggregated_values[i][0])) for i in range(len(chemo_label))]

# mtsne using DTW distance metric
# dtw_square_distance_matrix = distance_metric.dtw_distance_matrix(p_data, distance_file + '_dtw', recompute=True)
# Y_2 = mtsne.mtsne(dtw_square_distance_matrix, 2)
# Y_3 = mtsne.mtsne(dtw_square_distance_matrix, 3)

# mtsne using Euclidean distance metric
# eu_square_distance_matrix = eu_distance_matrix(p_data, distance_file, squared=True)
# tsne.tsne(eu_square_distance_matrix, chemo_label, graph_chemo_file, annotations, 2)
# tsne_old.tsne_old(eu_square_distance_matrix, chemo_label, graph_chemo_file, None, 3)

# tsne using EROS similarity
similarity_matrix = np.loadtxt(similarity_file);
print 'matrix loaded'
Y_2 = mtsne.mtsne(similarity_matrix, 2)     #2 dimensional
print 'y_2'
Y_3 = mtsne.mtsne(similarity_matrix, 3)     #3 dimensional
print 'y_3'
# PCA
# Y_2 = pca.do_pca(p_normed_aggregated_values, 2)
# Y_3 = pca.do_pca(p_normed_aggregated_values, 3)
#
graph_plot.dump_graph(Y_2, labels,'graph3d_'+str(individuos),labels,2)
graph_plot.dump_graph(Y_3, labels,'graph3d_'+str(individuos),labels,3)     #mtsne in 3-D space