from setuptools import find_packages,setup
from typing import List

HYP='-e.'
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
    if HYP in requirements:
        requirements.remove(HYP)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Kshitij',
    author_email='kshitijp2006@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)