Set objshell=CreateObject("Wscript.Shell")
objShell.CurrentDirectory = Wscript.Arguments.item(0)
objShell.Run("git annex assistant --autostart"), 0, False
