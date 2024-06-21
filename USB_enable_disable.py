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
import configparser

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("USB_enable_disable.ini")

# Присваиваем значения внутренним переменным
_default = config['Default']['_default']

_reboot = config[_default]['_reboot']
_restart = config[_default]['_restart']
_yes = config[_default]['_yes']
_no = config[_default]['_no']

_menu = config[_default]['_menu']
_allow_usb = config[_default]['_allow_usb']
_deny_usb = config[_default]['_deny_usb']
_language = config[_default]['_language']
_about = config[_default]['_about']
_exit = config[_default]['_exit']
_set_allow_usb = config[_default]['_set_allow_usb']
_set_deny_usb = config[_default]['_set_deny_usb']
_reboot_pc = config[_default]['_reboot_pc']

_press_enter = config[_default]['_press_enter']
_exit_prog = config[_default]['_exit_prog']
_run_as_admin = config[_default]['_run_as_admin']


filename = 'USB_enable_disable.ini'
lines = []
with open(filename) as file:
    while line := file.readline():
        if '[' in line.strip():
            if 'Default' not in line.strip():
                line = line.strip()
                line = line.strip('[')
                line = line.strip(']')
                lines.append(line)

def confirm_reboot(key):
	q = [
		inquirer.List("reboot", message=key+"\n\n" + _reboot, choices=[_yes, _no], default = _yes),
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
                          message=_menu,
                          choices=[_allow_usb, _deny_usb, _language, _about, _exit])
        ]
        choice = prompt(questions)['choice']

        if choice == _allow_usb:
            USB_allow_deny(0)
            if confirm_reboot(_set_allow_usb)['reboot'] == _yes:
                subprocess.Popen('shutdown.exe /r /t 120 /c ' + _reboot_pc)

        elif choice == _deny_usb:
            USB_allow_deny(1)
            if confirm_reboot(_set_deny_usb)['reboot'] == _yes:
                subprocess.Popen('shutdown.exe /r /t 120 /c ' + _reboot_pc)

        elif choice == _language:
            questions = [
                inquirer.List("language", message="Language", choices = lines, carousel = True),
            ]
            answers = inquirer.prompt(questions)
            #print (answers)
            #print (answers['language'])
            if answers['language'] == '<-----':
                pass
            else:
                config.set('Default', '_default', answers['language'])
                with open('USB_enable_disable.ini', 'w') as config_file:
                    config.write(config_file)

                input('\n ' + '\n ' + _restart + '\n ' + '\n ' + _press_enter)


        elif choice == _about:
            print("#-------------------------------------------------------------------------------")
            print("# Name:        USB_enable_disable.py")
            print("# Purpose:     USB allow/deny from command line")
            print("# Author:      sysuev.va")
            print("# e-mail:      sysuev.va@gidroagregat.ru, vladsyss@ya.ru")
            print("# Created:     20.06.2024")
            print("# Copyright:   (c) sysuev.va 2024")
            print("# Licence:     GPL-3.0 license ")
            print("#-------------------------------------------------------------------------------")
            input ('\n' + _press_enter)

        elif choice == _exit:
            print(_exit_prog)
            break


if is_admin():
    _main()
else:
    _clear()
    print ('\n ' + _run_as_admin)
    input('\n ' + _press_enter)
