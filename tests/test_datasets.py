import pytest
import matplotlib.pyplot as plt
import requests
from drd.datasets import load_eleven_sandstones
from drd.datasets import load_icl_microct_sandstones_carbonates_2015
from drd.datasets import load_icl_sandstones_carbonates_2009
from drd.datasets.eleven_sandstones import DATASET_METADATA as ELEVEN_SANDSTONES_METADATA
from drd.datasets.icl_microct_sandstones_carbonates_2015 import DATASET_METADATA as ICL_2015_METADATA
from drd.datasets.icl_sandstones_carbonates_2009 import DATASET_METADATA as ICL_2009_METADATA
from drd.datasets.download_utils import download_file_from_google_drive, get_data_home

eleven_sandstones_urls = [(metadata['url'], filename) for _, dataset in ELEVEN_SANDSTONES_METADATA.items()  for filename, metadata in dataset.items() ]
@pytest.mark.parametrize("url,filename", eleven_sandstones_urls)
def test_eleven_sandstones_file_availability(url, filename):
    assert(requests.head(url).status_code==302)


def test_icl_microct_sandstones_carbonates_2015_file_availability():
    download_root = get_data_home()
    api_response = download_file_from_google_drive(ICL_2015_METADATA['drive_id'], root=download_root, filename=ICL_2015_METADATA['filename'], save_content=False)
    assert(api_response is None)


icl_images_2009 = [(name, url) for name, url in ICL_2009_METADATA.items()]
print(icl_images_2009)
@pytest.mark.parametrize("name,url", icl_images_2009)
def test_icl_sandstones_carbonates_2009_file_availability(name, url):
    assert(requests.head(url).status_code==302)


def test_icl_sandstones_carbonates_2009_loading():
    img = load_icl_sandstones_carbonates_2009("Berea")
    assert True
