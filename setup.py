from setuptools import setup, find_packages
import pathlib
import re

WORK_DIR = pathlib.Path(__file__).parent

try:
    with open("README.md", "r", encoding="utf-8") as readme:
        long_description = readme.read()
except:
    long_description = "A simple library that takes chemistry to the next level."


def get_version():
    try:
        file = (WORK_DIR / "chemica" / "__init__.py").read_text("utf-8")
        return re.findall(r"^__version__ = \"([^\"]+)\"\r?$", file, re.M)[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")


setup(
    name="chemica",
    version=get_version(),
    description="A simple library that takes chemistry to the next level.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Chemistry, chemical equations",
    author="Mikhail Kuznetsov",
    author_email="yaunm@yandex.com",
    python_requires=">=3.7.0",
    url="https://github.com/mishailovic/chemica/",
    project_urls={
        "Documentation": "https://github.com/mishailovic/chemica/blob/main/README.md",
        "Issues": "https://github.com/mishailovic/chemica/issues",
    },
    packages=find_packages(),
    install_requires=["urllib3", "beautifulsoup4"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Typing :: Typed",
    ],
)