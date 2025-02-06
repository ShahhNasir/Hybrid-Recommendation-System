from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list[str]:
    """
    This function is created to iterate through the requirements file and create a list.
    """
    with open(file_path,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(

    name= "Hybrid Recommendation System",
    version= '0.1',
    author= "Nasir Hussain",
    author_email= "shahhnasir83@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
    
)