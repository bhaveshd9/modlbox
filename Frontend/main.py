import sys
import os
import msvcrt
import time
from PySide6.QtWidgets import QApplication
from MainWindow import SplashScreen

# Define the lock file path
lock_file = 'app.lock'

# Attempt to create and open the lock file
try:
    lock_fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_RDWR)
except OSError:
    print("Another instance is already running. Exiting.")
    sys.exit(1)

# Create the QApplication instance
app = QApplication(sys.argv)

# Create and show the SplashScreen window
window = SplashScreen()
window.show()

# Remove the lock file when the application exits
def cleanup():
    os.close(lock_fd)
    os.remove(lock_file)

# Connect the aboutToQuit signal to the cleanup function
app.aboutToQuit.connect(cleanup)

# Execute the application event loop
sys.exit(app.exec())
