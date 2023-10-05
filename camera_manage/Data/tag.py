import numpy as np
from camera_manage.Config.tag import SIGN_MAP, IDX_MAP, IDX_INV_MAP


class Tag(object):
    def __init__(self, info: str = '+x+y+z'):
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
            SIGN_MAP[self.info[2*i]] for i in range(3)
        ]
        self.idx_list = [
            IDX_MAP[self.info[2*i+1]] for i in range(3)
        ]

        return True

    def setInfo(self, info: str):
        self.info = info
        self.updateParams()
        return True

    def inv(self):
        inv_info_list = ['+', 'x', '+', 'y', '+', 'z']
        for i in range(3):
            if abs(self.sign_list[i] - 1.0) < abs(self.sign_list[i] + 1.0):
                inv_info_list[2 * self.idx_list[i]] = '+'
            else:
                inv_info_list[2 * self.idx_list[i]] = '-'
            inv_info_list[2 * self.idx_list[i] + 1] = IDX_INV_MAP[str(i)]

        inv_info = ''
        for i in range(6):
            inv_info += inv_info_list[i]
        return Tag(inv_info)

    def dot(self, last_tag):
        new_sign_list = [
            self.sign_list[i] * last_tag.sign_list[self.idx_list[i]]
            for i in range(3)
        ]
        new_idx_list = [
            last_tag.idx_list[self.idx_list[i]] for i in range(3)
        ]

        new_info = ''
        for i in range(3):
            sign = new_sign_list[i]
            if abs(sign - 1.0) < abs(sign + 1.0):
                new_info += '+'
            else:
                new_info += '-'

            new_info += IDX_INV_MAP[str(new_idx_list[i])]

        return Tag(new_info)

    def getMatrix(self):
        matrix = np.zeros((3, 3), dtype=float)

        for i in range(3):
            matrix[i, self.idx_list[i]] = self.sign_list[i]
        return matrix
