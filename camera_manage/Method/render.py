import numpy as np
from wis3d import Wis3D

from camera_manage.Method.colmap.scene import readColmapSceneInfo

def renderImagePose(dataset_folder_path, mesh_file_path=None):
    scene_info = readColmapSceneInfo(dataset_folder_path, 'images', False)

    dataset_name = dataset_folder_path.split('/')[-3]

    wis3d = Wis3D('./output/' + dataset_name + '/', dataset_name, xyz_pattern=('x', 'y', 'z'))
    wis3d.add_point_cloud(scene_info.point_cloud.points,
                          scene_info.point_cloud.colors,
                          name='pointcloud')

    if mesh_file_path is not None:
        wis3d.add_mesh(mesh_file_path, name='mesh')

    for i, train_camera in enumerate(scene_info.train_cameras):
        image_matrix = np.zeros((4, 4), dtype=float)
        image_matrix[:3, :3] = train_camera.R.transpose()
        image_matrix[:3, 3] = - train_camera.R.transpose().dot(train_camera.T)
        image_matrix[3, 3] = 1.0

        wis3d.add_camera_pose(image_matrix, name="camera_pose_" + str(i))
    return True
