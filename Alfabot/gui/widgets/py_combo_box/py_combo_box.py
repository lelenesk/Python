from qt_core import *

style = '''
QComboBox {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
	selection-background-color: {_bg_color_selection};
	selection-color: yellow;
}}
QComboBox:hover {{
	background-color: {_bg_color_hover};
}}
QComboBox:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

class PyComboBox(QComboBox):
    def __init__(
        self,
        radius,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        bg_color_dropdown,
        parent = None,
    ):
        super().__init__()

        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed,
            _bg_color_selection = bg_color_dropdown,
        )
        self.setStyleSheet(custom_style)

        