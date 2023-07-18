import pytest
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QImage, QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib 
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import *

@pytest.fixture
def app(qtbot):
    existing_app = QApplication.instance()
    if not existing_app:
        test_app = QApplication([])
    else:
        test_app = existing_app
    yield test_app
    if not existing_app:
        test_app.quit()

def test_canvas_drawing_valid_inputs(app, qtbot):
    widget = DarkThemeWidget(600)
    widget.eqn_entry.setText("x^2")
    widget.x_min_entry.setText("1")
    widget.x_max_entry.setText("5")

    widget.draw_button.click()
    buffer = widget.canvas.buffer_rgba()
    image = QImage(buffer, buffer.shape[1], buffer.shape[0], QImage.Format_ARGB32)

    # Check if any non-transparent pixels are present
    has_drawn = False
    for y in range(image.height()):
        for x in range(image.width()):
            pixel_color = image.pixelColor(x, y)
            if pixel_color.alpha() != 0:
                has_drawn = True
                break
                
    # Perform assertion on whether something was drawn
    assert has_drawn

def test_canvas_drawing_invalid_inputs(app, qtbot):
    widget = DarkThemeWidget(600)
    widget.eqn_entry.setText("")
    widget.x_min_entry.setText("5")
    widget.x_max_entry.setText("")

    widget.draw_button.click()
    buffer = widget.canvas.buffer_rgba()
    image = QImage(buffer, buffer.shape[1], buffer.shape[0], QImage.Format_ARGB32)

    # Check if any non-transparent pixels are present
    has_drawn = False
    for y in range(image.height()):
        for x in range(image.width()):
            pixel_color = image.pixelColor(x, y)
            if pixel_color.alpha() != 0:
                has_drawn = True
                break

    # Perform assertion on whether something was drawn
    assert has_drawn