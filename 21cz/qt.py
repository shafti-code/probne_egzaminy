# Rejestracja konta - aplikacja okienkowa w PyQt6
# Autor: <TWÓJ PESEL>

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

AUTOR_PESEL = "RODO I WGL"

class RejestracjaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rejestruj konto")
        self.setup_ui()

    def setup_ui(self):
        # główny układ pionowy
        main_layout = QVBoxLayout()

        # nagłówek
        title = QLabel("Rejestruj konto")
        title_font = QFont()
        title_font.setPointSize(18)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: #008080; color: white; padding: 10px;")
        main_layout.addWidget(title)

        # pole e-mail
        lbl_email = QLabel("Podaj e-mail:")
        main_layout.addWidget(lbl_email)

        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("email")
        self.edit_email.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main_layout.addWidget(self.edit_email)

        # pole hasło
        lbl_pass = QLabel("Podaj hasło:")
        main_layout.addWidget(lbl_pass)

        self.edit_pass = QLineEdit()
        self.edit_pass.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(self.edit_pass)

        # pole powtórz hasło
        lbl_pass2 = QLabel("Powtórz hasło:")
        main_layout.addWidget(lbl_pass2)

        self.edit_pass2 = QLineEdit()
        self.edit_pass2.setEchoMode(QLineEdit.EchoMode.Password)
        main_layout.addWidget(self.edit_pass2)

        # przycisk zatwierdź
        btn_layout = QHBoxLayout()
        btn_layout.addStretch(1)
        self.btn_submit = QPushButton("ZATWIERDŹ")
        self.btn_submit.setFixedWidth(160)
        self.btn_submit.clicked.connect(self.on_submit)
        btn_layout.addWidget(self.btn_submit)
        btn_layout.addStretch(1)
        main_layout.addLayout(btn_layout)

        # obszar komunikatów
        msg_layout = QHBoxLayout()
        msg_layout.addStretch(1)
        self.lbl_msg = QLabel(f"Autor {AUTOR_PESEL}")
        self.lbl_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg_layout.addWidget(self.lbl_msg)
        msg_layout.addStretch(1)
        main_layout.addLayout(msg_layout)

        self.setLayout(main_layout)
        self.setMinimumWidth(360)

    def on_submit(self):
        # walidacja danych
        email = self.edit_email.text().strip()
        p1 = self.edit_pass.text()
        p2 = self.edit_pass2.text()

        if "@" not in email:
            self.lbl_msg.setText("Nieprawidłowy adres e-mail")
            return
        if p1 != p2:
            self.lbl_msg.setText("Hasła się różnią")
            return

        self.lbl_msg.setText(f"Witaj {email}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RejestracjaApp()
    window.show()
    sys.exit(app.exec())

