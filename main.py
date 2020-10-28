from UI.login import Login_UI
from UI.main_window import Main_UI
from UI.profile import Profile_UI
import sys
from PyQt5.QtWidgets import *


def abort(*args):
    for window in args:
        window.close()
    sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = Login_UI()
    profile_window = Profile_UI()
    main_window = Main_UI()

    login_window.setupUi(login_window)
    profile_window.setupUi(profile_window)
    main_window.setupUi(main_window)

    if True:#login_window.exec_()==QDialog.Accepted:
        # TODO: validate username password
        # login validation should be done in login_window, not here
        # QMessageBox.information(login_window,"Info", "Login successful！", QMessageBox.Yes, QMessageBox.Yes)
        if True:#profile_window.exec_()==QDialog.Accepted:
            login_window.exec_()
            profile_window.exec_()
            main_window.show()
            sys.exit(app.exec_())
    abort(login_window, profile_window, main_window)