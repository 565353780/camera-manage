import numpy as np
from camera_manage.Config.tag import SIGN_MAP, IDX_MAP


class Tag(object):
    def __init__(self, info='+x+y+z'):
        '''
        info: descript the axis direction of world axis
        '''
        self.info = info

        self.sign_list = [1, 1, 1]
        self.idx_list = [0, 1, 2]

        self.updateParams()
        return

    def reset(self):
        self.info = '+x+y+z'

        self.sign_list = [1, 1, 1]
        self.idx_list = [0, 1, 2]
        return True

    def updateParams(self):
        self.sign_list = [
            SIGN_MAP[self.info[2 * i]] for i in range(3)
        ]
        self.idx_list = [
            IDX_MAP[self.info[2*i+1]] for i in range(3)
        ]

        return True

    def setInfo(self, info):
        self.info
        self.updateParams()
        return True

    def getMatrix(self):
        matrix = np.zeros((3, 3), dtype=float)

        for i in range(3):
            matrix[i, self.idx_list[i]] = self.sign_list[i]
        return matrix
