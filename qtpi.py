from PyQt5.QtWidgets import QApplication as QApp, QLabel

app = QApp([])
label = QLabel('Hello World!')
label.show()
app.exec()