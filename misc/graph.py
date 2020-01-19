import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from process_lines import facts
import pylab

G=nx.Graph()
plt.figure(num='Expert System')
nodelist = G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,
                             10,11,12,13,14,15,16,
                             17,18,19,20,21,22,23,
                             24,25])

facts_list = []
facts_list = [facts["A"], facts["B"], facts["C"], facts["D"], facts["E"], facts["F"],
              facts["G"], facts["H"], facts["I"], facts["J"], facts["K"],
              facts["L"], facts["M"], facts["N"], facts["O"], facts["P"], facts["Q"],
              facts["R"], facts["S"], facts["T"], facts["U"], facts["V"], facts["W"],
              facts["X"],facts["Y"],facts["Z"]
              ]

pos={0:(0,0),1:(0,2),2:(0,4),3:(0,6),4:(0,8),
     5:(0,10),6:(0,12),7:(0,14),8:(0,16),9:(0,18),10:(0,20),
     11:(0,22),12:(0,24),13:(0,26),14:(0,28),15:(0,30),
     16:(0,32),17:(0,34),18:(0,36),19:(0,38),20:(0,40),
     21:(0,42),22:(0,44),23:(0,46),24:(0,48),25:(0,50)}

color_map = []
for node in facts_list:
    if node == False:
        color_map.append('red')
    else:
        color_map.append('green')
        
print(color_map)

nx.draw_networkx_nodes(G,pos,
                       nodelist,
                       node_color=color_map,
                       node_size=500,
                       alpha=0.8)
# print(facts)
# print(facts_list)

labels={}
labels[0]=r'$A$'
labels[1]=r'$B$'
labels[2]=r'$C$'
labels[3]=r'$D$'
labels[4]=r'$E$'
labels[5]=r'$F$'
labels[6]=r'$G$'
labels[7]=r'$H$'
labels[8]=r'$I$'
labels[9]=r'$J$'
labels[10]=r'$K$'
labels[11]=r'$L$'
labels[12]=r'$M$'
labels[13]=r'$N$'
labels[14]=r'$O$'
labels[15]=r'$P$'
labels[16]=r'$Q$'
labels[17]=r'$R$'
labels[18]=r'$S$'
labels[19]=r'$T$'
labels[20]=r'$U$'
labels[21]=r'$V$'
labels[22]=r'$W$'
labels[23]=r'$X$'
labels[24]=r'$Y$'
labels[25]=r'$Z$'

plt.savefig("graph.png")
red_patch = mpatches.Patch(color='red', label='False')
grn_patch = mpatches.Patch(color='green', label='True ')
plt.legend(handles=[red_patch, grn_patch])
nx.draw_networkx_labels(G,pos,labels,font_size=10)
plt.axis('off')
plt.show()