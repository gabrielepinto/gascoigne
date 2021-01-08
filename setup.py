import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guascoigne", # Replace with your own username
    version="0.0.1",
    author="gabrieelepinto",
    author_email="gabriele.pinto@uniroma1.it",
    description="a set of useful tools for python. at the moment it includes: coeffplot a tool to make coefficient regression plot with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)