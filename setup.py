
import os
import sys
from pathlib import Path
from setuptools import setup, find_packages


if sys.version_info.major != 3:
    raise RuntimeError("This package requires Python 3+")


version = '0.0.0a'
pkg_name = 'trt_trf'
gitrepo = 'gexexp/trt-trf'
root = Path(__file__).parent


requirements = [
    'lazycls',
    'lazyapi',
    'pylogz',
    'transformers',
    'sentencepiece'
]

args = {
    'packages': find_packages(include = ['trt_trf', 'trt_trf.*']),
    'install_requires': requirements,
    'long_description': root.joinpath('README.md').read_text(encoding='utf-8'),
    'python_requires': '>=3.7',
    'entry_points': {
        'console_scripts': [
            'trtbench = trt_trf.benchmark:main',
        ]
    }
}

os.system(f'pip install -r {root.joinpath("requirements.txt").as_posix()}')

setup(
    name=pkg_name,
    version=version,
    url=f'https://github.com/{gitrepo}',
    license='MIT Style',
    description='',
    author='Tri Songz',
    author_email='ts@growthengineai.com',
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    include_package_data=True,
    **args
)