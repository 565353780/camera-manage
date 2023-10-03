from wis3d import Wis3D

from camera_manage.Data.axis import Axis

tag_info = '+x-z+y'
pos = [0, 0, 0]
quat = [0, 0, 0, 1]

axis_1 = Axis(tag_info, pos, quat)

tag_info = '+x-z+y'
pos = [0, 0, 0]
quat = [0, 0, 0, 1]

axis_2 = Axis(tag_info, pos, quat)

print('start dot tag')
tag = axis_1.tag.dot(axis_2.tag)
print('finish dot tag')
print(tag.info)

exit()

wis3d = Wis3D('./output/axis/', 'axis', xyz_pattern=('x', 'y', 'z'))

wis3d.add_camera_pose(axis.getRTMatrix(), name="camera_pose_0")
