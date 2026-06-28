'''
A `setup.py` file is used to package and install an ML project as a Python package,
 making it easier to organize, share, and reuse the code. It contains metadata about 
 the project (such as its name, version, author, and description), specifies the project's
dependencies (libraries required to run it), and defines which Python modules should be
included during installation. When you run commands like `pip install .` or `python setup.py
install` (older approach), Python uses this file to install the project and its 
dependencies so that modules can be imported from anywhere without manually setting paths.
In modern ML projects, `setup.py` helps maintain a clean project structure, supports reproducibility
, and simplifies deployment and collaboration, although newer projects increasingly use 
`pyproject.toml` instead of `setup.py` for packaging.
'''

from setuptools import find_packages , setup
from typing import List 

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup (
name='mlproject1',
version='0.0.1',
author='Atharva',
author_email='matharva655@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   
)