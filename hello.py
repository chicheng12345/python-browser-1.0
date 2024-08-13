import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle('Simple Browser')
        self.resize(1024, 768)

        # 创建中心小部件和布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # 创建一个 WebEngineView 对象用于显示网页
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # 创建一个地址栏
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        layout.addWidget(self.url_bar)

        # 设置中心小部件
        self.setCentralWidget(central_widget)

        # 加载初始网页
        self.browser.setUrl(QUrl('https://example.com'))  # 替换为你想访问的网址
        self.url_bar.setText('https://example.com')

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())
