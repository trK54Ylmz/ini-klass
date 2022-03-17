from setuptools import find_packages, setup

description = 'ini file parser.'

try:
    long_description = open('readme.md', 'r', encoding='utf8').read()
except Exception:
    long_description = description

setup(
    name='ini-klass',
    version='0.0.1',
    author='Tarik Yilmaz',
    author_email='tarikyilmaz.54@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/trk54ylmz/ini-klass',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'attrdict2==0.0.2',
        'configobj==5.0.6',
    ],
)
