from classes.label import Label


class Cluster:
    def __init__(self):
        self.point_set = []

    def expand(self, neighbor_point, data_set, eps, minPts):
        for p in neighbor_point:
            if p.label == Label.VISITED:
                continue
            else:
                # set object's label to visited
                p.label = Label.VISITED

                # append object to self point_set
                self.point_append(p)

                # find neighbor objects
                p_neighbor = p.region_query(data_set, eps)

                if len(p_neighbor) >= minPts:
                    # recursive call
                    self.expand(p_neighbor, data_set, eps, minPts)

    def point_append(self, point):
        self.point_set.append(point)
        point.cluster = self
