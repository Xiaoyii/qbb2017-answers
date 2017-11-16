#!/usr/bin/env python


"""

"""

import sys
import math
import itertools
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hac
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
from sklearn.cluster import KMeans


# a = pd.read_csv(sys.argv[1], sep = "\t", index_col = 0)
# print a

infile = open(sys.argv[1],'r')
#save the column/row headers (conditions/genes) into an array
colHeaders = infile.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

for line in infile:
	data = line.strip().split('\t')
	rowHeaders.append(data[0])
	dataMatrix.append([float(x) for x in data[1:]])

#convert native data array into a numpy array
dataMatrixnp = np.array(dataMatrix) 
# print dataMatrixnp

linkageMatrix = hac.linkage(dataMatrixnp, method = "average")
heatmapOrder = hac.leaves_list(linkageMatrix)

linkageMatrix_transposed = hac.linkage(dataMatrixnp.T, method = "average")
heatmapOrder_transposed = hac.leaves_list(linkageMatrix_transposed)

orderedDataMatrix = dataMatrixnp[heatmapOrder,:][:, heatmapOrder_transposed]
# rowHeaders = np.array(rowHeaders)
# orderedRowHeaders = rowHeaders[heatmapOrder,:]
labels = np.array(['CFU', 'poly', 'unk', 'int', 'mys', 'mid'])
labels_t = labels[ heatmapOrder_transposed]
plt.figure()
plt.imshow(orderedDataMatrix, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], labels_t) 
plt.savefig("week10_heatmap.png") # Save the image
plt.close()


plt.figure()
hac.dendrogram(linkageMatrix_transposed, labels=labels )
plt.savefig( 'dendrogram10.png' )
plt.close()


kmeans = KMeans( n_clusters=5, random_state=0 )
kmeans.fit( dataMatrixnp )
labels = kmeans.predict( dataMatrixnp )
dataMatrix_df = pd.merge( pd.DataFrame(dataMatrixnp, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = dataMatrix_df.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("Heatmap of Iris characteristics")
plt.colorbar()
plt.xticks( [ x for x in range(6) ], labels_t) 
plt.savefig("week10_k_clustered.png") # Save the image
plt.close()



# def main():
#     data_df = pd.read_csv(sys.argv[1], sep = "\t" )
#     labels = [ 'CFU', 'poly', 'unk', 'int', 'mys', 'mid' ]
#     data_df_oi = data_df[ labels ]
#     plot_dendrogram( linkageMatrix_transposed, labels, 'dendrogram.png')
#     k_transformed, k_labels = k_means_clustering( data_df_oi )
#     k_transformed = k_transformed[ :, heatmapOrder_transposed ]
#     plot_heatmap( 'k-means clustered gene expression, k=5', labels_tr, k_tranformed, 'k_means_heatmap.png' )
#
# main()





# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target
# labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width",]
# species = ["Setosa", "Versicolour", "Virginica"]
#
# #============================================================#
# # CREATE SOME PLOTS
#
# # Start by normalizing the data so each feature can fit on the
# ##same scale. Basically we are calculating the Z-score for
# ##each value based on only the feature it belongs to.
# X = (X-np.average(X,axis=0))/np.std(X,axis=0)
#
# # Pull out the value with the greatest magnitude, to set the
# ##scale
# m = np.max(np.abs(X))
#
# # Make the actual plot
# plt.figure()                                 # Open a blank canvas
# plt.title("Heatmap of Iris characteristics") # Add a title to the top
# plt.imshow(                                  # Treat the values like pixel intensities in a picture
#     X,                                       # ... Using X as the values
#     aspect='auto',                           # ... 'Stretch' the image to fit the canvas, so you don't get a skinny strip that is 4x150 pixels
#     interpolation='nearest',                 # ... Don't use any blending between pixel values
#     cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
#     vmin=-1*m,                               # ... Set the lowest value to show on the scale
#     vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
#     )
# plt.grid(False)        # Turn of the grid lines (a feature added automatically by ggplot)
# plt.xticks(            # Edit the xticks being shown
#     range(X.shape[1]), # ... use the values centered on each column of pixels
#     labels,            # ... which corresponds to the indices of our labels
#     rotation=50,       # ... and rotate the labels 50 degrees counter-clockwise
#     )
# plt.yticks([])         # Edit the ticks on the y-axis to show....NOTHING
# plt.colorbar()         # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values
#
# plt.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
#     left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
#     bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
#     right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
#     top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
# )
#
# plt.savefig("clean_heatmap.png") # Save the image
# plt.close() # Close the canvas













