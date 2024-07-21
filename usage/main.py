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
    # 打印版本
    print(arrow.__version__)

    # 调用arrow/factory.py文件中的now函数
    """
    函數原型: now(tz: Optional[TZ_EXPR] = None) -> Arrow
    返回一个：class: `Arrow <Arrow.Arrow.Arrow>`对象，表示给定时区中的当前时间。
    ：param tz:(可选) A: ref: =`时区表达式 <tz-expr>`。默认为当地时间。

    用法：
    >>> import arrow
    >>> arrow.now()
    2024-07-21T22:07:04.908242+08:00
    >>> arrow.now('US/Pacific')
    2024-07-21T07:07:04.972242-07:00
    >>> arrow.now("+02:00")
    2024-07-21T16:07:04.972242+02:00
    >>> arrow.now("local")
    2024-07-21T22:07:04.972242+08:00
    """
    print(arrow.now())
    print(arrow.now('US/Pacific'))
    print(arrow.now("+02:00"))
    print(arrow.now("local"))

    print(arrow.get())

    # 调用arrow/arrow.py文件中的utcnow函数
    x = arrow.utcnow()
    print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond, x.tzinfo, x.fold)
    print(x.float_timestamp, x.int_timestamp, x.naive)
    print(x, x.datatime)
