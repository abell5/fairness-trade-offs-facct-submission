import os
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='FairnessEvaluator',
    version='0.0.1',
    author='BestResearchTeam',
    author_email='alb9742@nyu.edu',
    description='Fairness Evaluator toolkit',
    install_requires=required,
    python_requires='>=3.7',
    packages=find_packages()
)