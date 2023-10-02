from wis3d import Wis3D

from camera_manage.Data.axis import Axis

axis_tag = '+x+z-y'
pos = [0, 0, 0]
quat = [0, 0, 0, 1]

axis = Axis(axis_tag, pos, quat)

wis3d = Wis3D('./output/axis/', 'axis', xyz_pattern=('x', 'y', 'z'))

wis3d.add_camera_pose(axis.getRTMatrix(), name="camera_pose_0")
