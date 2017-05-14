from .label import Label


class Point:
    def __init__(self, _x, _y):
        # x position
        self.x = float(_x)

        # y position
        self.y = float(_y)

        # label
        self.label = Label.UNVISITED

        # assigned cluster
        self.cluster = None

    # search nearby points within eps
    def region_query(self, data_set, eps):
        # return set initialize
        neighbor_points = []

        # check each point in dataset
        for point in data_set:

            # if x or y position differences is larger than eps then pass
            if abs(self.x - point.x) > eps or abs(self.y - point.y) > eps:
                continue
            else:
                # calculate euclidean distance
                x_square = (self.x - point.x) ** 2
                y_square = (self.y - point.y) ** 2

                if (x_square + y_square) ** 0.5 <= eps:
                    neighbor_points.append(point)
        return neighbor_points
