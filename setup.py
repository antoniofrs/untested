from setuptools import setup, find_packages


setup(
    name='untested',
    version='0.1.0',
    packages=find_packages(),
    author='Antonio Frisenda',
    author_email='antoniofrisenda.dev@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/antoniofrs/untested.git',
    install_requires=[
        'requests==2.31.0'
    ]
)