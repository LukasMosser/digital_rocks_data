from pathlib import Path
import numpy as np
import numpy.typing as npt
import xarray as xr
import xarray.plot.utils as ut


def load_numpy_from_raw(file_path: Path, image_type: npt.DTypeLike, height: int, width: int, number_of_slices: int) -> npt.ArrayLike:
    img = np.fromfile(file_path, dtype=image_type, sep="")
    img = img.reshape([height, width, number_of_slices])
    return img


def create_xarray_from_numpy(img, name, voxel_lengths, length_unit, height, width, number_of_slices) -> xr.DataArray:
    
    if not isinstance(length_unit, list):
        length_unit = [length_unit]*3

    x_axis = [i*voxel_lengths[0]*length_unit[0] for i in range(height)]
    y_axis = [i*voxel_lengths[1]*length_unit[1] for i in range(width)]
    z_axis = [i*voxel_lengths[2]*length_unit[2] for i in range(number_of_slices)]

    da = xr.DataArray(
        img,
        dims=("x", "y", "z"),
        name=name,
        coords={
            "x": ('x', x_axis, {'long_name': 'height', 'units': 'm'}),
            "y": ('y', y_axis, {'long_name': 'width', 'units': 'm'}),
            "z": ('z', z_axis, {'long_name': 'slice', 'units': 'm'})
        }
    )

    return da