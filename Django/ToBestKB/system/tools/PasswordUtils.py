# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:41:20 2024

@author: wangxg
"""

import hashlib
 
def md5Encode(password:str):
    """MD5基础实现"""
    md = hashlib.md5(password.encode('utf-8'))
    md5pwd = md.hexdigest()
    return  md5pwd

#盐编码
SALT_CODE="""
  以さもっんとかぇш защㄞāáモョヲトケヴィタàǎㄤㄅлжㄖкакㄞㄤㄅㄖапぅぃひゅスソス
  无限为有限,以无法为有法,隐技巧与无形;以無限為有限,以無法為有法
"""

def md5SaltEncode(password:str):
    """盐加密"""
    md5pwd=md5Encode(password)
    pwd2=md5pwd+SALT_CODE+md5pwd
    return md5Encode(pwd2)

if __name__ == '__main__':
   password = '0000'
   md5pwd=md5Encode(password)
   print(md5pwd)
   
   md5pwd2=md5SaltEncode(password)
   print(md5pwd2)
