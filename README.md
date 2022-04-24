# Digital Rocks Data
### Make downloading and using Digital Rock Data great again!  
[![Run tests](https://github.com/lukasmosser/digital_rocks_data/actions/workflows/build.yaml/badge.svg)](https://github.com/lukasmosser/digital_rocks_data/actions/workflows/build.yaml)## Contributing [![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lukasmosser/digital_rocks_data/issues)[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://lukasmosser.github.io/digital_rocks_data/index.html)
## About

Digital Rock Images are three-dimensional datasets of rocks and other porous media.  
These are typically acquired using three-dimensional imaging techniques such as [Micro-Computer Tomography (MicroCT)](https://en.wikipedia.org/wiki/X-ray_microtomography).  

They represent a rich dataset that form a basis for characterization of physical processes involving porous media.  

## Purpose of the `drd` library

Digital Rock Images are scattered throughout the web on various hosting sites such as the [Digital Rocks Portal](https://www.digitalrocksportal.org/), [Zenodo](https://www.zenodo.org), or university specific sites.
This library aims to make downloading these datasets easy through a python interface so they can be used in automated image processing workflows, 
reproducible research, or data science and machine learning worfklows.  

Furthermore, these images are associated with metadata about their spatial dimensions which should be considered when loading these image datasets.  
The library therefore requires these metadata to be available and creates an [xarray](https://docs.xarray.dev/en/stable/) DataArray which can keep spatial scale information when loading an image dataset.  

Each dataset is linked in this library i.e. no hosting is done by the library itself.  

## Available Datasets

[Digital Rocks Portal](https://www.digitalrocksportal.org/):
- [Eleven Sandstones Dataset](https://www.digitalrocksportal.org/projects/317)
    - Berea

[Imperial College London](https://www.imperial.ac.uk/earth-science/research/research-groups/pore-scale-modelling/micro-ct-images-and-networks/):
- MicroCT Images of Sandstones and Carbonates 2015

## Contributing

Authors are encouraged to contribute their own datasets using the correct metadata.  
See `drd/datasets/eleven_sandstones.py` for an example implementation.  
Please add corresponding tests and an example to your pull request.  

## Creation

This package was created during the Transform 22 software sprint.