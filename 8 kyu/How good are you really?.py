from functools import reduce
def better_than_average(class_points, your_points):
    class_points.append(your_points)
    x = reduce(lambda a, b: a + b, class_points) / len(class_points)
    return x < your_points
