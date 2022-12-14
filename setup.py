import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="emercoin",
    version="0.0.4",
    description="Emercoin cryptocurrency API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sr.ht/~cofob/Emercoin.py/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
