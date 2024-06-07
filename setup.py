# -*- coding: utf-8 -*-

# @Date    : 2019-06-26
# @Author  : Peng Shiyu
from __future__ import print_function, unicode_literals, absolute_import, division

import io
import os
import glob

from setuptools import setup, find_packages

"""
## 本地测试
安装测试
python setup.py install 

卸载
pip uninstall spideradmin -y


## 打包上传
先升级打包工具
pip install --upgrade setuptools wheel twine

打包
python setup.py sdist bdist_wheel

检查
twine check dist/*

上传pypi
twine upload dist/*

命令整合
rm -rf dist build *.egg-info \
&& python setup.py sdist bdist_wheel  \
&& twine check dist/* \
&& twine upload dist/*


## 下载测试
安装测试
pip install -U spideradmin -i https://pypi.org/simple

打包的用的setup必须引入

参考：
https://packaging.python.org/guides/making-a-pypi-friendly-readme/

"""

base_dir = os.path.dirname(os.path.abspath(__file__))


# 版本号
version_file = glob.glob("*/version.py")[0]

with io.open(version_file, 'rb') as f:
    version_var = {}
    exec(f.read(), version_var)
    VERSION = version_var['VERSION']

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

with io.open("requirements.txt", 'r') as f:
    install_requires = f.read().split(os.sep)

setup(
    name='scrapyd-api',
    version=VERSION,
    description="scrapyd api",

    keywords='spider admin',
    author='Peng Shiyu',
    author_email='pengshiyuyx@gmail.com',
    license='MIT',
    url="https://github.com/mouday/scrapyd-api",

    long_description=long_description,
    long_description_content_type='text/markdown',

    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
)
