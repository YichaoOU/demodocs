from setuptools import setup

setup(
    name="my_package",
    # (...)
    extras_require={
        'docs': [
            'sphinx == 1.5.5']}
)