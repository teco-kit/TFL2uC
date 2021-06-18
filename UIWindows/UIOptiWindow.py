import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIOptiWindow(QWidget):
    """Select a optimization algorithm. 

    This GUI window has two buttons to choose the optimazion algorithms
    pruning and quantization. The pruning factors can be passed via
    input fields, and the quantization data type via buttons.
    """
    def __init__(self, FONT_STYLE, parent=None):
        super(UIOptiWindow, self).__init__(parent)

        self.FONT_STYLE = FONT_STYLE        
        
        self.label = QLabel("Optimization")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel(self)
        self.Abstand.setFixedWidth(140)
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_label = QLabel(self)
        self.Abstand_label.setFixedWidth(20)
        self.Abstand_label.setFixedHeight(30)
        
        self.Button_Platzhalter = QLabel()
        self.Button_Platzhalter.setFixedWidth(90)
        self.Button_Platzhalter.setFixedHeight(30)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_2.png'))
        self.Schritt.setFixedHeight(30)
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)    
        
        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(25, 25))
        self.Next.setFixedHeight(30)    
        
        self.Pruning = QPushButton(self)
        self.Pruning.setIcon(QIcon(os.path.join('Images', 'Pruning_Button.png')))
        self.Pruning.setIconSize(QSize(260, 260))
        self.Pruning.setCheckable(True)
        self.Pruning.setGeometry(80, 125, 280, 280)
        self.Pruning.setToolTip('Optimize the network through pruning. This\n'
                                'involves reducing the size of the network\n'
                                'by removing neurons from the fully connected\n'
                                'layers or feature maps from the convolution\n'
                                'layers. The pruning factors determine the\n'
                                'percentage of neurons or feature maps to\n'
                                'be removed from each layer.') 
        self.Pruning.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        
        
        self.Quantization = QPushButton(self)
        self.Quantization.setIcon(QIcon(os.path.join('Images', 'Quantization_Button.png')))
        self.Quantization.setIconSize(QSize(260, 260))
        self.Quantization.setCheckable(True)
        self.Quantization.setGeometry(440, 125, 280, 280)
        self.Quantization.setToolTip('Optimize the network through quantization.\n'
                                     'This reduces the number of bits required\n'
                                     'to represent the value of the weights.\n'
                                     'For example, a fourfold reduction of the\n'
                                     'required memory space can be achieved by\n'
                                     'converting the weights from 32-bit float\n'
                                     'values to 8-bit integer values.')
        self.Quantization.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        
        
        self.Pruning_Dense_label = QLabel("Pruningfactor\nDense layer", self)
        self.Pruning_Dense_label.setStyleSheet("font: 9pt " + FONT_STYLE)
        self.Pruning_Dense_label.setFixedWidth(90)
        self.Pruning_Dense_label.setFixedHeight(30)
        self.Pruning_Dense_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Dense_label.setVisible(False)
        
        self.Pruning_Conv_label = QLabel("Pruningfactor\nConv layer", self)
        self.Pruning_Conv_label.setStyleSheet("font: 9pt " + FONT_STYLE)
        self.Pruning_Conv_label.setFixedWidth(90)
        self.Pruning_Conv_label.setFixedHeight(30)
        self.Pruning_Conv_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Conv_label.setVisible(False)
        
        self.Pruning_Dense = QLineEdit(self)
        self.Pruning_Dense.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Pruning_Dense.setFixedWidth(90)
        self.Pruning_Dense.setFixedHeight(30)
        self.Pruning_Dense.setAlignment(Qt.AlignCenter)
        self.Pruning_Dense.setVisible(False)

        self.Pruning_Conv = QLineEdit(self)
        self.Pruning_Conv.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.Pruning_Conv.setFixedWidth(90)
        self.Pruning_Conv.setFixedHeight(30)
        self.Pruning_Conv.setAlignment(Qt.AlignCenter)
        self.Pruning_Conv.setVisible(False)

        self.quant_int = QPushButton("int8+float32", self)
        self.quant_int.setFixedWidth(90)
        self.quant_int.setFixedHeight(30)
        self.quant_int.setCheckable(True)
        self.quant_int.setVisible(False)
        self.quant_int.setToolTip('This quantization approach converts all weights\n'
                                     'to int8 values. But the input and output\n'
                                     'still remain 32-bit float.')
        self.quant_int.setStyleSheet("""QPushButton {
                           font: 9pt """ + FONT_STYLE + """}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        # self.quant_int.setDisabled(True)
        # self.quant_int.setStyleSheet("font: 12pt " + FONT_STYLE + ";" + "background-color : gray")
        
        self.quant_int_only = QPushButton("int8 only", self)
        self.quant_int_only.setFixedWidth(90)
        self.quant_int_only.setFixedHeight(30)
        self.quant_int_only.setCheckable(True)
        self.quant_int_only.setVisible(False)
        self.quant_int_only.setToolTip('This quantization approach converts all weights\n'
                                     'to int8 values. Also the input and output\n'
                                     'will be converted to 8-bit integer.')
        self.quant_int_only.setStyleSheet("""QPushButton {
                           font: 10pt """ + FONT_STYLE + """}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")

        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand)
        self.horizontal_box[1].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Pruning_Dense_label, 0, 0, Qt.AlignBottom)
        sublayout.addWidget(self.Abstand_label, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Conv_label, 0, 2, Qt.AlignBottom)
        sublayout.addWidget(self.Abstand, 0, 3, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 0, 4, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_label, 0, 5, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 0, 6, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Dense, 1, 0, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_label, 1, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Conv, 1, 2, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand, 1, 3, Qt.AlignCenter)
        sublayout.addWidget(self.quant_int, 1, 4, Qt.AlignCenter)
        # sublayout.addWidget(self.Abstand_label, 1, 4, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_label, 1, 5, Qt.AlignCenter)
        # sublayout.addWidget(self.Abstand_label, 1, 6, Qt.AlignCenter)
        sublayout.addWidget(self.quant_int_only, 1, 6, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 2, 0, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_label, 2, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 2, 2, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand, 2, 3, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 2, 4, Qt.AlignCenter)
        sublayout.addWidget(self.Abstand_label, 2, 5, Qt.AlignCenter)
        sublayout.addWidget(self.Button_Platzhalter, 2, 6, Qt.AlignCenter)
        sublayout.setAlignment(Qt.AlignCenter)
        self.horizontal_box[2].addLayout(sublayout)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Next, 0, 2, Qt.AlignRight)
        self.horizontal_box[3].addLayout(sublayout)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)