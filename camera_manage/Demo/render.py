from camera_manage.Method.render import renderImagePose

def demo():
    dataset_folder_path = '../colmap-manage/output/NeRF_3vjia_simple/gs/'

    renderImagePose(dataset_folder_path)
    return True
