from camera_manage.Method.render import renderImagePose

def demo():
    dataset_folder_path = '../colmap-manage/output/NeRF_3vjia_simple/gs/'

    dataset_folder_path = '../habitat-sim-manage/output/scene0474_02_vh_clean/'
    mesh_file_path = '/home/chli/chLi/Dataset/ScanNet/scans/scene0474_02/scene0474_02_vh_clean.ply'

    renderImagePose(dataset_folder_path, mesh_file_path)
    return True
