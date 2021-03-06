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
    python_requires='==3.*,>=3.6.1',
    author='André Ferreira',
    author_email='andrecnf@gmail.com',
    packages=['model_interpreter'],
    package_data={},
    install_requires=[
        'colorlover==0.*,>=0.3.0', 'comet-ml==3.*,>=3.1.10,>=3.1.2',
        'everett==1.*,>=1.0.0', 'modin==0.*,>=0.7.2', 'numpy==1.*,>=1.17.0',
        'pandas==1.0.1', 'pdoc3==0.*,>=0.7.2', 'pillow==7.*,>=7.0.0',
        'plotly==4.*,>=4.0.0', 'ray', 'shap', 'torch==1.*,>=1.1.0',
        'tqdm==4.*,>=4.32.0'
    ],
    dependency_links=['git+https://github.com/AndreCNF/shap.git#egg=shap'],
)
