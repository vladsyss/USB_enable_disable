import keyboard
import ctypes, sys
from time import sleep
 
def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
 
if is_admin():
	print ("\n Pess 1 or 2 or 3 to execute\n\n 1 - USB_allow_read_write_execute\n 2 - USB_deny_read_write_execute\n 3 - exit")

	while True:
		if keyboard.read_key() == "1":
			print("You pressed 1")
			time.sleep(1)
			#break
			sys.exit()
		if keyboard.read_key() == "2":
			print("You pressed 2")
			time.sleep(1)
			#break
			sys.exit()
		if keyboard.read_key() == "3":
			print("You pressed 3")
			time.sleep(1)
			#break
			sys.exit()

else:
	# Call the same script ar another one with Admin's Privileges
	# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	#ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, 'USB_enable_disable.exe', None, 1)

	print ("\nYou must run as Administrator")
	print ("\nPress Esc to exit")
	#sys.stdin.readline()
	keyboard.wait('esc')