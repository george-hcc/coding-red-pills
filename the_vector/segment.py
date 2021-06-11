from resources.plotting import plot

def segment2(pt1, pt2, nof_points):
    rng = [x/(nof_points-1) for x in range(nof_points)]
    pt1_arr = [[a*pt1[0], a*pt1[1]] for a in rng]
    pt2_arr = [[b*pt2[0], b*pt2[1]] for b in reversed(rng)]
    return [[pt1[0]+pt2[0], pt1[1]+pt2[1]] for (pt1, pt2) in zip(pt1_arr, pt2_arr)]
