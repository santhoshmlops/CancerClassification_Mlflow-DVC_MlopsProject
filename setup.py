# setup.py - Package Configuration Script

import setuptools

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package metadata
__version__ = "0.1.0"
REPO_NAME = "CancerClassification_Mlflow-DVC_MlopsProject"
AUTHOR_USER_NAME = "santhoshmlops"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "santhoshmlops@gmail.com"

# Configure setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This package is designed for building convolutional neural network (CNN) applications using the Python programming language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
