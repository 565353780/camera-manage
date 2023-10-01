import numpy as np
from wis3d import Wis3D

from camera_manage.Method.colmap.scene import readColmapSceneInfo

def renderImagePose(dataset_folder_path):
    scene_info = readColmapSceneInfo(dataset_folder_path, 'images', False)

    wis3d = Wis3D("./output/test1/", 'test1', xyz_pattern=('x', 'y', 'z'))
    wis3d.add_point_cloud(scene_info.point_cloud.points,
                          scene_info.point_cloud.colors,
                          name='pointcloud')

    for i, train_camera in enumerate(scene_info.train_cameras):
        image_matrix = np.zeros((4, 4), dtype=float)
        image_matrix[:3, :3] = train_camera.R.transpose()
        image_matrix[:3, 3] = - train_camera.R.transpose().dot(train_camera.T)
        image_matrix[3, 3] = 1.0

        wis3d.add_camera_pose(image_matrix, name="camera_pose_" + str(i))
    return True
