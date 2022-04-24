import numpy as np
import xarray as xr
import os
from drd.datasets.download_utils import download_url, get_data_home
from drd.datasets.utils import load_numpy_from_raw, create_xarray_from_numpy

DATASET_METADATA = {
    "Berea": {
        "Berea_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223451/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Berea_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223452/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Berea_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223453/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    }
}



def load_eleven_sandstones(dataset: str, filename: str, data_home: str = None) -> xr.DataArray:
    metadata = DATASET_METADATA[dataset][filename]
    
    data_home = get_data_home(data_home=data_home)
    if not os.path.exists(data_home):
        os.makedirs(data_home)

    file_path = os.path.join(data_home, filename)
    download_url(metadata["url"], root=data_home, filename=filename)

    img = load_numpy_from_raw(file_path, metadata['image_type'], metadata['height'], metadata['width'], metadata['number_of_slices'])
    img = create_xarray_from_numpy(img, filename, metadata['voxel_length'], metadata['metric_voxel_length_unit'], metadata['height'], metadata['width'], metadata['number_of_slices'])

    return img
