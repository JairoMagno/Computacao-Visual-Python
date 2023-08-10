"""
Autor: Jairo Magno Caracciolo Marques
Data de criação: 08/08/2023
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QFont
from PySide6 import QtCore, QtGui

from rasp_state import rasp_update

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Teste Módulos Raspberry')
        self.setWindowIcon(QIcon('images/Logo_GPEB_Menor.png'))

        #label do Corpo
        img_body = QImage('images/body.png')
        pixmap = QPixmap(img_body.scaledToWidth(250))
        self.body_label = QLabel(self)
        self.body_label.setPixmap(QPixmap(pixmap))
        self.body_label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QHBoxLayout(self)
        layout.addWidget(self.body_label)

        # Layout para os círculos informativos e as frases
        circle_info_layout = QVBoxLayout()
        serisFont_1 = QFont('Times', 15)
        serisFont_2 = QFont('Times', 40)

        # Criação das frases e círculos informativos
        phrases_and_circles = [
            ('Não Conectado', QtGui.QColor(255, 0, 0)), # Vermelho
            ('Conectado e Não Enviando Dados', QtGui.QColor(0, 0, 255)), # Azul
            ('Conectado e Enviando Dados', QtGui.QColor(0, 255, 0)) # Verde
        ]

        for phrase, circle_color in phrases_and_circles:
            circle_label = QLabel('●')
            circle_label.setFont(serisFont_2)
            circle_label.setStyleSheet(f'color: {circle_color.name()}')

            phrase_label = QLabel(phrase)
            phrase_label.setFont(serisFont_1)

            phrase_layout = QHBoxLayout()
            phrase_layout.addWidget(circle_label)
            phrase_layout.addSpacing(-400)
            phrase_layout.addWidget(phrase_label)

            circle_info_layout.addLayout(phrase_layout)

        layout.addLayout(circle_info_layout)
        self.setLayout(layout)
        
        self.rasp_connection = [0, 1, 2]
        self.current_connection_state = [0, 0, 0, 0, 0, 0] # Índice inicial
        self.circle_colors = [
            QtGui.QColor(255, 0, 0),   # Vermelho
            QtGui.QColor(0, 0, 255),   # Azul
            QtGui.QColor(0, 255, 0)   # Verde
        ]
        
        self.update_circle_states()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_circle_states)
        self.timer.start(2500)  # Atualize a cada 2500 ms (2.5 segundos)

    def update_circle_states(self):
        # Atualize os estados dos círculos
        self.current_connection_state = rasp_update(self.current_connection_state, self.rasp_connection)
        # Mude a cor com base no novo estado
        color = [self.circle_colors[i] for i in self.current_connection_state]
        # Redesenhe a interface gráfica
        self.draw_circles(color)

    def draw_circles(self, color):
        pixmap = QPixmap(self.body_label.pixmap())
        painter = QPainter(pixmap)
        
        circle_coordinates = [
            (30, 340),   # Mão esquerda
            (225, 340),  # Mão direita
            (90, 600),   # Perna esquerda
            (160, 600),  # Perna direita
            (128, 280),  # Barriga ECG
            (128, 180)   # Peito Temperatura
        ]
        circle_radius = 15

        for (x, y), circle_color in zip(circle_coordinates, color):
            painter.setBrush(circle_color)
            painter.drawEllipse(x - circle_radius, y - circle_radius, 2 * circle_radius, 2 * circle_radius)
        painter.end()

        self.body_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.resize(1000, 600)
    window.show()

    sys.exit(app.exec())
