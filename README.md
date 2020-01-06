Wishbone 
--------

Wishbone is an algorithm to align single cells from differentiation systems with bifurcating branches. Wishbone has been designed to work 
with multidimensional single cell data from diverse technologies such as Mass cytometry and single cell RNA-seq. 

## Installation and dependencies

Wishbone requires Python 3.
It depends on a number of Python 3 packages available on PyPI or conda-forge.
This fork adds support for openTSNE which is notably easier to install with conda, but a pip-only installation is feasible too.

### conda
The easiest way to install Wishbone and its dependencies is to create a dedicated conda environment.
```sh
# create and activate conda environment
conda create -n wishbone python=3.6
conda activate wishbone
# if necessary: conda install jupyter
# install wishbone and its dependencies
git clone git://github.com/manusetty/wishbone.git
cd wishbone
pip install .
# install openTSNE
conda install --channel conda-forge opentsne
```

### pip
The alternative is to install everything directly on your system, using `pip` only.
It is apparently simpler but the result is more fragile because the dependencies can be updated inadvertently.
Installing openTSNE is harder too, as it requires numpy, a C/C++ compiler with OpenMP, and possibly FFTW3.

```sh
git clone git://github.com/manusetty/wishbone.git
cd wishbone
pip install .
pip install opentsne
```

## Usage

### Command line
A tutorial on Wishbone usage and results visualization for single cell RNA-seq data can be found in this notebook: http://nbviewer.jupyter.org/github/ManuSetty/wishbone/blob/master/notebooks/Wishbone_for_single_cell_RNAseq.ipynb


A tutorial on Wishbone usage and results visualization for mass cytometry data can be found in this notebook: http://nbviewer.jupyter.org/github/ManuSetty/wishbone/blob/master/notebooks/Wishbone_for_mass_cytometry.ipynb


### GUI
A python GUI is now available for Wishbone. After following the installation steps listed below, the GUI can be invoked using
```console
wishbone_gui.py
```

A tutorial on using the interface is available in the [Wishbone tutorial](docs/wishbone_tutorial.pptx).


## Citation

Wishbone manuscript is available from [Nature Biotechnology](http://www.nature.com/nbt/journal/vaop/ncurrent/full/nbt.3569.html). If you use Wishbone for your work, please cite our paper.

```
	@article{Wishbone_2016,
                title = {Wishbone identifies bifurcating developmental trajectories from single-cell data},
                author = {Manu Setty and Michelle D Tadmor and Shlomit Reich-Zeliger and Omer Angel and Tomer Meir Salame and Pooja Kathail and Kristy Choi and Sean Bendall and Nir Friedman and Dana Pe'er},
                journal = {Nature Biotechnology},
                year = {2016},
                month = {may},
                url = {http://dx.doi.org/10.1038/nbt.3569},
                doi = {doi:10.1038/nbt.3569}
        }
```
