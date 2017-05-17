from classes.cluster import Cluster
from classes.label import Label


def db_scan(data_set, eps, minPts):
    # initialize returning cluster_set
    cluster_set = []

    # iterate through whole data set
    for point in data_set:
        if point.label == Label.UNVISITED:
            # get neighbor points including self
            neighbor_points = point.region_query(data_set, eps)

            # if number of neighbor points belows minPts
            if len(neighbor_points) < minPts:
                point.label = Label.NOISE
            else:
                # create new cluster
                c = Cluster()
                c.expand(neighbor_points, data_set, eps, minPts)
                cluster_set.append(c)
    return cluster_set
