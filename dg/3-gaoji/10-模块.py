"""
In [1]: import hashlib	# 哈希库

In [2]: t = hashlib.md5()

In [3]: t.update("Nmamtf@013")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-749534d13aa6> in <module>()
----> 1 t.update("Nmamtf@013")

TypeError: Unicode-objects must be encoded before hashing

In [4]: t.update(b"Nmamtf@013")

In [5]: t.hexdigest()
Out[5]: '4e3b4b09cd9d83b5efd9004b93c26e19' # 不管要加密的字符串有多长，密文只有32位
# 黑客现在会利用很多台服务器（就是较高配置电脑）把一些你在不同服务器注册的同名的数据调出，然后用这些密文去匹配你的密码从而能破解你的密码
"""
