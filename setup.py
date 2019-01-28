
from setuptools import find_packages, setup
setup(
    name='KLineAnalys',
    version='0.0.1.1',
    description='this is a Finance Analysis System',
    author='fdsn670428704',#作者
    author_email="670428704@qq.com",
    url='https://github.com/670428704/FinanceAnalysis.git',
    # packages=find_packages(),
    packages=find_packages(),  #这里是所有代码所在的文件夹名称
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
