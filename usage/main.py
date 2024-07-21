import arrow

r"""
pip源: 
清华源: https://pypi.tuna.tsinghua.edu.cn/simple
阿里源: https://mirrors.aliyun.com/pypi/simple/
腾讯源: http://mirrors.cloud.tencent.com/pypi/simple
豆瓣源: http://pypi.douban.com/simple/
"""

r"""
安装arrow, 当前版本为python 3.8.10
pip install arrow
pip install --upgrade pip
pip install pytest

(venv) PS C:\github\arrow> pip list          
Package               Version
--------------------- --------------
arrow                 1.3.0
colorama              0.4.6
exceptiongroup        1.2.2
iniconfig             2.0.0
packaging             24.1
pip                   22.3.1
pluggy                1.5.0
pytest                8.3.1
python-dateutil       2.9.0.post0
setuptools            65.5.1
six                   1.16.0
tomli                 2.0.1
types-python-dateutil 2.9.0.20240316
wheel                 0.38.4

"""

if __name__ == "__main__":
    print(arrow.__version__)

    print(arrow.now())
    print(arrow.get())
    print(arrow.utcnow())
