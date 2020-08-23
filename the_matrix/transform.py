import math

from resources.vec import Vec
from resources.mat import Mat
from resources.matutil import rowdict2mat

homo_set = {'x', 'y', 'u'}
spc_D = (homo_set, homo_set)
rgb_set = {'r', 'g', 'b'}
color_D = (rgb_set, rgb_set)

def degree2rad(degree):
    return degree * math.pi / 180

def translation(alpha, beta):
    return Mat(spc_D, {('x','x'):1, ('x','u'):alpha,
                       ('y','y'):1, ('y','u'):beta,
                       ('u','u'):1})

def scale(alpha, beta):
    return Mat(spc_D, {('x','x'):alpha, ('y','y'):beta, ('u','u'):1})

def rotation(theta):
    return Mat(spc_D, {('x','x'):math.cos(theta), ('x','y'):-math.sin(theta),
                       ('y','x'):math.sin(theta), ('y','y'):math.cos(theta),
                       ('u','u'):1})

def rotation_about(theta, x, y):
    return translation(x,y)*rotation(theta)*translation(-x,-y)

def reflect_x():
    return Mat(spc_D, {('x','x'):1, ('y','y'):-1, ('u','u'):1})

def reflect_y():
    return Mat(spc_D, {('x','x'):-1, ('y','y'):1, ('u','u'):1})

def reflect_about(x1, y1, x2, y2):
    assert (x1, y1) != (x2, y2)
    x, y = (x2-x1), (y2-y1)
    theta = math.atan2(y, x)
    return translation(x1, y1)*rotation(theta)*reflect_x()*rotation(-theta)*translation(-x1, -y1)

def scale_color(r_scl, g_scl, b_scl):
    return Mat(color_D, {('r','r'):r_scl, ('g','g'):g_scl, ('b','b'):b_scl})

def grayscale():
    row = Vec(rgb_set, {'r':77/256, 'g':151/256, 'b':28/256})
    return rowdict2mat({i:row for i in range(3)})
