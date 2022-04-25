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
    },
    "BanderaBrown": {
        "BanderaBrown_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223448/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BanderaBrown_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223454/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BanderaBrown_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223455/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "BanderaGray": {
        "BanderaGray_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223459/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BanderaGray_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223457/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BanderaGray_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223458/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "Bentheimer": {
        "Bentheimer_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223461/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Bentheimer_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223462/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Bentheimer_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223463/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "BSG": {
        "BSG_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223464/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BSG_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223465/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BSG_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223466/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "BUG": {
        "BUG_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223467/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BUG_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223468/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BUG_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223469/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "BB": {
        "BB_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223470/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BB_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223471/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "BB_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223472/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "CastleGate": {
        "CastleGate_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223473/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "CastleGate_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223474/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "CastleGate_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223475/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "Kirby": {
        "Kirby_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223476/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Kirby_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223477/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Kirby_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223478/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "Leopard": {
        "Leopard_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223479/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Leopard_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223480/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Leopard_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223481/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit": 1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        }   
    },
    "Parker": {
        "Parker_2d25um_grayscale.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223482/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Parker_2d25um_grayscale_filtered.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223483/download/",
            "voxel_length": [2.25, 2.25, 2.25],
            "metric_voxel_length_unit":  1e-6,
            "width": 1000, 
            "height": 1000, 
            "number_of_slices": 1000,
            "byte_order": "little-endian",
            "image_type": np.uint8
        },
        "Parker_2d25um_binary.raw": {
            "url": "https://www.digitalrocksportal.org/projects/317/images/223484/download/",
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
