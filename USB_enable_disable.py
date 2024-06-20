#-------------------------------------------------------------------------------
# Name:        USB_enable_disable.py
# Purpose:     USB allow/deny from command line
# Author:      sysuev.va
# e-mail:      sysuev.va@gidroagregat.ru, vladsyss@ya.ru
# Created:     20.06.2024
# Copyright:   (c) sysuev.va 2024
# Licence:     GPL-3.0 license 
#-------------------------------------------------------------------------------

from inquirer import prompt
import inquirer
import os
import ctypes, sys
import winreg
import subprocess


def confirm_reboot(key):
	q = [
		inquirer.List("reboot", message=key+"\n\nНеобходимо перезагрузить компьютер. Выполнить перезагрузку сейчас?", choices=["Да", "Нет"], default="Да"),
	]
	answers = inquirer.prompt(q)
	return answers

def USB_allow_deny(_key):

    key_name = 'Deny_Read'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Write'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Execute'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Read'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Write'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Read'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

    key_name = 'Deny_Write'; new_val = _key; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, key_name, 0, key_type, new_val)

def _clear():
    #How can I clear the interpreter console?
    #https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    clear = lambda: os.system('cls')
    clear()

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def _main():
    _clear()

    while True:
        questions = [
            inquirer.List('choice',
                          message="Выберите пункт меню:",
                          choices=['Разрешить USB', 'Запретить USB', 'Выход'])
        ]
        choice = prompt(questions)['choice']

        if choice == 'Разрешить USB':
            USB_allow_deny(0)
            if confirm_reboot("Установлено разрешение на пользование USB")['reboot'] == 'Да':
                subprocess.Popen('shutdown.exe /r /t 120 /c "Компьютер будет перезагружен через 120 секунд. Сохраните свои документы!"')

        elif choice == 'Запретить USB':
            USB_allow_deny(1)
            if confirm_reboot("Установлен запрет на пользование USB")['reboot'] == 'Да':
                subprocess.Popen('shutdown.exe /r /t 120 /c "Компьютер будет перезагружен через 120 секунд. Сохраните свои документы!"')

        elif choice == 'Выход':
            print("Выход из программы.")
            break

if is_admin():
    _main()
else:
    _clear()
    print ('\nЗапустите программу от имени администратора')
    input('\nНажмите Enter для продолжения...')
