#To define configuration of your project such as metadata,dependencies,and more

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    # this function will return  list of requirements
    requirement_lst:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirement.txt file do not exist")
    return requirement_lst         

setup(
    Name="NetworkSecurity",
    version="0.0.1",
    author="Sanskar Jain",
    packages=find_packages(),
    install_requirements=get_requirements()
)
