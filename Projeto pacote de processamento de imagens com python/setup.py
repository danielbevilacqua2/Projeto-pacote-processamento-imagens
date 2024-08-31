from setuptools import setup, find_packages # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="my_name",
    author_email="my_email",
    description="My short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements==requirements,
    python_requires=">=3.8",
)