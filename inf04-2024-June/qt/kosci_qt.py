import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QHBoxLayout, QWidget, QPushButton, QLabel)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont

class DiceGameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.dice_values = [0, 0, 0, 0, 0]
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Gra w kości")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #F5F5DC;")  # Beige background
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 10, 20, 10)
        
        # Title label
        title_label = QLabel("Gra w kości. Autor 12345678901")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            color: white;
            background-color: #A52A2A;
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
        """)
        main_layout.addWidget(title_label)
        
        # Roll dice button
        self.roll_button = QPushButton("RZUĆ KOŚĆMI")
        self.roll_button.setStyleSheet("""
            QPushButton {
                background-color: #D2691E;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #CD853F;
            }
        """)
        self.roll_button.clicked.connect(self.roll_dice)
        main_layout.addWidget(self.roll_button)
        
        # Dice images layout
        dice_container = QWidget()
        dice_container.setStyleSheet("background-color: white; padding: 10px;")
        dice_layout = QHBoxLayout()
        dice_layout.setSpacing(9)
        dice_layout.setContentsMargins(9, 9, 9, 9)
        
        # Create 5 dice image labels
        self.dice_labels = []
        for i in range(5):
            dice_label = QLabel()
            dice_label.setFixedSize(60, 60)
            dice_label.setScaledContents(True)
            dice_label.setStyleSheet("border: 1px solid #ccc;")
            self.set_question_image(dice_label)
            dice_layout.addWidget(dice_label)
            self.dice_labels.append(dice_label)
        
        dice_container.setLayout(dice_layout)
        main_layout.addWidget(dice_container)
        
        # Round result label
        self.round_result_label = QLabel("Wynik tego losowania: 0")
        self.round_result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.round_result_label.setStyleSheet("font-size: 14px; padding: 5px;")
        main_layout.addWidget(self.round_result_label)
        
        # Game result label
        self.game_result_label = QLabel("Wynik gry: 0")
        self.game_result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.game_result_label.setStyleSheet("font-size: 14px; padding: 5px;")
        main_layout.addWidget(self.game_result_label)
        
        # Reset button
        self.reset_button = QPushButton("RESETUJ WYNIK")
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #D2691E;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #CD853F;
            }
        """)
        self.reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(self.reset_button)
        
        central_widget.setLayout(main_layout)
    
    def set_question_image(self, label):
        """Set question mark image for dice"""
        # Create a simple question mark placeholder
        label.setText("?")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("""
            border: 1px solid #ccc;
            font-size: 24px;
            font-weight: bold;
            color: #666;
            background-color: #f0f0f0;
        """)
    
    def set_dice_image(self, label, value):
        """Set dice image based on value"""
        # Create dice representation with dots
        dice_patterns = {
            1: "●",
            2: "●●",
            3: "●●●",
            4: "●●\n●●",
            5: "●●\n●\n●●",
            6: "●●●\n●●●"
        }
        
        label.setText(dice_patterns.get(value, "?"))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("""
            border: 2px solid #333;
            font-size: 16px;
            font-weight: bold;
            color: #000;
            background-color: white;
            border-radius: 5px;
        """)
    
    def roll_dice_values(self):
        """
        ************************************************
        nazwa: roll_dice_values
        opis: Losuje 5 liczb z przedziału 1-6 reprezentujących rzut kośćmi
        parametry: brak
        zwracany typ i opis: list - lista 5 liczb całkowitych z przedziału 1-6
        autor: 12345678901
        ************************************************
        """
        return [random.randint(1, 6) for _ in range(5)]
    
    def calculate_points(self, dice_values):
        """
        ************************************************
        nazwa: calculate_points
        opis: Oblicza punkty za rzut według zasady gry - tylko liczby wylosowane więcej niż raz
        parametry: dice_values - lista liczb z rzutu kośćmi
        zwracany typ i opis: int - suma punktów za rzut
        autor: 12345678901
        ************************************************
        """
        # Count occurrences of each number
        counts = {}
        for value in dice_values:
            counts[value] = counts.get(value, 0) + 1
        
        # Calculate points - sum only numbers that appear 2 or more times
        points = 0
        for value, count in counts.items():
            if count >= 2:
                points += value * count
        
        return points
    
    def roll_dice(self):
        """Handle roll dice button click"""
        # Roll 5 dice
        self.dice_values = self.roll_dice_values()
        
        # Update dice images
        for i, value in enumerate(self.dice_values):
            self.set_dice_image(self.dice_labels[i], value)
        
        # Calculate round points
        round_points = self.calculate_points(self.dice_values)
        
        # Update round result
        self.round_result_label.setText(f"Wynik tego losowania: {round_points}")
        
        # Update game score
        self.game_score += round_points
        self.game_result_label.setText(f"Wynik gry: {self.game_score}")
    
    def reset_game(self):
        """Handle reset button click"""
        # Reset game score
        self.game_score = 0
        
        # Reset dice images to question marks
        for label in self.dice_labels:
            self.set_question_image(label)
        
        # Reset result labels
        self.round_result_label.setText("Wynik tego losowania: 0")
        self.game_result_label.setText("Wynik gry: 0")

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    window = DiceGameApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
