#!/usr/bin/env python3
#coding:utf-8
import os, binascii, struct
from Crypto.Cipher import AES

pad = lambda m: m + bytes([16 - len(m) % 16] * (16 - len(m) % 16))
def haggis(m):
    crypt0r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))

    print(len(m).to_bytes(0x10, 'big')+ pad(m))
    print(crypt0r.encrypt(len(m).to_bytes(0x10, 'big') + pad(m))[-0x10:])
    crypt0r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))
    return crypt0r.encrypt(len(m).to_bytes(0x10, 'big') + pad(m))[-0x10:] #

target = binascii.unhexlify('e946328273904b9702dc375bc1b5e18c')
#target = os.urandom(0x10) #随机产生一个32位长度的字符串
print(binascii.hexlify(target).decode())



true_msg = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@I solemnly swear that I am up to no good.\0qwerty';
crypt1r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))

enc_true = '\xdd\x90\x17\xa0\xc8\xec\xb9\xcc\x19A\x96\xa5\xde\xf3f\x8e'

dd = '\x97;\xd6_\xf7\xdc\xe4\xa1\x97\xb9.o"\xbd\x11\xaa'
print(len(dd))

'''
###################################                            --------1第一次解密随机字符串
'''
ddb = binascii.unhexlify('e946328273904b9702dc375bc1b5e18c')

crypt2r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))
dd_de = crypt2r.decrypt(ddb)

'''
###################################                            --------2转换结果dd_de(byte)->dd(str)
'''
print(dd_de)

last = '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
encrypted = [ hex(ord(a) ^ ord(b)) for (a,b) in zip(dd, last) ]
print(''.join(encrypted))


'''
###################################                           --------3第一次异或得到第二段密文
'''
ddb2 = b'\x87\x2b\xc6\x4f\xe7\xcc\xf4\xb1\x87\xa9\x3e\x7f\x32\xad\x01\xba'


crypt3r = AES.new(bytes(0x10), AES.MODE_CBC, bytes(0x10))
dd2_de = crypt3r.decrypt(ddb2)
'''
###################################                           --------4第二次解密
'''
print(dd2_de)
dd2 = '\x92]\xf5\xbe\x84\xa4\xe7t\x1a\x86\xe9\xc2\xb8l\x0c\xce'
encrypted = [ hex(ord(a) ^ ord(b)) for (a,b) in zip(enc_true, dd2) ]
print(''.join(encrypted))

'''
###################################                           --------5第二次异或得到构造字符串
'''
ss = b'I solemnly swear that I am up to no good.\0qwerty\x4f\xcd\xe2\x1e\x4c\x48\x5e\xb8\x03\xc7\x7f\x67\x66\x9f\x6a\x40'
ma = binascii.hexlify(ss).decode()
print(ma)


msg = binascii.unhexlify(ma)
#msg = binascii.unhexlify(input())
print(msg)

if msg.startswith(b'I solemnly swear that I am up to no good.\0') \
        and haggis(msg) == target:
    #print(open('flag.txt', 'r').read().strip())
    print("yes")

# hxp{PLz_us3_7h3_Ri9h7_PRiM1TiV3z}
