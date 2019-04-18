# coding : utf8

import base64
import re
import email

def safe_base64_decode(s):
    while len(s) % 4 > 0:
        s += b'='
    return base64.b64decode(s)

def is_base64_code(s):
    '''Check s is Base64.b64encode'''
    if not isinstance(s ,str) or not s:
        # raise ValueError, "params s not string or None"
        raise ValueError

    _base64_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                    'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
                    '2', '3', '4','5', '6', '7', '8', '9', '+',
                    '/', '=' ]

    # Check base64 OR codeCheck % 4
    code_fail = [ i for i in s if i not in _base64_code]
    if code_fail or len(s) % 4 != 0:
        return False
    return True

a = """
=?UTF-8?B?RndkOiBb6Zu75a2Q6ZaA56WoXSDoib7lvrforYnliLjmnJ/osqjjgIrlpoLkvZXkvJg=?=

    =?UTF-8?B?6ZuF55qE5YyW6Kej5bC05bCs44CLLSAwMeaciDE25pelKOaYn+acn+S4iSk=?=
"""
b = 'hello'
# "^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$"
s = is_base64_code(a)
print(s)
print(email.header.decode_header(a))

