from setuptools import find_packages,setup 
from typing import List

HYPEN_E_DOT='-e.'

"""
def get_requirements(file_path:str)->List[str]:
    '''
    This function return the requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
"""

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from the file.
    """
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()
        # Strip whitespace and newline characters from each line
        requirements = [req.strip() for req in requirements if req.strip() != HYPEN_E_DOT]
    
    return requirements
    

setup (
name='mlproject',
version='0.0.1',
author='Murat',
author_email='buzzycarl@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
