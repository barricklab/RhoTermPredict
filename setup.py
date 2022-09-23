from setuptools import setup, find_packages

# Gets Dependencies
with open('requirements.txt', 'r') as requirements_file:
    requirements = []
    for line in requirements_file:
        requirements.append(line.strip())

setup(
    name="rhotermpredict",
    version="3.0",
    packages=["rhotermpredict"],
    package_dir={'rhotermpredict': 'rhotermpredict'},

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=requirements,

    # metadata to display on PyPI
    author="Cameron Roots",
    author_email="croots@utexas.edu",
    description="Barrick Lab fork of Salvo 2019 RhoTermPredict",
    keywords="",
    url="https://github.com/barricklab/RhoTermPredict",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/barricklab/RhoTermPredict/issues",
        "Source Code": "https://github.com/barricklab/RhoTermPredict",
    },
    include_package_data=True,
    classifiers=[
        "License :: GNU Affero General Public License v3.0"
    ],
    entry_points={
        'console_scripts' : [
          'rhotermpredict = rhotermpredict.algorithm:main',
        ],
    },

    # could also include long_description, download_url, etc.
)
