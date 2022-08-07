from setuptools import setup
from typing import List


PROOJECT_NAME = "housing predictor"
VERSION = "0.0.1"
REQUIREMENTS_FILE_NAME = "requirements.txt"
def get_requirement_list()->List[str]:
    """
    Description: This function is going to return list of requirements mentioned 
    in requirements.txt file
    return : This function will return a list which wil contain name of libraries mentioned
    in requirement.txt file
    """


    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    




# declaring variiables for setup function

setup(
    name="housing predictor",
    version = "0.0.3",
    author = "Govind",
    description = "MAchine Learning Project",
    packages = ["housing"],
    install_requires = get_requirement_list().remove('-e .')


)


if __name__=="__main__":
    print(get_requirement_list())