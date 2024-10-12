from setuptools import setup, find_packages

setup(
    name='phabox',
    version='2.0.0',
    packages=find_packages(),
    install_requires=[
    'aiohttp==3.10.9',
    'aiosignal==1.3.1',
    'async-timeout==4.0.3',
    'attrs==24.2.0',
    'beautifulsoup4==4.12.3',
    'biopython==1.78',
    'boltons==24.0.0',
    'certifi==2024.8.30',
    'cffi==1.17.1',
    'charset-normalizer==3.3.2',
    'click==8.1.7',
    'colorama==0.4.6',
    'cryptography==39.0.0',
    'cycler==0.12.1',
    'datasets==2.2.2',
    'dill==0.3.4',
    'filelock==3.16.1',
    'fonttools==4.54.1',
    'fsspec==2024.9.0',
    'h2==4.1.0',
    'hpack==4.0.0',
    'huggingface_hub==0.25.1',
    'hyperframe==6.0.1',
    'idna==3.10',
    'importlib-metadata==8.5.0',
    'importlib-resources==6.4.5',
    'jinja2==3.1.4',
    'joblib==1.4.2',
    'jsonpatch==1.33',
    'jsonpointer==3.0.0',
    'jsonschema==4.23.0',
    'jsonschema-specifications==2024.10.1',
    'kiwisolver==1.4.7',
    'markupsafe==3.0.1',
    'matplotlib==3.9.1',
    'more-itertools==10.5.0',
    'multidict==6.1.0',
    'multiprocess==0.70.13',
    'networkx==3.2.1',
    'numpy==1.26.4',
    'olefile==0.47',
    'packaging==24.1',
    'pandas==2.2.3',
    'patsy==0.5.6',
    'pillow==8.4.0',
    'pkginfo==1.11.1',
    'pkgutil-resolve-name==1.3.10',
    'pluggy==1.5.0',
    'protobuf==3.20.3',
    'psutil==6.0.0',
    'pycparser==2.22',
    'pyopenssl==23.2.0',
    'pyparsing==3.1.4',
    'pytz==2024.1',
    'pyyaml==6.0.2',
    'regex==2024.9.11',
    'requests==2.32.3',
    'responses==0.18.0',
    'ruamel.yaml==0.17.40',
    'ruamel.yaml.clib==0.2.8',
    'sacremoses==0.0.53',
    'scipy==1.13.1',
    'seaborn==0.13.2',
    'setuptools==75.1.0',
    'six==1.16.0',
    'soupsieve==2.5',
    'statsmodels==0.14.4',
    'tornado==6.4.1',
    'tqdm==4.66.5',
    'transformers',
    'torch',
    'typing-extensions==4.12.2',
    'urllib3==2.2.3',
    'wheel==0.44.0',
    'yarl==1.13.1',
    'zipp==3.20.2',
    ],
    entry_points={
        'console_scripts': [
            'phabox2=phabox2.phabox2:main',
        ],
    },
    author='SHANG JIAYU',
    author_email='jiayushang@cuhk.edu.hk',
    description='Local version of the virus identification and analysis web server',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KennthShang/PhaBOX',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
