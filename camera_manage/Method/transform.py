import numpy as np

def getAxisTransformMatrix(axis_tag='+x+z-y'):
    sign_map = {
        '+': 1.0,
        '-': -1.0,
    }
    axis_idx_map = {
        'x': 0,
        'y': 1,
        'z': 2,
    }

    x_sign = sign_map[axis_tag[0]]
    y_sign = sign_map[axis_tag[2]]
    z_sign = sign_map[axis_tag[4]]

    x_idx = axis_idx_map[axis_tag[1]]
    y_idx = axis_idx_map[axis_tag[3]]
    z_idx = axis_idx_map[axis_tag[5]]

    transform_matrix = np.zeros((3, 3), dtype=float)

    transform_matrix[0, x_idx] = x_sign
    transform_matrix[1, y_idx] = y_sign
    transform_matrix[2, z_idx] = z_sign

    return transform_matrix
