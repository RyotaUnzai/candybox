
# class PyCircularProgress(QWidget):
#     value = 73
#     progress_width = 10
#     is_rounded = True
#     max_value = 100
#     progress_color = "#ff79c6"
#     enable_text = True
#     font_family = "Segoe UI"
#     font_size = 12
#     suffix = "%"
#     text_color = "#ff79c6"
#     enable_bg = True
#     bg_color = "#44475a"

#     def __init__(self, parent=None):
#         super(PyCircularProgress, self).__init__(parent)

#     # ADD DROPSHADOW

#     def add_shadow(self, enable):
#         if enable:
#             self.shadow = QGraphicsDropShadowEffect(self)
#             self.shadow.setBlurRadius(15)
#             self.shadow.setXOffset(0)
#             self.shadow.setYOffset(0)
#             self.shadow.setColor(QColor(0, 0, 0, 80))
#             self.setGraphicsEffect(self.shadow)

#     # SET VALUE
#     def set_value(self, value):
#         self.value = value
#         self.repaint()  # Render progress bar after change value

#     # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)

#     def paintEvent(self, event):
#         width = self.width() - self.progress_width
#         height = self.height() - self.progress_width
#         margin = self.progress_width / 2
#         value = self.value * 360 / self.max_value

#         # PAINTER
#         paint = QPainter(self)
#         paint.begin(self)
#         paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
#         paint.setFont(QFont(self.font_family, self.font_size))

#         # CREATE RECTANGLE
#         rect = QRect(0, 0, self.width(), self.height())

#         # PEN
#         pen = QPen(QColor(self.bg_color), self.progress_width, Qt.SolidLine)
#         # Set Round Cap
#         if self.is_rounded:
#             pen.setCapStyle(Qt.RoundCap)

#         # ENABLE BG
#         if self.enable_bg:
#             pen = QPen(QColor(self.bg_color), self.progress_width, Qt.SolidLine)
#             paint.setPen(pen)
#             paint.drawArc(margin, margin, width, height, 0, 360 * 16)

#         # CREATE ARC / CIRCULAR PROGRESS

#         pen = QPen(QColor(self.progress_color), self.progress_width, Qt.SolidLine)
#         paint.setPen(pen)
#         paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

#         # CREATE TEXT
#         if self.enable_text:

#             pen = QPen(QColor(self.text_color), self.progress_width, Qt.SolidLine)
#             paint.setPen(pen)
#             paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

#         # END
#         paint.end()

# self.createQAnimationComboBox()
# self.changeWidget()
# self.ui.Cb_qss.deleteLater()

# d = PyCircularProgress(
#     parent=self.ui,
#     value=80,
#     progress_color="#568af2",
#     text_color="#dce1ec",
#     font_size=14,
#     bg_color="#272c36"
# )
# # d.setFixedSize(200, 200)

# d2 = PyCircularProgress(
#     parent=self.ui,
# )
# d2.setFixedSize(100, 100)
# d2.setMinimumSize(100, 100)
# d2.setMaximumSize(100, 100)

# self.ui.gridLayout.addWidget(
#     d2, 9, 0, 1, 1
# )
# d = QPushButton()

# self.ui.gridLayout.addWidget(
#     d, 8, 0, 2, 2
# )

# def createQAnimationComboBox(self):
#     self.ComboBox = QtCustom.QAnimationComboBox(self.ui)
#     self.ComboBox_ListView = QListView(self.ui)
#     self.ComboBox_ListView.setObjectName("Cb_qss")
#     self.ComboBox_ListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#     self.ComboBox.setView(self.ComboBox_ListView)
#     self.ComboBox_LineEdit = QLineEdit(self.ui)
#     self.ComboBox_LineEdit.setObjectName("Cb_qss")
#     self.ComboBox_LineEdit.setReadOnly(True)
#     self.ComboBox.setLineEdit(self.ComboBox_LineEdit)
#     self.ComboBox.setObjectName("Cb_qss")
#     self.ComboBox.PopupOffcet = (0, 10)
#     self.ComboBox.fade = True
#     self.ComboBox.slide = False
#     self.ComboBox.stretch = True
#     for i in range(5):
#         self.ComboBox.addItem("Item %s" % i)

# def changeWidget(self):
#     for num in range(self.ui.gridLayout.count()):
#         item = self.ui.gridLayout.itemAt(num)
#         try:
#             widget = item.widget()
#             objectName = widget.objectName()
#             if objectName == "Cb_qss":
#                 pos = self.ui.gridLayout.getItemPosition(num)
#         except BaseException:
#             pass

#     self.ui.Cb_qss.deleteLater()
#     self.ui.Cb_qss = self.ComboBox
#     self.ui.gridLayout.addWidget(
#         self.ui.Cb_qss, pos[0], pos[1], pos[2], pos[3]
#     )
