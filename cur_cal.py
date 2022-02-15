

from cProfile import label
from cgitb import text
from distutils.command.build_scripts import first_line_re
import sys
import math
from unittest import main
from PyQt5 import QtWidgets            
from PyQt5 import QtGui
from PyQt5 import QtCore
import currency_api

class Mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("currency-calculator") 
        self.setGeometry(500,500,500,300)
        

        self.lbl=QtWidgets.QLabel("write here: ")
        self.cb =QtWidgets.QComboBox()
        self.cb.addItems(["$ - USD", "€ - EUR", "£ - GBP", "ƒ - frank" , "lira"])

        self.push_btn=QtWidgets.QPushButton("Convert")
        self.push_btn.clicked.connect(self.main_function)

        self.first_line_edit=QtWidgets.QLineEdit()
        self.second_line_edit=QtWidgets.QLineEdit("result")


	

   
        main_layaut=QtWidgets.QGridLayout()

        
        #widget     

        main_layaut.addWidget(self.first_line_edit,0,0)
        main_layaut.addWidget(self.cb,1,0)
        main_layaut.addWidget(self.push_btn,1,1)
        main_layaut.addWidget(self.second_line_edit,2,0)


        
        self.styling()


        widget=QtWidgets.QWidget()
        widget.setLayout(main_layaut)
        self.setCentralWidget(widget)

    #function

    


    #all function section
#usd

    def main_function(self):
        if self.cb.currentText()=="$ - USD":
            
            first_text=self.first_line_edit.text()
            if first_text.isdigit():
                self.first_line_edit.setText(first_text)
                us=currency_api.main_dict["USD"]
                us=float(us)
                result=float(first_text) * us
                self.second_line_edit.clear()
                self.second_line_edit.setText(f"{str(result)}₾")
            else:                    
                self.first_line_edit.setText("error")


#EURO

        elif self.cb.currentText()=="€ - EUR":
                first_text=self.first_line_edit.text()
                if first_text.isdigit():
                    self.first_line_edit.setText(first_text)
                    eu=currency_api.main_dict["EUR"]
                    eu=float(eu)
                    result1=float(first_text) * eu
                    self.second_line_edit.clear()
                    self.second_line_edit.setText(f"{str(result1)}₾")
                else:
                    self.first_line_edit.setText("error")

#GBP

        elif self.cb.currentText()=="£ - GBP":
            first_text=self.first_line_edit.text()
            if first_text.isdigit():
                self.first_line_edit.setText(first_text)
                ru=currency_api.main_dict["GBP"]
                ru=float(ru)
                result3=float(first_text) * ru
                self.second_line_edit.clear()
                self.second_line_edit.setText(f"{str(result3)}₾")
            else: 
                    self.first_line_edit.setText("error")


#farnk
        elif self.cb.currentText()=="ƒ - frank":
            first_text=self.first_line_edit.text()
            if first_text.isdigit():
                self.first_line_edit.setText(first_text)
                fr=currency_api.main_dict["CHF"]
                fr=float(fr)
                result3=float(first_text) * fr
                self.second_line_edit.clear()
                self.second_line_edit.setText(f"{str(result3)}₾")
            else: 
                    self.first_line_edit.setText("error")

#lira

        elif self.cb.currentText()=="lira":
            first_text=self.first_line_edit.text()
            if first_text.isdigit():
                self.first_line_edit.setText(first_text)
                lir=currency_api.main_dict["TRY"]
                lir=float(lir)
                result3=int(first_text) * lir
                self.second_line_edit.clear()
                self.second_line_edit.setText(f"{str(result3)}₾")
            else: 
                    self.first_line_edit.setText("error")





    def styling(self):
        style = """
            QMainWindow {
                background-color:#E69A8DFF	;
            }
            QPushButton {
                border-radius: 15px;
                background-color:#E69A8DFF	;
                color: #00FF00		;
                font: 20px;
            }
            QLineEdit {
                background-color:#E69A8DFF;
                color: #00FF00			;
                font: 30px bold;
                border: none;
            }
            
            }
            QComboBox {
                background-color:#E69A8DFF;
                color:#E69A8DFF;
            border : 1px solid black;
         
            border-radius : 20px;
            }
            QComboBox::!on:hover
            {   
            background-color:#cbf6db;
            }

            QComboBox::!editable:on
            {
            border : 4px #E69A8DFF;
            }
            
            QPushButton:hover{
                background-color:#cbf6db			;

            }
            QLineEdit:hover{

            background-color:#cbf6db			;

            }
            

        """
        self.setStyleSheet(style)


   


if __name__=="__main__":
    app= QtWidgets.QApplication(sys.argv)      
    win=Mywindow2()
    win.show()
    sys.exit(app.exec_())                                               

