from qt_core import *

from . style import *

class PyComboBoxb(QComboBox):
    def __init__(
        self,
        radius = 8,
        color = "#46D11C",
        bg_color = "#46D11C",
        selection_color = "#46D11C",
        header_horizontal_color = "#333",
        header_vertical_color = "#444",
        bottom_line_color = "#555",
        grid_line_color = "#555",
        scroll_bar_bg_color = "#FFF",
        scroll_bar_btn_color = "#ff5554",
        context_color = "#21252D",
        selection_background_color ="#3C4052",
        bg_hover = "#8C1F1F",
        bg_pressed ="#3C4052",
        font="23pt Comic Sans MS",

    ):
        super().__init__()

        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color,
            selection_background_color,
            bg_hover,
            bg_pressed,
            font
        )
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        header_horizontal_color,
        header_vertical_color,
        selection_color,
        bottom_line_color,
        grid_line_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color,
        selection_background_color,
        bg_hover,
        bg_pressed,
        font
    ):
        style_format = style.format(
            _radius = radius,
            _color = color,
            _bg_color = bg_color,
            _header_horizontal_color = header_horizontal_color,
            _header_vertical_color = header_vertical_color,
            _selection_color = selection_color,
            _bottom_line_color = bottom_line_color,
            _grid_line_color = grid_line_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color,
            _bg_color_selection = selection_background_color,
            _bg_color_hover = bg_hover,
            _bg_color_pressed = bg_pressed,
            _font = font
        )
        self.setStyleSheet(style_format)

        