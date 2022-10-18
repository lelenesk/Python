from qt_core import *

style = '''
QLineEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
    font:  {_font};
}}
QLineEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''


class PyLineEdit(QLineEdit):
    def __init__(
        self, 
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#FFF",
        selection_color = "#FFF",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#00ABE8",
        font = "23pt Comic Sans MS"
    ):
        super().__init__()

        if text:
            self.setText(text)
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color,
            font
        )

    def set_stylesheet(
        self,
        radius,
        border_size,
        color,
        selection_color,
        bg_color,
        bg_color_active,
        context_color,
        font
    ):
        style_format = style.format(
            _radius = radius,
            _border_size = border_size,           
            _color = color,
            _selection_color = selection_color,
            _bg_color = bg_color,
            _bg_color_active = bg_color_active,
            _context_color = context_color,
            _font =font
        )
        self.setStyleSheet(style_format)