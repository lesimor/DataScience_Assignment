# -*- encoding: utf-8 -*-
from classes.point import Point
from classes.cluster import Cluster
from classes.label import Label
import sys  # 프로그램 실행 시 인자를 전달받기 위함

f = open("./data/input3.txt")


point_set = []

for line in f:
    point_info = f.readline().split()
    _id, _x, _y = point_info[0], point_info[1], point_info[2]
    point_set.append(Point(_x, _y))

print(len(point_set))
# x축 위치 기준으로 정렬.
point_set.sort(key=lambda p: p.x)

# for point in point_set:
#     print(point.x)

eps = 5
minPts = 5
#
# target = point_set[800]
#
# nearby = target.region_query(point_set, 10)
#
# print("X: ", target.x, "Y: ", target.y)
# print("nearby")
# for point in nearby:
#     print("X: ", point.x, "Y: ", point.y)


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

print(len(cluster_set))


#
# 의사 코드
# DBSCAN(D, eps, MinPts) {
#    C = 0
#    for each point P in dataset D {
#       if P is visited
#          continue next point
#       mark P as visited
#       NeighborPts = regionQuery(P, eps)
#       if sizeof(NeighborPts) < MinPts
#          mark P as NOISE
#       else {
#          C = next cluster
#          expandCluster(P, NeighborPts, C, eps, MinPts)
#       }
#    }
# }
#
# expandCluster(P, NeighborPts, C, eps, MinPts) {
#    add P to cluster C
#    for each point P' in NeighborPts {
#       if P' is not visited {
#          mark P' as visited
#          NeighborPts' = regionQuery(P', eps)
#          if sizeof(NeighborPts') >= MinPts
#             NeighborPts = NeighborPts joined with NeighborPts'
#       }
#       if P' is not yet member of any cluster
#          add P' to cluster C
#    }
# }
#
# regionQuery(P, eps)
#    return all points within P's eps-neighborhood (including P)
