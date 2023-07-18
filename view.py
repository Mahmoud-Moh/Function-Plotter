from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DarkThemeWidget(QWidget):
    def __init__(self, viewModel, window_width):
        super().__init__()
        self.window_width = window_width
        self.viewModel = viewModel
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100, 100, self.window_width, 800)
        self.setWindowTitle("Plotter")

        #Dark Mode 
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)


        #Layouts 
        sidebar_main = QHBoxLayout(self)
        sidebar = QVBoxLayout(self)
        main = QVBoxLayout(self)

        #Widgets 
        sidebar_widget = QWidget(self)
        instructions_widget = QWidget()
        main_widget = QWidget(self)
        icon_home = QPushButton()
        icon_instructions = QPushButton()
        icon_uml = QPushButton()

        main_widget_stacked = QStackedWidget()
        main_widget_stacked.addWidget(main_widget)
        main_widget_stacked.setCurrentWidget(main_widget)

        #Adding Layouts  
        sidebar_main.addLayout(sidebar)
        sidebar_main.addLayout(main) 

        #Adding Widgets to Layouts 
        sidebar.addWidget(sidebar_widget)
        main.addWidget(main_widget_stacked)

        #Adding Layouts of Widgets to Widgets 
        sidebar_widget_layout = QVBoxLayout(sidebar_widget)
        main_widget_layout =  QVBoxLayout(main_widget)
        sidebar_widget_layout.setAlignment(Qt.AlignTop)

        #Nested Widgets to Layouts of Widgets
        icon_home.setIcon(QIcon("assets/homeAsset 46.png"))
        icon_home.setIconSize(QSize(20, 50))
        icon_home.setFlat(True)
        icon_home.setStyleSheet(u"QPushButton {\n"
        "	border: 2px solid rgb(51,51,51);\n"
        "	border-radius: 5px;	\n"
        "	color:rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	border: 2px solid rgb(211, 211, 211);\n"
        "	background-color: rgb(211, 211, 211);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 2px solid rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {	\n"
        "	border-radius: 5px;	\n"
        "	border: 2px solid rgb(112,112,112);\n"
        "	background-color: rgb(112,112,112);\n"
        "}")
        icon_home.clicked.connect(lambda:self.switch_page(main_widget_stacked, main_widget))

        icon_instructions.setIcon(QIcon("assets/icons8-info-64.png"))
        icon_instructions.setIconSize(QSize(20, 50))
        icon_instructions.setFlat(True)
        icon_instructions.setStyleSheet(u"QPushButton {\n"
        "	border: 2px solid rgb(51,51,51);\n"
        "	border-radius: 5px;	\n"
        "	color:rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	border: 2px solid rgb(211, 211, 211);\n"
        "	background-color: rgb(211, 211, 211);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 2px solid rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {	\n"
        "	border-radius: 5px;	\n"
        "	border: 2px solid rgb(112,112,112);\n"
        "	background-color: rgb(112,112,112);\n"
        "}")
        icon_instructions.clicked.connect(lambda:self.switch_page(main_widget_stacked, instructions_widget))

        icon_uml.setIcon(QIcon("assets/icons8-diagram-64.png"))
        icon_uml.setIconSize(QSize(20, 50))
        icon_uml.setFlat(True)
        icon_uml.setStyleSheet(u"QPushButton {\n"
        "	border: 2px solid rgb(51,51,51);\n"
        "	border-radius: 5px;	\n"
        "	color:rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	border: 2px solid rgb(211, 211, 211);\n"
        "	background-color: rgb(211, 211, 211);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 2px solid rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {	\n"
        "	border-radius: 5px;	\n"
        "	border: 2px solid rgb(112,112,112);\n"
        "	background-color: rgb(112,112,112);\n"
        "}")

        sidebar_widget_layout.addWidget(icon_home)
        sidebar_widget_layout.addWidget(icon_instructions)
        sidebar_widget_layout.addWidget(icon_uml)

        #main_widget.setStyleSheet("background-color: (50, 50, 50);")
        #Main 
        fig, ax, canvas = self.form_plotter()
        self.canvas.draw()
        font = QFont()
        font.setPointSizeF(18)

        layout2 = QHBoxLayout(self)

        layout3 = QHBoxLayout(self)
        layout4 = QVBoxLayout(self)
        layout5 = QHBoxLayout(self)
        layout6 = QHBoxLayout(self) 

        eqn_label = QLabel(self)
        eqn_label.setText("Equation")
        eqn_label.setFont(font)

        self.eqn_entry = QLineEdit(self)
        self.eqn_entry.setFixedWidth(450)
        self.eqn_entry.setFixedHeight(40)
        eqn_label.setFixedWidth(120)
        layout2.addWidget(eqn_label)    
        layout2.addWidget(self.eqn_entry)
        layout2.setAlignment(Qt.AlignLeft) 

        layout2.setContentsMargins(0, 30, 0, 0)


        x_min_label = QLabel(self)
        x_min_label.setText("Xmin")

        x_max_label = QLabel(self)
        x_max_label.setText("Xmax")

        self.x_min_entry = QLineEdit(self)
        self.x_max_entry = QLineEdit(self)

        x_max_label.setFixedWidth(120)
        x_min_label.setFixedWidth(120)
        x_min_label.setFont(font)
        x_max_label.setFont(font)
        eqn_label.setStyleSheet("color: white; font-weight: bold;")
        x_min_label.setStyleSheet("color: white; font-weight: bold;")
        x_max_label.setStyleSheet("color: white; font-weight: bold")
        self.x_min_entry.setStyleSheet("color: white; font-size: 18px; background-color:rgb(150,150,150); border: 0.5px solid rgb(90,90,90); border-radius: 3px")
        self.x_max_entry.setStyleSheet("color: white; font-size: 18px; background-color:rgb(150,150,150); border: 0.5px solid rgb(90,90,90); border-radius: 3px")
        self.eqn_entry.setStyleSheet("color: white; font-size: 18px; background-color:rgb(150,150,150); border: 0.5px solid rgb(90,90,90); border-radius: 3px")   


        self.x_min_entry.setFixedHeight(30)
        self.x_max_entry.setFixedHeight(30)
        self.x_min_entry.setFixedWidth(150)
        self.x_max_entry.setFixedWidth(150)


        layout5.addWidget(x_min_label)
        layout5.addWidget(self.x_min_entry)

        layout6.addWidget(x_max_label)
        layout6.addWidget(self.x_max_entry)

        layout4.addLayout(layout5)
        layout4.addLayout(layout6)

        layout3.addLayout(layout4)

        self.draw_button = QPushButton(self, text="Plot")
        self.draw_button.setIcon(QIcon("assets/icons8-plot-50.png"))
        self.draw_button.setIconSize(QSize(20, 50))
        self.draw_button.setFlat(True)
        self.draw_button.setStyleSheet(u"QPushButton {\n"
        "	border: 2px solid rgb(51,51,51);\n"
        "	border-radius: 5px;	\n"
        "	color:rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	border: 2px solid rgb(211, 211, 211);\n"
        "	background-color: rgb(211, 211, 211);\n"
        "}\n"
        "QPushButton:pressed {	\n"
        "	border: 2px solid rgb(255,255,255);\n"
        "	background-color: rgb(51,51,51);\n"
        "}\n"
        "\n"
        "QPushButton:disabled {	\n"
        "	border-radius: 5px;	\n"
        "	border: 2px solid rgb(112,112,112);\n"
        "	background-color: rgb(112,112,112);\n"
        "}")

        self.draw_button.clicked.connect(lambda:self.draw_button_clicked(canvas, ax))
        layout_button = QVBoxLayout()
        layout_button.addWidget(self.draw_button)
        layout3.addLayout(layout_button)
        layout_button.setContentsMargins(75, 0, 46 , 0)

        main_widget_layout.addLayout(layout2)
        main_widget_layout.addLayout(layout3)
        main_widget_layout.setContentsMargins(50, 0, 0, 0)
        main_widget_layout.addWidget(canvas)     
        main_widget.setStyleSheet("background-color: rgb(100, 100, 100)")

        #Instructions Widget
        instructions_widget_layout = QVBoxLayout(instructions_widget)
        instructions_label = QLabel()
        instructions_label.setText("Instuctions")
        instructions_list = QListWidget()
        instructs = ["\n1.Function should only contain these operators + - / * ^. \n", 
                     "2.The only supported variable name is x.\n", 
                     "3.Example of valid functions\n   -x^3 + (1/5)*x^2 + 3*x + 1\n   -(x-4)^2/(x-6)\n   -5\n",
                     "4.Example of invalid functions\n   -x^3 +\n   -f(x)=(x-4)^2/(x-6)    \n   -3x(remember to put * with scalars -> correct is 3*x)\n",
                     "5.Divison by zero is handled don't wory, but if you put (1/0) into equation \nthat's not valid."]
        for item_text in instructs:
            list_item = QListWidgetItem(item_text)
            instructions_list.addItem(list_item)
        instructions_list.setStyleSheet("font-size:18px; background-color:rgb(100, 100, 100); color:white; font-weight:bold;")
        instructions_widget_layout.addWidget(instructions_label)
        instructions_widget_layout.addWidget(instructions_list)
        main_widget_stacked.addWidget(instructions_widget)
        

        #Setting up Widgets 
        #sidebar_widget.setStyleSheet("background-color: red;")
        sidebar_widget.setFixedWidth(100)  
        #main_widget.setStyleSheet("background-color: green;")       

        #Setting Main Layout    
        self.setLayout(sidebar_main)
    
    def form_plotter(self): 
        """
        Create a plotter with a customized background color and axis styles.

        Returns:
            tuple: A tuple containing:
                Figure: The Matplotlib figure object for the plot.
                Axes: The Matplotlib axes object for the plot.
                FigureCanvas: The Matplotlib FigureCanvas object for the plot.
        """
        fig = plt.figure(facecolor='none') 
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.set_facecolor((100/255, 100/255, 100/255))
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        canvas.setStyleSheet("background-color: transparent;")
        self.fig = fig
        self.canvas = canvas 
        self.ax = ax 
        return fig, ax, canvas 
        
    def switch_page(self, stacked_main, widget):
        """
        Switch the current page in the stacked widget to the specified widget.

        Parameters:
            stacked_main: The QStackedWidget containing multiple pages.
            widget: The widget to be displayed.

        Returns:
            None
        """ 
        stacked_main.setCurrentWidget(widget)
    
    def show_popup(self, message, parent):
        """
        Display a popup message box with an error icon.

        Parameters:
            message (str): The message to be displayed in the popup.
            parent: The parent widget for the popup.

        Returns:
            None
        """
        popup = QMessageBox(parent)
        popup.setWindowTitle("Error")
        popup.setText("\u274C " + message)
        popup.exec_()
    
    def draw_button_clicked(self, canvas,  ax):
        """
        Draw the graph on the canvas based on the provided equation and Xmin, Xmax values.

        Parameters:
            canvas: The Matplotlib FigureCanvas object for drawing the plot.
            ax: The Matplotlib axes object for the plot.

        Returns:
            None
        """ 
        eqn_text = self.eqn_entry.text()
        Xmin_text = self.x_min_entry.text()
        Xmax_text = self.x_max_entry.text()
        state, message = self.viewModel.validate_input(eqn_text, Xmin_text, Xmax_text)
        if state: 
            self.show_popup(message, self)
        else: 
            self.ax.cla()   
            x, y = self.viewModel.get_plot_xys(eqn_text, float(Xmin_text), float(Xmax_text))
            self.ax.plot(x, y, color='y')
            self.canvas.draw()


