
import socket
import chg400ui
from PyQt5 import QtCore, QtGui, QtWidgets


def chgdate():
    HOST = '10.160.2.150'
    PORT = 10001
    data = " "

    if ui.lineEdit.text() == "":
        retinfo = "返回信息：必输项不允许为空！"
        ui.label_10.setText(retinfo)
        return

    if ui.radioButton_2.isChecked() == True:
        HOST = '10.160.2.153'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(30)
    # if s.connect_ex((HOST, PORT)) != 0
    #     retinfo = "返回信息：服务器连接失败！"
    #     ui.label_10.setText(retinfo)
    #     return
    try:
       s.connect((HOST, PORT))
    except:
        retinfo = "返回信息：服务器连接失败！"
        ui.label_10.setText(retinfo)
        return

    if  ui.lineEdit_2.text() != "":
        txno = "0001"
        lib = ui.lineEdit.text()
        date = ui.lineEdit_2.text()
        data = "+0018" + txno + date + lib
    else:
        txno = "0003"
        lib = ui.lineEdit.text()
        date = "99991231"
        data = "+0018" + txno + date + lib

    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    retinfo = "返回信息：" + data.decode('utf-8')[5:-1]
    ui.label_10.setText(retinfo)
    #print("获取服务器信息：\n", data.decode('utf-8'))
    # data = input('请输入信息：\n')
    s.close()

def button_clicked():
    #清空标签信息
    ui.pushButton.clicked.connect(ui.label_10.clear)
    ui.pushButton_2.clicked.connect(ui.label_11.clear)

    #ui.pushButton.setText("按钮被点击")
    #调用访问400函数
    ui.pushButton.clicked.connect(chgdate)


def ui_addattribute():
    ui.label_10.setWordWrap(True)      #设置为可自动换行
    ui.label_11.setWordWrap(True)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = chg400ui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    #增加UI属性
    ui_addattribute()
    #设置点击button动作
    button_clicked()

    MainWindow.show()
    sys.exit(app.exec_())
