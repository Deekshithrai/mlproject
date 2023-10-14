from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as file_obj:
        for line in file_obj:
            req = line.strip()  # Remove leading/trailing whitespace
            if req and req != HYPEN_E_DOT:  # Skip empty lines and "-e ."
                requirements.append(req)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Deekshith",
    author_email="deekshithrai505@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
