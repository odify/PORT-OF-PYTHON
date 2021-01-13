# import os
# import ctypes
# os.system('color a')

# a=raw_input('\n\t\t\t\t\t    Press  e to  ENABLE USB PORT \n\t\t\t\t\t    press  d to DISABLE USB PORT\n\n\t\t\t\t\t\t Enter your choice: ')


# if a=='e' or a=='E':
# 	os.system('reg add HKLM\SYSTEM\CurrentControlSet\Services\UsbStor /v "Start" /t REG_DWORD /d "3" /f')
# 	ctypes.windll.user32.MessageBoxA(0,"USB is enabled","Message",ICON_INFO)
# 	exit(0)


# if a=='d' or a=='D':
# 	os.system('reg add HKLM\SYSTEM\CurrentControlSet\Services\UsbStor /v "Start" /t REG_DWORD /d "4" /f')
# 	ctypes.windll.user32.MessageBoxA(0,"USB is disabled ","Message",ICON_INFO)
# 	exit(0)


# else:
# 	ctypes.windll.user32.MessageBoxA(0,"Wrong input","Message",ICON_INFO)
# 	exit(0)
