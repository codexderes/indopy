from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'IndoPy adalah Packages Module Python berbahasa Indonesia yang akan membantu mempermudah proses pembelajaran.'

# Setting up
setup(
    name="IndoPy",
    version=VERSION,
    author="Codex Deres",
    author_email="codexderes@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/codexderes/indopy',
    packages=find_packages(),
    install_requires=[],
    keywords=['python indonesia','indopy','python berbahasa indonesia'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)