import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__('broadcasts').__doc__.splitlines()).strip()

setup(
    name="django-broadcasts",
    version=__import__('{{app_name}}').get_version().replace(' ', '-'),
    url='https://github.com/Natgeoed/django-broadcasts',
    author='',
    author_email='',
    description=DESC,
    long_description=get_readme(),
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    tests_require=[
        'Django>=1.0',
        'django-setuptest'
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    zip_safe=False
)
