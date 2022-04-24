import xarray as xr
import os
import py7zr
import numpy as np
from drd.datasets.download_utils import download_url, get_data_home, extract_archive
from drd.datasets.utils import load_numpy_from_raw, create_xarray_from_numpy

UNITS = {"µm": 1e-6}

DATASET_METADATA = {
    "Berea": "https://figshare.com/ndownloader/files/3216671",
    "LV60A": "https://figshare.com/ndownloader/files/1699431",
    "LV60B": "https://figshare.com/ndownloader/files/3229805",
    "LV60C": "https://figshare.com/ndownloader/files/3229874",
    "S1": "https://figshare.com/ndownloader/files/3229847",
    "S2": "https://figshare.com/ndownloader/files/3229817",
    "S3": "https://figshare.com/ndownloader/files/3229790",
    "S4": "https://figshare.com/ndownloader/files/3229799",
    "S5": "https://figshare.com/ndownloader/files/3571106",
    "S6": "https://figshare.com/ndownloader/files/3229820",
    "S7": "https://figshare.com/ndownloader/files/3229862",
    "S8": "https://figshare.com/ndownloader/files/3229823",
    "S9": "https://figshare.com/ndownloader/files/3229835",
    "A1": "https://figshare.com/ndownloader/files/3229769",
    "C1": "https://figshare.com/ndownloader/files/3229778",
    "C2": "https://figshare.com/ndownloader/files/3229766",
    "F42A": "https://figshare.com/ndownloader/files/3229787",
    "F42B": "https://figshare.com/ndownloader/files/3229796",
    "F42C": "https://figshare.com/ndownloader/files/3229772"   
}

def load_icl_sandstones_carbonates_2009(dataset: str, data_home: str = None) -> xr.DataArray:
    url = DATASET_METADATA[dataset]
    
    data_home = get_data_home(data_home=data_home)

    if not os.path.exists(data_home):
        os.makedirs(data_home)

    download_url(url, filename=dataset+".7z", root=data_home)

    file_path = os.path.join(data_home, dataset+".7z")
    target_path = os.path.join(data_home, dataset)

    with py7zr.SevenZipFile(file_path, mode='r') as z:
        z.extractall(target_path)

    file_path_raw = os.path.join(data_home, dataset, dataset+".raw")
    file_path_nhdr = os.path.join(data_home, dataset, dataset+".nhdr")

    rows = ["type", "sizes", "space directions", "space units"]
    metadata = {}
    with open(file_path_nhdr, mode="r") as f:
        for line in f.readlines():
            row = line.split(":")
            if  row[0] in rows:
                metadata[row[0]] = row[1].strip("\n")

    metadata["sizes"] = [int(v) for v in metadata["sizes"].split(" ") if v not in [' ', '']]
    metadata["space directions"] = [v.strip("()").split(",") for v in metadata["space directions"].split(" ") if v not in [' ', '']]
    metadata["voxel_length"] = [float(v[i]) for i, v in enumerate(metadata['space directions'])]
    metadata["height"], metadata["width"], metadata["number_of_slices"] = metadata["sizes"]
   
    metadata['metric_voxel_length_unit'] = 1e-6
    metadata['image_type'] = np.uint8

    metadata['space units'] = [unit for unit in metadata['space units'].split(" ") if unit not in [' ', '']]
    metadata['metric_voxel_length_unit'] = [UNITS[v.strip("\"")] for v in metadata['space units']]

    img = load_numpy_from_raw(file_path_raw, metadata['image_type'], metadata['height'], metadata['width'], metadata['number_of_slices'])
    img = create_xarray_from_numpy(img, dataset, metadata['voxel_length'], metadata['metric_voxel_length_unit'], metadata['height'], metadata['width'], metadata['number_of_slices'])

    return img