# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="tenntucky-lambdata-pt4",
    version="1.0",
    author="Kole Goldsberry",
    author_email="kole.goldsberry@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Tenntucky/tenntucky-lambdata-pt4",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)