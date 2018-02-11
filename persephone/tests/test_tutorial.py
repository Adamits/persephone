import os
from os.path import join
import pytest

from persephone import corpus
from persephone import run

NA_EXAMPLE_LINK = "https://cloudstor.aarnet.edu.au/plus/s/YJXTLHkYvpG85kX/download"

@pytest.mark.slow
def test_ready_train():
    """ Pull the corpus from the link in the README. """

    # Set some filenames
    data_dir = "data/"
    zip_fn = join(data_dir, "na_example_small.zip")
    zip_fn = join(data_dir, "na_example_small.zip")
    na_example_dir = join(data_dir, "na_example/")

    # Remove data previously collected
    import shutil
    if os.path.isdir(na_example_dir):
        shutil.rmtree(na_example_dir)
    if os.path.isfile(zip_fn):
        os.remove(zip_fn)

    import urllib.request
    urllib.request.urlretrieve(NA_EXAMPLE_LINK, filename=zip_fn)

    # Unzip the data
    import subprocess
    args = ["unzip", zip_fn, "-d", data_dir]
    subprocess.run(args)

    wav_dir == join(na_example_dir, "wav/")
    assert os.path.isdir(wav_dir)
    assert len(os.listdir(wav_dir)) == 1024

    na_example_dir = join(data_dir, "na_example/")
    assert os.path.exists(na_example_dir)

    # Test the first setup encouraged in the tutorial
    corp = corpus.ReadyCorpus(na_example_dir)
    run.train_ready(corp)

    # TODO Get the experiment number and experiment directory and fetch
    # results. Probably should expect < 20% LER.

    # TODO Assert the convergence of the model at the end by reading the
    # output.

# Other tests:
    # TODO assert the contents of the prefix files

    # TODO Assert that we've filtered files with too many frames

    # TODO Test out corpus reader on the same data. (Make a function for that
    # within this functions scope)