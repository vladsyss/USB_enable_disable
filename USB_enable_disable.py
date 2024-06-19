from pynput import keyboard
from pynput.keyboard import Key, Controller
# How to clear input while using keyboard module
import msvcrt as kb # https://stackoverflow.com/questions/64727578/how-to-clear-input-while-using-keyboard-module
import winreg
import ctypes, sys
import os
import subprocess
 
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def clear_keyboard_buffer():
    _keyboard = Controller()
    _keyboard.press(Key.esc)
    _keyboard.release(Key.esc)

def y_n():

    def on_release2(key):
        print('{0} released'.format(key))
        if key == keyboard.KeyCode.from_char('y'):
            subprocess.Popen('shutdown.exe /r /t 60 /c "Компьютер будет перезагружен через 60 секунд. Сохраните свои документы!"')
            clear_keyboard_buffer()
            # Stop listener
            #return False
            sys.exit()
        if key == keyboard.KeyCode.from_char('n'):
            clear_keyboard_buffer()
            # Stop listener
            #return False
            sys.exit()
    # Collect events until released
    with keyboard.Listener(
            #on_press=on_press,
            on_release=on_release2) as listener:
        listener.join()
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        #on_press=on_press,
        on_release=on_release2)
    listener.start()

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        clear_keyboard_buffer()
        return False

    if key == keyboard.KeyCode.from_char('1'):
        # Stop listener

        key_name = 'Deny_Read'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Execute'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Read'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Read'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 0; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)
        
        #How can I clear the interpreter console?
        #https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
        clear = lambda: os.system('cls')
        clear()

        print ('\n USB enable now (Установлено разрешение на пользование USB)')
        print ('\n\n You must reboot Windows. Reboot now? (Необходимо перезагрузить компьютер. Выполнить перезагрузку сейчас?) (Y/N)')

        y_n()
        return True

    if key == keyboard.KeyCode.from_char('2'):
        # Stop listener

        key_name = 'Deny_Read'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Execute'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Read'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{6AC27878-A6FA-4155-BA85-F98F491D4F33}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Read'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)

        key_name = 'Deny_Write'; new_val = 1; key_type = winreg.REG_DWORD; path = r'SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{F33FDC04-D1AC-4E8E-9A30-19BBD4B108AE}'
        with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, new_val)


        #How can I clear the interpreter console?
        #https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
        clear = lambda: os.system('cls')
        clear()

        print ('\n USB disable now (Установлен запрет на пользование USB)')
        print ('\n\n You must reboot Windows. Reboot now? (Необходимо перезагрузить компьютер. Выполнить перезагрузку сейчас?) (Y/N)')


        y_n()
        return True

if is_admin():
	print ("\n Pess 1 or 2 or 3 to execute\n\n 1 - USB_allow_read_write_execute\n 2 - USB_deny_read_write_execute\n Esc - exit")
else:
	# Call the same script ar another one with Admin's Privileges
	# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	#ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, 'USB_enable_disable.exe', None, 1)
	print ("\nYou must run as Administrator")
	print ("\nPress Esc to exit")
 

# Collect events until released
#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener = keyboard.Listener(on_release=on_release)
listener.start()
