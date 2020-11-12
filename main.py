# this file mostly had been written by behrad mirzapoor 
#but a little corraction had been done by mohammad matin younesnia
#Mohammad Matin just write mr def and add img.show end of some defs. 
#and some of this part (about 60%) had been designed with app Qt Designer.

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL.ImageQt import ImageQt

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys 
from PIL import Image
import functions
import colour_effect
import os
import easygui
flag = False

img=''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(320, 70, 521, 271))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionGray_scale = QtWidgets.QAction(MainWindow)
        self.actionGray_scale.setObjectName("actionGray_scale")
        self.actionColour_edit = QtWidgets.QAction(MainWindow)
        self.actionColour_edit.setObjectName("actionColour_edit")
        self.actionNegative = QtWidgets.QAction(MainWindow)
        self.actionNegative.setObjectName("actionNegative")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionFlip = QtWidgets.QAction(MainWindow)
        self.actionFlip.setObjectName("actionFlip")
        self.actionMirror = QtWidgets.QAction(MainWindow)
        self.actionMirror.setObjectName("actionMirror")
        self.actionDetail = QtWidgets.QAction(MainWindow)
        self.actionDetail.setObjectName("actionDetail")
        
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionGray_scale)
        self.menuEdit.addAction(self.actionColour_edit)
        self.menuEdit.addAction(self.actionNegative)
        self.menuEdit.addAction(self.actionRotate)
        self.menuEdit.addAction(self.actionFlip)
        self.menuEdit.addAction(self.actionMirror)
        self.menuEdit.addAction(self.actionDetail)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "edit_picture"))

        self.label.setText(_translate("MainWindow", "welcome!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionGray_scale.setText(_translate("MainWindow", "Gray scale"))
        self.actionColour_edit.setText(_translate("MainWindow", "Colour edit"))
        self.actionNegative.setText(_translate("MainWindow", "Negative"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionFlip.setText(_translate("MainWindow", "Flip"))
        self.actionMirror.setText(_translate("MainWindow", "Mirror"))
        self.actionDetail.setText(_translate("MainWindow", "Detail"))
        self.actionHelp.setText(_translate("MainWindow", "help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Tips for using program"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))

        self.actionNew.triggered.connect(lambda: self.insert('open'))
        self.actionSave.triggered.connect(lambda: self.export('Save'))
        self.actionHelp.triggered.connect(lambda: self.help('Help'))
        self.actionGray_scale.triggered.connect(lambda: self.gs('gs'))
        self.actionColour_edit.triggered.connect(lambda: self.ce('ce'))
        self.actionNegative.triggered.connect(lambda: self.ne('ne'))
        self.actionRotate.triggered.connect(lambda: self.re('re'))
        self.actionFlip.triggered.connect(lambda: self.fp('fp'))
        self.actionMirror.triggered.connect(lambda: self.mr('mr'))
        self.actionDetail.triggered.connect(lambda: self.dl('dl'))

    def show_picture(self,img):
        self.label.setPixmap(QtGui.QPixmap(img))
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 430))
        os.remove('trash.jpg')

    def insert(self,text):
        global img
        try:
            img=Image.open(functions.insert())
            img.save("trash.jpg")
            self.show_picture('trash.jpg')
            global flag
            flag = True
        except:
            pass
        return

    def export(self,text):
        global img
        global flag
        try:
            if flag:
                img.save(functions.export())
            else:
                mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')
        except:
            pass

    def gs(self,text):
        global img
        global flag
        if flag:
            img=colour_effect.grayscale(img)
            img.save("trash.jpg")
            self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')

    def ce (self,text):
        global img
        global flag
        if flag:
            x=functions.colour_edit()

            if x[0] =='green':
                img=colour_effect.greeninstaa(img)
                img.save("trash.jpg")
                self.show_picture('trash.jpg')
            if x[0] =='red':
                img=colour_effect.redinstaa(img)
                img.save("trash.jpg")
                self.show_picture('trash.jpg')
            if x[0] =='blue':
                img=colour_effect.blueinstaaa(img)
                img.save("trash.jpg")
                self.show_picture('trash.jpg')
            if x[0] =='black and white':
                img=colour_effect.colour_edit(img)
                img.save("trash.jpg")
                self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')

    def ne(self,text):
        global img
        global flag
        if flag:
            img=colour_effect.negative(img)
            img.save("trash.jpg")
            self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')
        


    def re(self,text):
        global img
        global flag
        if flag:
            img=colour_effect.rotated(img,int(functions.rotate()))
            img.save("trash.jpg")
            self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')


    def fp(self,text):
        global img
        global flag
        if flag:
            x=functions.flip()
            if x:
                img=colour_effect.flip_top_bottom(img)
            else:
                img=colour_effect.flip_left_right(img)
            img.save("trash.jpg")
            self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')
        


    def mr(self,text):
        global img
        global flag
        if flag:
            x=functions.mirror()
            
            if x == 'mirror_right_left':
                img=colour_effect.mirror_right_left(img)

            elif x == 'mirror_left_right':
                img=colour_effect.mirror_left_right(img)

            elif x == 'mirror_bottom_top':
                img=colour_effect.mirror_bottom_top(img)

            elif x == 'mirror_top_bottom':
                img=colour_effect.mirror_top_bottom(img)

            img.save("trash.jpg")
            self.show_picture('trash.jpg')
        else:
            mt=easygui.msgbox('You do not insert any file, please open a file and try again','Detail','                           ok                            ')
        
        

    def help (self,test):
        easygui.msgbox('Help \n                                    address:\n __Click on file icon then click on new icon and type your picture URL\n                                     save\n__Click on file icon then click on save icon and type a name that you want to save your picture with this name\n                                   color_edit:\n__use this to do some edits like color_edits(Black and white , blue_white , red_white , green_white) , mirror(Mirror_left_right , Mirror_top_bottom) , flip (Flip_top_bottom , Flip_left_right)  or give you some information about your picture such as detail or matt your picture such as Blur\n _ Rotate: if you want that your photo be rotate, in the box, program will ask you the degree of rotation (round clock)                                           Exit:\n__if you want to exit programe click on the red cross up_left of programe','Help','OK')  


    def dl(self,text):
        global img
        if flag:
            functions.detail(colour_effect.detail(img))
    
#MainWindow_x = 100 ; MainWindow_y = 170 ; MainWindow_w = 800 ; MainWindow_h = 400

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.setGeometry(MainWindow_x,MainWindow_y,MainWindow_w,MainWindow_h)
    MainWindow.show()
    sys.exit(app.exec_())
