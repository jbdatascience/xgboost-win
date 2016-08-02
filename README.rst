XGBoost Python Package
======================

This is simply a compiled version for Windows (both 32 and 64 bit) of the popular xgboost (Scalable, Portable and Distributed Gradient Boosting) package for Python 2.x, without any modifications. The compilation for Windows OS is quite tedious and complicated, thus, this package includes everything that is needed to run this tool from Python environment. It can be installed from the GitHub simply using *pip install*. It also includes binary executables (both 32 and 64 bit), yet, they are not installed with pip, but can also be found in winxx directories. These libraries are built in Windows 7 SP1 (32 bit) and Windows 10 (64 bit), using MinGW 5.3 (https://sourceforge.net/projects/mingw/files/)

The original version can be found found in https://github.com/dmlc/xgboost; if you are using **nix based version, please install from the original source or just entering *pip install xgboost*

As noted in the README of the original package, their pip installation may not work on some Windows environments, and it may cause unexpected errors. Original *xgboost* pip installation on Windows is currently disabled for further investigation, therefore, use this package instead at your own risk.
