from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtDBus import QDBusConnection

class CursorReceiver(QObject):
	# the signal handler, the callback is set by the user later
	cursorPosChanged = pyqtSignal(int, int)

	def __init__(self):
		super().__init__()

	@pyqtSlot(int, int)  # sets the expected input parameter for the dbus method
	def Send(self, x, y):  # the method invoced in python
		# We can simply emit a signal with the coordinates, that enables us to connect
		# to cursorPosChanged later with a custom function
		self.cursorPosChanged.emit(x, y)

# sets up the service, see ListenerExample.py for more details
class Listener:
	def __init__(self):
		self.receiver = CursorReceiver()
		self.conn = QDBusConnection.sessionBus()
		self.conn.registerService("org.pythonmacro.Cursor")
		self.conn.registerObject("/", self.receiver, QDBusConnection.RegisterOption.ExportAllSlots)
