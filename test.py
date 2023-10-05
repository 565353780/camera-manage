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

tag = axis_1.tag.dot(axis_2.tag)
print('tag 1 dot tag 2 =')
print(tag.info)

print('tag 1:')
print(axis_1.tag.info)
print('tag 1 inv:')
print(axis_1.tag.inv().info)
print('tag 2:')
print(axis_2.tag.info)
print('tag 2 inv:')
print(axis_2.tag.inv().info)

exit()

wis3d = Wis3D('./output/axis/', 'axis', xyz_pattern=('x', 'y', 'z'))

wis3d.add_camera_pose(axis.getRTMatrix(), name="camera_pose_0")
