# https://setuptools.readthedocs.io/
# https://docs.python.org/2/distutils/index.html
# https://docs.python.org/3/distutils/index.html
import setuptools

# https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
# https://docs.python.org/3/distutils/setupscript.html#additional-meta-data
# https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords
# https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata

setuptools.setup(
    name='zaecee',
    version='1.0',
    packages=setuptools.find_packages(),
    #py_modules=['cli'],
    entry_points={
        'console_scripts': [
            'zaecee=zaecee.cli:main'
        ]
    },
    zip_safe=False
)
