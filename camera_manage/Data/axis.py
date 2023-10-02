import numpy as np
from scipy.spatial.transform import Rotation as R

from camera_manage.Method.transform import getAxisTransformMatrix

class Axis(object):
    def __init__(self, axis_tag='+x+y+z', pos=[0, 0, 0], quat=[0, 0, 0, 1]) -> None:
        '''
        axis_tag: target axis order on world axis when pos and quat is set to I
        pos: axis center pos in world, xyz-order
        quat: axis face-forward direction in world, xyzw-order
        '''
        self.axis_tag=axis_tag
        self.pos = np.array(pos, dtype=float)
        self.quat = np.array(quat, dtype=float)

        self.transform_matrix = np.identity(3, dtype=float)

        self.updateTransformMatrix()
        return

    def updateTransformMatrix(self):
        self.transform_matrix = np.diag([1, 1, 1]).astype(float)

        axis_transform_matrix = getAxisTransformMatrix(self.axis_tag)
        self.transform_matrix = axis_transform_matrix.dot(self.transform_matrix)

        rotate_matrix = R.from_quat([
            self.quat[1], self.quat[2], self.quat[3], self.quat[0]
        ]).as_matrix()
        self.transform_matrix = rotate_matrix.dot(self.transform_matrix)
        return True

    def rotateAxis(self, delta_quat):
        rotate_matrix = R.from_quat([
            self.quat[1], self.quat[2], self.quat[3], self.quat[0]
        ]).as_matrix()
        delta_rotate_matrix = R.from_quat([
            delta_quat[1], delta_quat[2], delta_quat[3], delta_quat[0]
        ]).as_matrix()
        new_rotate_matrix = delta_rotate_matrix.dot(rotate_matrix)

        self.quat = R.from_matrix(new_rotate_matrix).as_quat()

        self.updateTransformMatrix()
        return True

    def translateAxis(self, delta_pos):
        self.pos += np.array(delta_pos, dtype=float)
        return True

    def getRTMatrix(self):
        rt_matrix = np.zeros((4, 4), dtype=float)
        rt_matrix[:3, :3] = self.transform_matrix
        rt_matrix[:3, 3] = self.pos
        rt_matrix[3, 3] = 1.0
        return rt_matrix
