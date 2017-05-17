# -*- encoding: utf-8 -*-
from classes.point import Point
from modules.db_scan import db_scan
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# file name
input_file_name = sys.argv[1]

# number of cluster
cluster_number = int(sys.argv[2])

# eps
eps_number = float(sys.argv[3])

# minPts
minPts_number = int(sys.argv[4])

# file open by file name input
f = open("./data/" + input_file_name)

# point_set initialize
point_set = []

# get object information from file
for line in f:
    point_info = f.readline().split()
    _id, _x, _y = point_info[0], point_info[1], point_info[2]
    point_set.append(Point(_id, _x, _y))

# file close
f.close()

cluster_set = db_scan(point_set, eps_number, minPts_number)

# sort by element(cluster)'s point_set length ascend
cluster_set.sort(key=lambda x: len(x.point_set))
# remove element
del cluster_set[:-cluster_number]

# using matplotlib for visualizing
colors = cm.rainbow(np.linspace(0, 1, len(cluster_set)))

# cluster index initialize
cluster_idx = 0
for cluster, c in zip(cluster_set, colors):
    x_array = []
    y_array = []

    # output file name setting
    output_file_name = "./data/" + input_file_name.split(".")[0] + "_cluster_" + str(cluster_idx) + ".txt"

    # output file open with name
    output_file = open(output_file_name, 'w')

    # iterate on cluster's point_set
    for point in cluster.point_set:
        x_array.append(point.x)
        y_array.append(point.y)

        # print cluster point set element's id on file
        output_file.write(str(point.id) + "\n")

    # convert normal array to numpy array
    x_numpy = np.array(x_array)
    y_numpy = np.array(y_array)

    # print dot on scatter chart
    plt.scatter(x_numpy, y_numpy, color=c)

    # increment cluster index
    cluster_idx += 1

# show scatter chart
plt.show()

