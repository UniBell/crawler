from setuptools import setup

setup (
    name='crawler',
    packages=['crawler'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-SQLAlchemy',
        'MySQL-connector-python'
    ],
)
