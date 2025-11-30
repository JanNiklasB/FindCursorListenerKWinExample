from DBusListener import *
import PyQt6.QtWidgets as pyqt
import subprocess

from pathlib import Path
PATH = Path(__file__).parent.resolve()

# just sets the window for this example:
class Window(pyqt.QMainWindow):
	def __init__(self):
		super().__init__()

		# Window Title
		self.setWindowTitle("Listener Example")
		# Window
		mainWidget = pyqt.QWidget()
		self.setCentralWidget(mainWidget)
		# Layout
		layout = pyqt.QHBoxLayout()
		mainWidget.setLayout(layout)

		# set readonly position box
		PosPanel = pyqt.QWidget()
		PosLayout = pyqt.QHBoxLayout(PosPanel)
		self.PosLabel = pyqt.QLineEdit()
		self.PosLabel.setReadOnly(True)
		PosLayout.addWidget(self.PosLabel)

		layout.addWidget(PosPanel)

	def setCursorPos(self, x, y):
		self.PosLabel.setText(f"x={x}, y={y}")

if __name__ == "__main__":
	# start a QCoreApplication (also works with QCoreApplication, but only one at a time)
	app = pyqt.QApplication([])

	# init window:
	window = Window()

	# define the receiver class, this contains the signal handler 
	# which calls a callback function that is set later
	receiver = CursorReceiver()

	# set the callback:
	receiver.cursorPosChanged.connect(window.setCursorPos)

	# setup the service, the interface can also be generated, but is generated here by KWin to locale.ListenerExample.Send
	conn = QDBusConnection.sessionBus()
	conn.registerService("org.pythonmacro.Cursor")
	conn.registerObject("/", receiver, QDBusConnection.RegisterOption.ExportAllSlots)

	# # now we need to load the script into kwin, for that a simple bash script can be used:
	Output = subprocess.run(f"sh {str(PATH)}/startCursorListener.sh", shell=True, capture_output=True)
	# # to close the script correctly later we need to capture the script number:
	KWinScriptNumber = int(Output.stdout.decode())

	# show window:
	window.show()

	app.exec()

	# no unload the script which we generated earlier
	subprocess.run(f"sh {str(PATH)}/stopCursorListener.sh {KWinScriptNumber}", shell=True)