import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyLibrary",
    version = "0.0.1",
    author = "Hamid Reza Horr",
    author_email = "hamidreza.hr87@gmail.com",
    description = "A package to use in Irisa Prime Chat Bor",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hamidhr87/PyLibrary.git",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)