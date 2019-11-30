__author__ = 'minh'

from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import gif
from collections import OrderedDict
import math
segments_per_file={'SC4001E0': 5226000, 'SC4002E0': 5595000, 'SC4011E0': 4423688, 'SC4012E0': 5019344, 'SC4021E0': 4902000, 'SC4022E0': 4457110, 'SC4031E0': 5109000, 'SC4032E0': 4845035, 'SC4041E0': 4686000, 'SC4042E0': 5286744, 'SC4051E0': 5523000, 'SC4052E0': 6159576, 'SC4061E0': 4926000, 'SC4062E0': 5229000, 'SC4071E0': 5215914, 'SC4072E0': 5172805, 'SC4081E0': 5014464, 'SC4082E0': 4879797, 'SC4091E0': 5200660, 'SC4092E0': 5638438, 'SC4101E0': 4929420, 'SC4102E0': 5424000, 'SC4111E0': 5220000, 'SC4112E0': 5393385, 'SC4121E0': 5762271, 'SC4122E0': 5703000, 'SC4131E0': 5598000, 'SC4141E0': 5166000, 'SC4142E0': 5136642, 'SC4151E0': 5190000, 'SC4152E0': 5912306, 'SC4161E0': 5301000, 'SC4162E0': 5805000, 'SC4171E0': 5229000, 'SC4172E0': 5671163, 'SC4181E0': 5151000, 'SC4182E0': 5238000, 'SC4191E0': 6974046, 'SC4192E0': 7284000, 'ST7011J0': 3579693, 'ST7022J0': 3072667, 'ST7041J0': 2870100, 'ST7052J0': 3075744, 'ST7061J0': 3253617, 'ST7071J0': 2628384, 'ST7082J0': 2589080, 'ST7092J0': 2566290, 'ST7101J0': 3289674, 'ST7112J0': 3063350, 'ST7121J0': 3115962, 'ST7132J0': 2687934, 'ST7141J0': 2738565, 'ST7151J0': 3833649, 'ST7162J0': 2857148, 'ST7171J0': 2585590, 'ST7182J0': 3221262, 'ST7192J0': 3020340, 'ST7201J0': 2908373, 'ST7212J0': 2779440, 'ST7221J0': 3094300, 'ST7241J0': 3257232}
for key, value in segments_per_file.items():
    nv=[]
    temp=(value*1.0)/360000.0
    salto=temp/8
    #print key,temp
    i=salto
    while i<(temp):
      
      nv.append(round(i,1))
      i=i+salto
    #a=[i+salto for i in range(0,int(temp)-int(math.ceil(salto)))]
    segments_per_file[key] = nv
    a=[]

color_list = ['r', 'y', '#fdb462', 'b','m','c', 'k','g']
marker_list = ['o','v', '8', 'D', 's', '^', '<', '>', 'p', '*', 'h', 'H', 'd']

"""
gen markers/colors depends on the labels and the marker_list/color_list
"""
def gen_markers_colors(labels, marker_color_list):
    distinct_markers = marker_color_list[0:len(labels) + 1]

    # create a mapping from label to color
    label_to_color = dict(zip(set(labels), distinct_markers))

    # generate colors corresponding to labels
    markers = []
    for label in labels:
        markers.append(label_to_color[label])
    return markers


