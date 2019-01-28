
from setuptools import find_packages, setup
setup(
    name='KLineAnalys',
    version='0.0.1.1',
    description='this is a Finance Analysis System',
    author='fdsn',#作者
    author_email='670428704@qq.com',
    url='https://github.com/670428704/FinanceAnalysis.git',
    # packages=find_packages(),
    packages=['KLineAnalysis'],  #这里是所有代码所在的文件夹名称
    install_requires=['requests'],
)
