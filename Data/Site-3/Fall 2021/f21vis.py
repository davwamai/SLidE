import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import laspy
import json

file_path = './laz/terryF21_S3_groundex.laz'

with laspy.open(file_path) as file:
    las = file.read()

x = las.x
y = las.y
z = las.z

mesh_x, mesh_y = np.meshgrid(x, y)