def graf_with_scale(pat,title,Y, labels):  
    xx=Y[:, 0]
    yy=Y[:, 1]
    markers = gen_markers_colors(labels, marker_list)
    cant=len(xx)
    print "--*-*-*-**-*",cant
    fig = plt.figure()
    cmp = plt.cm.get_cmap('gnuplot2', cant)
    ax1=fig.gca()
    c = np.arange(1, cant + 1)
    #print c
    dummie_cax = ax1.scatter(c, c, c=c, cmap=cmp)
    ax1.cla()
    #print markers
  
    #ax1=fig.gca()
    i=0
    for _s,  _x, _y,l in zip(markers, xx, yy,labels):
        c=cmp(i)
        ax1.scatter(_x, _y,alpha=0.60,s=90, marker=_s, c=c,label=l)
        i+=1
    #ax.scatter(xx, yy, s=40,edgecolors='none',c=xx, cmap=cmp)# , marker=markers)

    cbar=plt.colorbar(dummie_cax)

    cbar.ax.set_ylabel('Time', rotation=270)
    cbar.ax.set_yticklabels(segments_per_file[pat])
    #cbar.set_ticks(c)
    #cbar.set_ticks(labels)

    #plt.legend(loc=2)
    handles, labelss = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labelss, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.title(title)
    plt.show()
    fig.savefig(title+'.png') 
    plt.close(fig)




"""
output: a graph visualizing data points
"""
def dump_graph(Y, labels, output_graph, annotations = None, d=2):

    # generate a random color corresponding to each label
    colors = gen_markers_colors(labels, color_list)
    markers = gen_markers_colors(labels, marker_list)
    #print colors,markers

    fig = plt.figure(figsize=(12,8))
    if d == 3:
        ax = fig.gca(projection='3d')
        # ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.gca()

    scats, anots = [], []
    for (i, cla) in enumerate(set(labels)):
        xc = [p for (j, p) in enumerate(Y[:, 0]) if labels[j] == cla]
        yc = [p for (j, p) in enumerate(Y[:, 1]) if labels[j] == cla]
        if d == 3:
            zc = [p for (j, p) in enumerate(Y[:, 2]) if labels[j] == cla]

        if annotations is not None:
            ac = [annotations[j] for (j, _) in enumerate(Y[:, 0]) if labels[j] == cla]

        cols = [c for (j, c) in enumerate(colors) if labels[j] == cla]
        mars = [m for (j, m) in enumerate(markers) if labels[j] == cla]

        # ax.set_xlabel('PC1')
        # ax.set_ylabel('PC2')
        ax.set_xlabel('Latent space')
        ax.set_ylabel('Latent space')
        scat = None
        if d == 2:
            scat = ax.scatter(xc, yc, s=40, marker=mars[0],edgecolors='none', c=cols, label=cla)

            #scat = ax.scatter(xc, yc, s=40)
        elif d == 3:
            scat = ax.scatter(xc, yc, zc, s=40, marker=mars[0], c=cols,edgecolors='none', label=cla, depthshade=False)
            #scat = ax.scatter(xc, yc, zc, s=40, depthshade=False)
            ax.set_zlabel('Latent space')

        # add anotations to each data point
        # if annotations is not None:
        #     for j in range(len(xc)):
        #         anot = None
        #         if d == 2:
        #             anot = ax.annotate(ac[j], (xc[j], yc[j]), fontsize=10.5, xytext=(2, 6),
        #                      ha='right', textcoords='offset points')
        #         elif d == 3:
        #             anot = ax.text(xc[j], yc[j], zc[j], ac[j]) #,  fontsize=8, xytext=(2, 5), ha='right', textcoords='offset points')
        #         anots.append(anot)
        # scats.append(scat)

    # fig.suptitle('PCA', fontsize=14)
    # ax.legend(scatterpoints=1, loc=1, fontsize=12)
    handles, labelss = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labelss, handles))
    plt.legend(by_label.values(), by_label.keys(),loc=2)
    plt.title(output_graph)
    if d == 3:
        angles = np.linspace(90, 450, 30)[:-1]  # Take 30 angles between 0 and 360
        # create an animated gif (100ms between frames)
        plt.show();
        gif.rotanimate(ax, angles,'graficas/'+ output_graph+".gif", delay=100)

    if d==2:
        plt.show();
        fig.savefig('graficas/'+output_graph+'.png')

	for scat in scats:
		scat.remove()
    for anot in anots:
    	anot.remove()

