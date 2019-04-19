set test = CreateObject("WScript.Shell")
test.SendKeys"+{INSERT}"

WScript.Sleep 250

Dim objShell
Set objShell = WScript.CreateObject( "WScript.Shell" )
objShell.Run("""C:\Users\cools\OneDrive\Documents\Lightshot\dist\main.exe""")
Set objShell = Nothing
WScript.Sleep 500