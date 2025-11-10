from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QLinearGradient, QBrush
from PyQt5.QtCore import Qt, QTimer
import sys

class VaporwaveGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vaporwave Grid 🌅")
        self.resize(900, 600)
        self.offset = 0  # movimento das linhas horizontais

        # Timer para animar o grid
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(60)  # atualiza a cada 60ms (~16 FPS)

    def animate(self):
        self.offset += 3
        if self.offset >= 60:  # reseta o movimento pra dar loop
            self.offset = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        horizon_y = height // 2 + 50  # posição do horizonte
        spacing = 60  # distância entre linhas

        # 🎨 Gradiente de fundo (roxo -> azul escuro)
        gradient = QLinearGradient(0, 0, 0, height)
        gradient.setColorAt(0, QColor("#000000"))
        painter.fillRect(self.rect(), QBrush(gradient))

        # 🕸️ Grid vaporwave
        # Linhas horizontais (perspectiva)
        for i in range(15):
            y = horizon_y + self.offset + i * spacing
            scale = (i + 1) / 15.0
            left_x = int(width // 2 - (width // 2) * (1 + scale))
            right_x = int(width // 2 + (width // 2) * (1 + scale))
            y = int(y)

            glow = QPen(QColor("#1eff00"))
            glow.setWidth(2)
            painter.setPen(glow)
            painter.drawLine(left_x, y, right_x, y)
        
        y = horizon_y
        painter.drawLine(left_x, y, right_x, y)

        # Linhas verticais convergindo para o horizonte
        painter.setPen(QPen(QColor("#1eff00"), 1.5))
        num_lines = 70
        for i in range(-num_lines // 2, num_lines // 2 + 1):
            x_bottom = int(width // 2 + i * 400)
            x_top = int(width // 2 + i * 30)
            painter.drawLine(x_bottom, height, x_top, horizon_y)

app = QApplication(sys.argv)
window = VaporwaveGrid()
window.show()
sys.exit(app.exec_())

