from classes.label import Label
class Cluster:
    def __init__(self):
        self.point_set = []

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
    def expand(self, neighbor_point, data_set, eps, minPts):
        for p in neighbor_point:
            if p.label == Label.VISITED:
                continue
            else:
                p.label = Label.VISITED
                self.point_append(p)
                p_neighbor = p.region_query(data_set, eps)
                if len(p_neighbor) >= minPts:
                    self.expand(p_neighbor, data_set, eps, minPts)


    def point_append(self, point):
        self.point_set.append(point)
        point.cluster = self
