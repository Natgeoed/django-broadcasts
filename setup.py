from setuptools import setup, find_packages
import os

README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    author="Ben Lopatin",
    author_email="ben.lopatin@wellfireinteractive.com",
    name='django-site-broadcasts',
    version='0.0.2',
    description='A small Django app that displays temporary, '
                'short broadcasts across a site.',
    long_description=open(README).read(),
    url='https://github.com/bennylope/django-site-broadcasts/',
    license='BSD License',
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
    install_requires=[
        'Django>=1.0',
    ],
    tests_require=[
        'Django>=1.0',
        'django-setuptest'
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    packages=find_packages(),
    zip_safe=False
)
