from distutils.core import setup

setup(
    # Application name:
    name="NiFi-XMLtoJSON",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Colton Rodgers",
    author_email="colton.rodgers@zirous.com",

    # Packages
    packages=["src", "src/runner", "src/xml2json"],

    # Include additional files into the package
    include_package_data=True,

    license="LICENSE.txt",

    description="Used for a NiFi processor in order to take an xml file and convert it to a JSON file.",

    long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "lxml"
    ],
)
