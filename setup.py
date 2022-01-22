from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="zdb",
    version="0.0.1",
    author="javang.lee",
    author_email="walkbob@sina.com",
    description="Timeseries for data show",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="http://themosthansomeman.com/", 
    include_package_data = True,
    packages_data={
        'data_pkg':['data/default/']
    },

    packages=find_packages(),

    py_modules=['zdb','vdict','runlog', 'common/common'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)