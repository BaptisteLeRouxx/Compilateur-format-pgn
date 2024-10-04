from setuptools import setup, find_packages

setup(
    name='compilateur_format_pgn',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy', 'requests', 'pytest', 'chess'
    ],
    entry_points={
        'console_scripts': [
            'analyse-partie = src.analyse_partie:main',
        ],
    },
)
