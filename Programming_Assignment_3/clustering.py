# -*- encoding: utf-8 -*-
from classes.point import Point
from classes.cluster import Cluster
from classes.label import Label
import sys  # 프로그램 실행 시 인자를 전달받기 위함
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.cm as cm

input_file_name = sys.argv[1]
cluster_number = int(sys.argv[2])
eps_number = int(sys.argv[3])
minPts_number = int(sys.argv[4])

print(input_file_name, cluster_number, eps_number, minPts_number)

f = open("./data/" + input_file_name)

point_set = []

for line in f:
    point_info = f.readline().split()
    _id, _x, _y = point_info[0], point_info[1], point_info[2]
    point_set.append(Point(_id, _x, _y))

# file close
f.close()

print(len(point_set))
# x축 위치 기준으로 정렬.
point_set.sort(key=lambda p: p.x)

# for point in point_set:
#     print(point.x)

eps = eps_number
minPts = minPts_number


def db_scan(dataset, eps, minPts):
    cluster_set = []
    for point in dataset:
        if point.label == Label.VISITED:
            continue
        # point.label = Label.VISITED
        neighbor_points = point.region_query(dataset, eps)
        if len(neighbor_points) < minPts:
            point.label = Label.NOISE
        else:
            # 새로운 클러스터 생성.
            c = Cluster()
            c.expand(neighbor_points, dataset, eps, minPts)
            cluster_set.append(c)
    return cluster_set


cluster_set = db_scan(point_set, eps, minPts)

colors = cm.rainbow(np.linspace(0, 1, len(cluster_set)))

cluster_idx = 0
for cluster, c in zip(cluster_set, colors):
    x_array = []
    y_array = []
    output_file_name = "./data/" + input_file_name.split(".")[0] + "_cluster_" + str(cluster_idx) + ".txt"
    print(output_file_name + "생성")
    output_file = open(output_file_name, 'w')
    for point in cluster.point_set:
        x_array.append(point.x)
        y_array.append(point.y)
        output_file.write(str(point.id) + "\n")

    x_numpy = np.array(x_array)
    y_numpy = np.array(y_array)
    plt.scatter(x_numpy, y_numpy, color=c)
    cluster_idx += 1
plt.show()

