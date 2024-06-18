from pynput import keyboard
# How to clear input while using keyboard module
import msvcrt as kb # https://stackoverflow.com/questions/64727578/how-to-clear-input-while-using-keyboard-module
import winreg
import ctypes, sys
 
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
 
def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        while kb.kbhit(): kb.getch()
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

        while kb.kbhit(): kb.getch()
        return False

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

        while kb.kbhit(): kb.getch()
        return False


if is_admin():
	print ("\n Pess 1 or 2 or 3 to execute\n\n 1 - USB_allow_read_write_execute\n 2 - USB_deny_read_write_execute\n Esc - exit")
else:
	# Call the same script ar another one with Admin's Privileges
	# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	#ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, 'USB_enable_disable.exe', None, 1)
	print ("\nYou must run as Administrator")
	print ("\nPress Esc to exit")
 

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
