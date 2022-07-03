from PySide6 import QtCore, QtWidgets, QtGui

class DragWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(DragWidget, self).__init__(parent)
        self.setStyleSheet("background-color: rgb(255,255,255); border:1px solid rgb(0, 0, 0); ")

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()
        pixmap = self.grab()
        self.drag = QtGui.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.setPixmap(pixmap)
        self.drag.exec_(QtCore.Qt.MoveAction)


    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            print('press')

class BranchWidget(DragWidget):
    def __init__(self, parent=None):
        super(BranchWidget, self).__init__(parent)
        
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QtWidgets.QLabel("Branch"), 0, 0, 1, 2)
        self.layout.addWidget(QtWidgets.QLabel("Trigger"), 1, 0)
        self.layout.addWidget(QtWidgets.QLabel("Condition"), 2, 0)
        self.layout.addWidget(QtWidgets.QLabel("True"), 1, 1)
        self.layout.addWidget(QtWidgets.QLabel("False"), 2, 1)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 150, 100)

        self.path = QtGui.QPainterPath()
"""
    def mousePressEvent(self, e):
        print("HERE")
        if self.path.elementCount() == 0:
            self.path.moveTo(e.pos())
        else:
            self.path.lineTo(e.pos())
        self.update()
        super().mousePressEvent(e)
 
    def paintEvent(self, ev):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.black, 5)
        qp.setPen(pen)
        qp.drawPath(self.path)

        brush = QtGui.QBrush(QtCore.Qt.black)
        qp.setBrush(brush)

        for i in range(self.path.elementCount()):
            e = self.path.elementAt(i)
            qp.drawEllipse(QtCore.QPoint(e.x, e.y), 5, 5)
"""