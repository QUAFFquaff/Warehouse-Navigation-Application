from UI.login import Login_UI
from UI.main_window import Main_UI
from UI.profile import Profile_UI
import utils.LoggerFactory as LF
from PyQt5.QtWidgets import *
from objs.WareHouse import *

def abort(*args):
    for window in args:
        window.close()
    sys.exit(0)

if __name__ == "__main__":
    logger=LF.get_logger(__name__)
    logger.info("main start")
    app = QApplication(sys.argv)

    logger.info("init UI windows")
    login_window = Login_UI()
    profile_window = Profile_UI()
    main_window = Main_UI()

    logger.info("set up UI windows")
    login_window.setupUi(login_window)
    profile_window.setupUi(profile_window)
    main_window.setupUi(main_window)

    login_window.init()
    profile_window.init()
    main_window.set_profile_window(profile_window)
    main_window.init()

    # init objs
    wh = WareHouse()
    wh.set_dhandler()

    # set warehouse
    profile_window.set_warehouse(wh)
    main_window.set_warehouse(wh)

    # fake username password for testing
    login_window.username_input.setText("alicebob")
    login_window.password_input.setText("123456")

    if login_window.exec_()==QDialog.Accepted:
        password=login_window.password_input.text()
        profile_window.lineEdit_password_input1.setText(password)
        profile_window.lineEdit_password_input2.setText(password)
        # TODO: validate username password
        # login validation should be done in login_window, not here
        # QMessageBox.information(login_window,"Info", "Login successful！", QMessageBox.Yes, QMessageBox.Yes)
        # if profile_window.exec_()==QDialog.Accepted:
        #     profile_params=profile_window.get_params()
        #     main_window.params=profile_params
        main_window.show()
        sys.exit(app.exec_())
    abort(login_window, profile_window, main_window)