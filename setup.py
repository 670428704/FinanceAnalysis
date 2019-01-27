

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "FinanceAnalysis",      #这里是pip项目发布的名称
    version = "1.0.1",  #版本号，数值大的会优先被pip
    keywords = ("FinanceAnalysis","Finance","Analysis"),
    description = "An feature extraction algorithm",
    long_description = "An feature extraction algorithm, improve the FastICA",
    license = "MIT Licence",

    url = "https://github.com/670428704/FinanceAnalysis.git",     #项目相关文件地址，一般是github
    author = "fdsn",
    author_email = "670428704@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy","tushare","matplotlib","mpl_finance","datetime"]          #这个项目需要的第三方库
)


