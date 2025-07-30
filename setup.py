from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI TRIP PLANNER",
    version="0.1",
    author="Atharva Hatekar",
    packages=find_packages(),
    install_requires = requirements,
)