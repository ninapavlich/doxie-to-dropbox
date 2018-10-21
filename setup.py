from setuptools import setup, find_packages

setup(
    name = 'doxietodropbox',
    version = '0.5',
    author = 'Nina Pavlich',
    author_email='nina@ninalp.com',
    url = 'https://github.com/ninapavlich/doxie-to-dropbox',
    license = "MIT",
    description = 'Retrieves scans on your Doxie Go or Doxie Q, then uploads to a Dropbox folder.',
    keywords = ['libraries', 'scanning'],
    include_package_data = True,
    packages = ['doxietodropbox'],

    install_requires=[
        'Pillow',
        'doxieautomator',
        'dropbox'
    ],
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)