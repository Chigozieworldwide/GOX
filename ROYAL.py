#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ROYAL64.so ROYAL32.so')
except:
    pass
os.system('rm -rf ROYAL64.so ROYAL32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ROYAL64.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/executable/blob/main/ROYAL64.cpython-311.so?raw=true -o ROYAL64.so') 
        import ROYAL64
    else:
        import ROYAL64

elif bit == '32bit':
    if not os.path.isfile('ROYAL32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/executable/blob/main/ROYAL32.cpython-311.so?raw=true -o ROYAL32.so') 
        import ROYAL32
    else:
        import ROYAL32
