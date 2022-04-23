from pathlib import Path
import numpy as np
import os
import xarray as xr
from drd.datasets.download_utils import download_file_from_google_drive, extract_archive, get_data_home
from drd.datasets.utils import load_numpy_from_raw, create_xarray_from_numpy

DATASET_METADATA = {
    "project_archive_url": "https://drive.google.com/file/d/1O_CCcoMxqdC6ebDOL-2DCM7jM__FHQEd/view?usp=sharing",
    "drive_id": "1O_CCcoMxqdC6ebDOL-2DCM7jM__FHQEd",
    "filename": "ImagesICPSC2015.zip",
    "Bentheimer": {
        "filename": "Bentheimer_1000c_3p0035um.raw",
        "url": "Bentheimer_1000c_3p0035um.raw.gz",
        "voxel_length": [3.0035, 3.0035, 3.0035],
        "metric_voxel_length_unit":  1e-6,
        "width": 1000, 
        "height": 1000, 
        "number_of_slices": 1000,
        "byte_order": "little-endian",
        "image_type": np.uint8
    },
    "Doddington": {
        "filename": "Doddington_1000c_2p6929um.raw",
        "url": "Doddington_1000c_2p6929um.raw.gz",
        "voxel_length": [2.6929, 2.6929, 2.6929],
        "metric_voxel_length_unit":  1e-6,
        "width": 1000, 
        "height": 1000, 
        "number_of_slices": 1000,
        "byte_order": "little-endian",
        "image_type": np.uint8
    },
    "Estaillades": {
        "filename": "Estaillades_1000c_3p31136um.raw",
        "url": "Estaillades_1000c_3p31136um.raw.gz",
        "voxel_length": [3.31136, 3.31136, 3.31136],
        "metric_voxel_length_unit":  1e-6,
        "width": 1000, 
        "height": 1000, 
        "number_of_slices": 1000,
        "byte_order": "little-endian",
        "image_type": np.uint8
    },
    "Ketton": {
        "filename": "Ketton_1000c_3p00006um.raw",
        "url": "Ketton_1000c_3p00006um.raw.gz",
        "voxel_length": [3.00006, 3.00006, 3.00006],
        "metric_voxel_length_unit":  1e-6,
        "width": 1000, 
        "height": 1000, 
        "number_of_slices": 1000,
        "byte_order": "little-endian",
        "image_type": np.uint8
    }
}


def load_icl_microct_sandstones_carbonates_2015(dataset, data_home: str = None, download_root="icl_temp", extract_root="~/icl_microct_sandstones_carbonates_2015", remove_finished: bool = True) -> xr.DataArray:

    data_home = get_data_home(data_home=data_home)
    if not os.path.exists(data_home):
        os.makedirs(data_home)
    
    metadata = DATASET_METADATA[dataset]

    download_root = os.path.join(data_home, download_root)
    extract_root = os.path.join(data_home, extract_root)

    filename = Path(extract_root, metadata['filename'])

    if not os.path.exists(os.path.join(extract_root, DATASET_METADATA['filename'][:-4])):
        download_file_from_google_drive(DATASET_METADATA['drive_id'], root=download_root, filename=DATASET_METADATA['filename'])

        archive = os.path.join(download_root, DATASET_METADATA['filename'])
        print(f"Extracting {archive} to {extract_root}")
        extract_archive(archive, extract_root, remove_finished)

    if not os.path.exists(filename):
        archive = os.path.join(extract_root,  DATASET_METADATA['filename'][:-4], metadata['url'])
        print(f"Extracting {archive} to {extract_root}")
        extract_archive(archive, extract_root, remove_finished)

    img = load_numpy_from_raw(filename, metadata['image_type'], metadata['height'], metadata['width'], metadata['number_of_slices'])
    img = create_xarray_from_numpy(img, metadata['filename'][:-4], metadata['voxel_length'], metadata['metric_voxel_length_unit'], metadata['height'], metadata['width'], metadata['number_of_slices'])

    return img