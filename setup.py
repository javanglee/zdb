from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name="richdb",
    version="0.1.2",
    author="javang.lee",
    author_email="walkbob@sina.com",
    description="Time,Timeseries,vdict(combine the benefits of list and dict) is designed for Timeseries problem analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires = ["rich"],
    url="https://github.com/javanglee/zdb.git",
    include_package_data = True,
    packages_data={
        'data_pkg':['data/default/']
    },

    packages=find_packages(),

    py_modules=['richdb','vdict','ztime','version','wull'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)