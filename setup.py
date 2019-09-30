import os
import sys
import shutil
from subprocess import call
from setuptools import setup
from warnings import warn

if sys.version_info.major != 3:
    raise RuntimeError('Wishbone requires Python 3')


setup(name='wishbone',
      version='0.4.2',
      description='Wishbone algorithm for identifying bifurcating trajectories from single-cell data',
      author='Manu Setty',
      author_email='manu.talanki@gmail.com',
      package_dir={'': 'src'},
      packages=['wishbone'],
      install_requires=[
          'numpy>=1.12.0',
          'pandas>=0.19.2',
          # scipy 1.3.1 (and probably 1.3.0) have a nasty bug:
          # https://github.com/scipy/scipy/issues/10695
          'scipy>=0.18.1, !=1.3.0, !=1.3.1',
          'Cython',
          'bhtsne',
          'matplotlib>=2.0.0',
          'seaborn>=0.7.1',
          'sklearn',
          'networkx>=1.11',
          'fcsparser>=0.1.2',
          'statsmodels>=0.8.0'],
      scripts=['src/wishbone/wishbone_gui.py'],
      )
    
# install phenograph
call(['pip', 'install', 'git+https://github.com/jacoblevine/phenograph.git'])


# get location of setup.py
setup_dir = os.path.dirname(os.path.realpath(__file__))

# install GSEA, diffusion components
tools_dir = os.path.expanduser('~/.wishbone/tools')
if os.path.isdir(tools_dir):
    shutil.rmtree(tools_dir)
shutil.copytree(setup_dir + '/tools/', tools_dir)
shutil.unpack_archive(tools_dir + '/mouse_gene_sets.tar.gz', tools_dir)
shutil.unpack_archive(tools_dir + '/human_gene_sets.tar.gz', tools_dir)

# Copy test data
data_dir = os.path.expanduser('~/.wishbone/data')
if os.path.isdir(data_dir):
    shutil.rmtree(data_dir)
shutil.copytree(setup_dir + '/data/', data_dir)

# Create directory for GSEA reports
os.makedirs( os.path.expanduser('~/.wishbone/gsea/'), exist_ok=True )
