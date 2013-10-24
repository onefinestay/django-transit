from setuptools import setup

setup(
    name='django-transits',
    version='0.0.1',
    install_requires=[
        'Django >=1.5',
    ],
    packages=['transit'],
    package_dir={'transit': 'transit'},
    include_package_data = True,    # include everything in source control
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python']
)