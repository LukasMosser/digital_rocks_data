# Digital Rocks Data
### Make downloading and using Digital Rock Data great again!  

## About

Digital Rock Images are three-dimensional datasets of rocks and other porous media.  
These are typically acquired using three-dimensional imaging techniques such as Micro-Computer Tomography (MicroCT).  

They represent a rich dataset that form a basis for characterization of physical processes involving porous media.  

## Purpose of the drd library

Digital Rock Images are scattered throughout the web on various hosting sites such as the digital rocks portal, zenodo, or university specific sites.
This library aims to make downloading these datasets easy through a python interface so they can be used in automated image processing workflows, 
reproducible research, or data science and machine learning worfklows.  

Furthermore, these images are associated with metadata about their spatial dimensions which should be considered when loading these image datasets.  
The library therefore requires these metadata to be available and creates an xarray DataArray which can keep spatial scale information when loading an image dataset.  

Each dataset is linked in this library i.e. no hosting is done by the library itself.  

## Available Datasets

Digital Rocks Portal:
- Eleven Sandstones Dataset

Imperial College London:
- MicroCT Images of Sandstones and Carbonates 2015

## Contributing

Authors are encouraged to contribute their own datasets using the correct metadata.  
See `drd/datasets/eleven_sandstones.py` for an example implementation.  
Please add corresponding tests and an example to your pull request.  