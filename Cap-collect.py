import sys
import getpass
import os
# import pexpect
# import Capture
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory, QTreeWidgetItem
from src.Pkt_UI import Pkt_Ui_MainWindow
from src.Login import Login_Ui_MainWindow


class MyMainForm(QMainWindow, Login_Ui_MainWindow):
    _signal_1 = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.originalPalette = QApplication.palette()
        self.changeStyle('Windows')

        self.pkt_link = Pkt_Ui()
        self._signal_1.connect(self.pkt_link.get_data)

        self.start_trace.clicked.connect(self.pkt_tracer)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(self.originalPalette)

    def pkt_tracer(self):
        self.hide()
        self.pkt = Pkt_Ui()
        self._signal_1.emit(self.node_input.text(), self.ns_input.text())


class Pkt_Ui(QMainWindow, Pkt_Ui_MainWindow):
    _signal = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(Pkt_Ui, self).__init__(parent)
        self.setupUi(self)

        self.start_btn.clicked.connect(self.start_capture)
        self.back_btn.clicked.connect(self.login)
        self.stop_btn.clicked.connect(self.stop_save)
        self.saved_files.itemDoubleClicked.connect(self.openWS)

    def get_data(self, node_name, namespace):
        self.hide();
        self.namespace = namespace
        self.dal_blade = "pccc-tool-203-11-1"
        # self.dal_blade = Capture.get_pcc_dallas_master_blade(node_name)
        self.node_name.setText(QtCore.QCoreApplication.translate("MainWindow", node_name))
        hello = self.label.text() + node_name
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow", hello))
        self.dal_name.setText(self.dal_blade)
        self.show()

    def start_capture(self):
        username = getpass.getuser()
        sut = self.product_name.currentText()
        if self.node_name.isChecked():
            capture_obj = "node"
            self.logBroswer.append("Starting capture on node " + self.node_name.text() + 
            "\n using " + self.node_cap.currentText() + "\n filtered by " + self.node_filter.text())
            # Capture.capture_start(self.node_name.text(), self.dal_blade, self.node_filter.text(), self.namespace, sut, username, capture_obj, self.node_cap.currentText())

        if self.dal_name.isChecked():
            capture_obj = "dallas"
            self.logBroswer.append("Starting capture on Dallas machine " + self.dal_blade
            + "\n using " + self.dal_cap.currentText() + "\n filtered by " + self.dal_filter.text())
            # Capture.capture_start(self.node_name.text(), self.dal_blade, self.dal_filter.text(), self.namespace, sut, username, capture_obj, self.dal_cap.currentText())

        self.logBroswer.append("Capture is ongoing, plz wait................")
        self.logBroswer.append("--------------------------------------------")


    def stop_save(self):
        self.stop_trace()
        self.savePkts()

    def stop_trace(self):
        if self.node_name.isChecked():
            self.logBroswer.append("Stopping capture on node " + self.node_name.text())
        if self.dal_name.isChecked():
            self.logBroswer.append("Stopping capture on Dallas " +  self.dal_blade)
        # self.savedPath = Capture.capture_stop()

    def savePkts(self):
        self.savedPath = ["/lab/epg_st_sandbox/eshibij/filename", "/lab/epg_st_sandbox/eshibij/path2", "/lab/epg_st_sandbox/eshibij/path3"]
        self.parentPath = '/'.join(self.savedPath[0].split('/')[:-1]) + '/'
        self.logBroswer.append("Saving packets under " + self.parentPath)
        self.listPath()
    
    def listPath(self):
        root = QTreeWidgetItem(self.saved_files)
        root.setText(0, self.parentPath)
        for path in self.savedPath:
            file_name = path.split("/")[-1]
            child = QTreeWidgetItem()
            child.setText(0, file_name)
            root.addChild(child)

    def openWS(self, item):
        """open wireshark here"""
        target = self.parentPath + "capture/" + item.text(0)
        cmd = "/lab/j20/testtools/onewireshark " + target
        # os.system(cmd)
        print("open wireshark")
        print(target)

    def login(self):
        self.hide()
        self.li = MyMainForm()
        self.li.show()


def main():
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
