import easygui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

#Kayarmin Mir
def error_wrong_information (a):
       e=''
       t=0
       for i in range (len(a)):
           if a[i]!='1' and a[i]!='2' and a[i]!='3' and a[i]!='4' and a[i]!='5' and a[i]!='6' and a[i]!='7' and a[i]!='8' and a[i]!='9' and a[i]!='0':
               return 'no'
           if a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9' or a[i]!=' ':
               e=e+a[i]
       if 0<=int(e)<=360:
           return 'yes'
       if int(e)<0 or int(e)>360:
           return 'no'
  
#Kayarmin Mir      
def chek_reshte_khali_ya_na(vorody):
           reshte_nadorost='no'
           alphabet_ba_adad_ha=('1234567890qwertyuiopasdfghjklzxcvbnm')
           for e in range (len(vorody)):
               khane=vorody[e]
               for i in range (len(alphabet_ba_adad_ha)):
                   if khane!=alphabet_ba_adad_ha[i]:
                      reshte_nadorost='yes'
                      return 'no'
           return 'yes'

#Mohammad Matin Younesnia
def insert():
    option = QFileDialog.Options()
    widget = QWidget()
    myfile = QFileDialog.getOpenFileName(widget,'save file','default.jpg','JPEG (*.jpg;*jpeg;*.jpe;*.jfif);;PNG (*.png)', options = option)
    print(myfile)
    return myfile[0]

#Mohammad Matin Yoinesnia
def export():
    option = QFileDialog.Options()
    widget = QWidget()
    myfile = QFileDialog.getSaveFileName(widget,'save file','default.jpg','JPEG (*.jpg;*jpeg;*.jpe;*.jfif);;PNG (*.png)', options = option)
    #print(myfile)
    return myfile[0]

#Kayarmin Mir
def rotate():
    p='no'
    while p=='no' :
        m=easygui.enterbox('enter a input from 0 to 360','details')
        if m==None:
           easygui.msgbox('error you must inter input please try again','error in information', 'Retry')
        elif chek_reshte_khali_ya_na(m)=='yes':
            p='no'
            easygui.msgbox('error you input is incorrect please try again','error in information', 'Retry')
        elif error_wrong_information(m)=='no':
            p='no'
            easygui.msgbox('error you input is incorrect please try again','error in information', 'Retry')
        elif error_wrong_information(m)=='yes':
            p='yes'
    return m
#kayarmin Mir
def colour_edit():
   p='yes'
   w='e'
   w=easygui.buttonbox('chose one of them','favorite work',('black and white','blue','red','green'))
   while p=='yes' :
      if w==None:
         easygui.msgbox('error you must choose one of them please try again','error in information', 'Retry')
         w=easygui.buttonbox('chose one of them','favorite work',('black and white','blue','red','green'))
      if w!=None:
         p='no'
   p='no'
   while p=='no' :
        m=easygui.enterbox('enter a input from 0 to 255','details')
        if m==None:
           easygui.msgbox('error you must inter input please try again','error in information', 'Retry')
        elif chek_reshte_khali_ya_na(m)=='yes':
            p='no'
            easygui.msgbox('error you input is incorrect please try again','error in information', 'Retry')
        elif error_wrong_information(m)=='no':
            p='no'
            easygui.msgbox('error you input is incorrect please try again','error in information', 'Retry')
        elif error_wrong_information(m)=='yes':
            p='yes'
   kar_nahaye=[w,m]
   return kar_nahaye
#and the rest by Parsa Mostaghimi
def flip ():
     output1=easygui.ynbox(' ','Flip',('                  Vertical                  ','                   Horizontal                  '))
     return output1

def mirror ():
      output1=easygui.buttonbox(' ','mirror',('mirror_right_left','mirror_left_right','mirror_bottom_top','mirror_top_bottom'))
      return output1 

def detail (n):
     mt=easygui.msgbox(n,'Detail','                           ok                            ')
