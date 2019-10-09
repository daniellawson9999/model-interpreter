# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='model-interpreter',
    version='0.1.0',
    description='An API for intuitive interpretation of machine learning models',
    python_requires='==3.*,>=3.7.0',
    author='André Ferreira',
    author_email='andrecnf@gmail.com',
    packages=['model_interpreter'],
    package_data={},
    install_requires=[
        'colorlover==0.*,>=0.3.0', 'comet-ml==2.*,>=2.0.0',
        'numpy==1.*,>=1.17.0', 'pandas==0.*,>=0.25.0', 'plotly==4.*,>=4.0.0',
        'shap', 'torch==1.*,>=1.1.0', 'tqdm==4.*,>=4.32.0'
    ],
    dependency_links=['git+https://github.com/AndreCNF/shap.git#egg=shap'],
)