from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .' # Defined a constant

def get_req(file_path:str)->List[str]:
    '''
    This is a function which would help to get the required libraries because writing install_requires=['pandas',....]
    is not really feasible at larger scale

    '-e .' is written at last in requirements.txt file because it opens in editable mode,meaning even if u change something in
    that particular file where this is written then it would also reflect the change in the entire project, meaning it would
    update the files in realtime
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

# MetaData Info
setup(
    name='MLP1',
    version=1.0,
    author='Vinay',
    author_email='dayamavinay2@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')

)
