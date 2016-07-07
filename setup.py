
from __future__ import absolute_import
import platform
import shutil
import sys
import os
from setuptools import setup, find_packages
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# We can not import `xgboost.libpath` in setup.py directly since xgboost/__init__.py
# import `xgboost.core` and finally will import `numpy` and `scipy` which are setup
# `install_requires`. That's why we're using `exec` here.
libpath_py = os.path.join(CURRENT_DIR, 'xgboost/libpath.py')
libpath = {'__file__': libpath_py}
exec(compile(open(libpath_py, "rb").read(), libpath_py, 'exec'), libpath, libpath)

if os.name == 'nt':     # if Windows, c
    ver = platform.architecture()[0]
    if ver == '32bit':
        shutil.copy('win32/libstdc++-6.dll', 'xgboost/')
        shutil.copy('win32/libxgboost.dll', 'xgboost/')
    elif ver == '64bit':
        shutil.copy('win64/libxgboost.dll', 'xgboost/')
    else:
        pass  # Guess, other architectures are not supported
else:
    print('Non-Windows users please use original source at https://github.com/dmlc/xgboost')
    sys.exit()

# Please use setup_pip.py for generating and deploying pip installation
# detailed instruction in setup_pip.py
setup(name='xgboost',
      version=open(os.path.join(CURRENT_DIR, 'xgboost/VERSION')).read().strip(),
      # version='0.4a23',
      description="XGBoost Python Package",
      long_description=open(os.path.join(CURRENT_DIR, 'README.rst')).read(),
      install_requires=[
          'numpy',
          'scipy',
      ],
      maintainer='Hongliang Liu',
      maintainer_email='phunter.lau@gmail.com',
      zip_safe=False,
      packages=find_packages(),
      # this will use MANIFEST.in during install where we specify additional files
      include_package_data=True,
      url='https://github.com/dmlc/xgboost')
