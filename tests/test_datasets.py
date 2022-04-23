import pytest
import matplotlib.pyplot as plt

from drd.datasets import load_eleven_sandstones
from drd.datasets import load_icl_microct_sandstones_carbonates_2015


def test_eleven_sandstones_dataset():
    img = load_eleven_sandstones("Berea", "Berea_2d25um_grayscale.raw")

    assert(True, True)

@pytest.mark.parametrize("dataset", ["Doddington", "Estaillades", "Ketton", "Bentheimer"])
def test_icl_microct_sandstones_carbonates_2015(dataset: str):

    img = load_icl_microct_sandstones_carbonates_2015(dataset=dataset)
    
    assert(True, True)