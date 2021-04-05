import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SM00R",
    version="0.0.2",
    author="Stephen Moore",
    author_email="author@example.com",
    description="A sentimenal analyzer and analysis of the Yelp Dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows 10",
    ],
    python_requires='>=3.7',
)