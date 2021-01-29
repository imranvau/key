import os
from time import sleep

#by Imran vau

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(b+'\t    
  _____                            __      __         
 |_   _|                           \ \    / /         
   | |  _ __ ___  _ __ __ _ _ __    \ \  / /_ _ _   _ 
   | | | '_ ` _ \| '__/ _` | '_ \    \ \/ / _` | | | |
  _| |_| | | | | | | | (_| | | | |    \  / (_| | |_| |
 |_____|_| |_| |_|_|  \__,_|_| |_|     \/ \__,_|\__,_|                                                                                                           

')
print(a+'\t  Shorcut for help you')
print(b+'\t  with  Imran vau')
print('\t http://bit.ly/S4vLs')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] making termux properties directory with imran vau..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file for your termux..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success buddy!')
sleep(1)
print(b+'\n[!] Please wait Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Setup Success by imran vau!!')


