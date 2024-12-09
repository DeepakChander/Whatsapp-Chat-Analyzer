from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt and returns a list of dependencies,
    excluding '-e .' which is used for editable installation.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            
            # Explicitly remove '-e .' from the list
            requirements = [req for req in requirements if req != HYPHEN_E_DOT]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file {file_path} does not exist.")
    
    return requirements

setup(
    name='Whatsapp-Chat-Analyzer',
    version='0.0.1',
    author="Deepak",
    author_email="bhattd7303@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)