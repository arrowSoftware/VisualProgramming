from DragWidget import BranchWidget
import sys
from PySide6 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):      
        self.setAcceptDrops(True)

        self.btn = BranchWidget(self)
        self.btn.move(300, 65)
        self.btn2 = BranchWidget(self)
        self.btn2.move(100, 65)

        self.p1 = self.btn.pos()
        self.p2 = self.btn2.pos()

        self.btn.installEventFilter(self)
        self.btn2.installEventFilter(self)

        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('Click or move')
        self.show()

    def eventFilter(self, o, e):
        if e.type() == QtCore.QEvent.Move:
            if o is self.btn:
                self.p1 = self.btn.pos()
            elif o is self.btn2:
                self.p2 = self.btn2.pos()
            self.update()

        return super().eventFilter(o, e)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.drawLine(self.p1, self.p2) 
        return super().paintEvent(event)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        dropItem = e.source()
        position = e.pos() - dropItem.drag.hotSpot()
        print("dropEvent: %s %s" % (e.pos(), dropItem.drag.hotSpot()))
        dropItem.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()

    sys.exit(app.exec())