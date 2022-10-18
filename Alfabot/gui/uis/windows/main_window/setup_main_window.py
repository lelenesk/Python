
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *

from . modify import *
from . finder import *

from . ui_main import *

from . functions_main_window import *

class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Kezdőlap",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_widgets",
            "btn_text" : "Widgetek tesztoldal",
            "btn_tooltip" : "Widgetek tesztoldal",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_modify_user",
            "btn_text" : "Adatbázis kezelés",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_finder",
            "btn_text" : "Keresés",
            "btn_tooltip" : "Keresés",
            "show_top" : True,
            "is_active" : False
        }
    ]
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Keresés",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Beállítások",
            "is_active" : False
        }
    ]

    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    def setup_gui(self):
        self.setWindowTitle(self.settings["app_name"])

        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Title bar")

        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        MainFunctions.set_page(self, self.ui.load_pages.page_welcome)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)
        settings = Settings()
        self.settings = settings.items
        themes = Themes()
        self.themes = themes.items
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        self.welcome_label = PyLabel(
            text="Minden munka: amit meg kell tenni, és minden szórakozás: amit önként vállal az ember. - Mark Twain",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_two"],
            selection_color=self.themes["app_color"]["bg_two"],
            context_color=self.themes["app_color"]["dark_four"],
            font="25pt Comic Sans MS", )

        self.welcome_label.setMinimumHeight(60)
        self.welcome_label.setMaximumHeight(60)
        self.welcome_label.setMinimumWidth(1)
        self.welcome_label.setMaximumWidth(1900)

        self.ui.load_pages.welcome_title.addWidget(self.welcome_label,alignment=Qt.AlignCenter)

        self.welcome_button = PyPushButton(
            text="Frissítsd az adatbázist!!",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.welcome_button.setMinimumHeight(300)
        self.welcome_button.setMinimumWidth(300)

        self.welcome_button.setIcon(self.icon_2)
        self.welcome_button.clicked.connect(lambda: modifyFunctions.load_google_test_data(self, modifyFunctions.worksheet_list_client))
        #self.welcome_button.clicked.connect(lambda: table1Functions.load_all(self,table1Functions.worksheet_list_all))
        self.ui.load_pages.welcome_buttons.addWidget(self.welcome_button, Qt.AlignCenter, Qt.AlignCenter)

        self.circular_progress_1 = PyCircularProgress(
            value = 80,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200,200)

        self.circular_progress_2 = PyCircularProgress(
            value = 45,
            progress_width = 4,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["context_color"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160,160)

        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_width = 2,
            progress_color = self.themes["app_color"]["pink"],
            text_color = self.themes["app_color"]["white"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140,140)
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        self.vertical_slider_2 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        self.vertical_slider_4 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_heart.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Icon button - Heart",
            width = 40,
            height = 40,
            radius = 20,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )

        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN actived! (is_actived = True)",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["context_color"],
            is_active = True
        )

        self.push_button_1 = PyPushButton(
            text = "Gomb",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)
        self.push_button_2 = PyPushButton(
            text = "ikonos gomb",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)
        self.line_edit = PyLineEdit(
            text = "",
            place_holder_text = "ide írhatsz",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Nevem")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("EGO")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Pénz")

        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("GT Kft.")))
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("Ennyit keresek vele:")))
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText(str(x) + " 000 000")
            self.table_widget.setItem(row_number, 2, self.pass_text)
            self.table_widget.setRowHeight(row_number, 22)

        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_5_layout.addWidget(self.table_widget)

        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)
#-----------------------------------own pages----------------------------------------------------------------------

#-----------------------search client main page-------------------------------------------------------------------------

        self.load_main_button1 = PyPushButton(
            text="Új ügyfél felvitele",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_main_button1.setMinimumHeight(100)
        self.load_main_button1.setMinimumWidth(250)
        self.load_main_button1.clicked.connect(lambda: MainFunctions.pageshifter_newclient(self))
        self.ui.load_pages.search_main_newc.addWidget(self.load_main_button1, alignment=Qt.AlignCenter)
        self.load_main_button1.clicked.connect(lambda: modifyFunctions.search_destroyer(self))


        self.load_main_button3 = PyPushButton(
            text="Meglévő ügyfél, új esemény:",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_main_button3.setMinimumHeight(100)
        self.load_main_button3.setMinimumWidth(250)
        self.load_main_button3.setVisible(False)
        self.ui.load_pages.search_main_existc.addWidget(self.load_main_button3,alignment=Qt.AlignCenter)

        self.load_main_button3.clicked.connect(lambda: show_buttons_new())
        self.load_main_button3.clicked.connect(lambda: MainFunctions.pageshifter_existing_new_event(self))
        self.load_main_button3.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

        self.load_main_button4 = PyPushButton(
            text="Meglévő ügyfél, adatmódosítás:",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_main_button4.setMinimumHeight(100)
        self.load_main_button4.setMinimumWidth(250)
        self.load_main_button4.setVisible(False)
        self.load_main_button4.clicked.connect(lambda: show_buttons_new())
        self.load_main_button4.clicked.connect(lambda: MainFunctions.pageshifter_existing_datamod(self))
        #self.load_main_button4.clicked.connect(lambda: table1Functions.page_modify_data_setter(self))
        self.load_main_button4.clicked.connect(lambda: modifyFunctions.search_destroyer(self))
        self.ui.load_pages.search_main_existc.addWidget(self.load_main_button4,alignment=Qt.AlignCenter)

        def show_buttons_old():
            self.load_main_button3.setVisible(True)
            self.load_main_button4.setVisible(True)
            self.load_main_button2.setVisible(False)
            self.load_main_button1.setVisible(False)

        def show_buttons_new():
            self.load_main_button3.setVisible(False)
            self.load_main_button4.setVisible(False)
            self.load_main_button2.setVisible(True)
            self.load_main_button1.setVisible(True)

        self.load_main_button2 = PyPushButton(
            text="Meglévő ügyfél adminisztrációja",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_main_button2.setMinimumHeight(100)
        self.load_main_button2.setMinimumWidth(250)
        self.ui.load_pages.search_main_existc.addWidget(self.load_main_button2, alignment=Qt.AlignCenter)

        self.load_main_button2.clicked.connect(lambda: show_buttons_old())
        self.load_main_button2.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

#------------------------------------search new client page-------------------------------------------------------------
        self.load_newclient_lineedit = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.load_newclient_lineedit.setMinimumHeight(60)
        self.load_newclient_lineedit.setMaximumHeight(100)
        self.load_newclient_lineedit.setMinimumWidth(320)
        self.load_newclient_lineedit.setMaximumWidth(1500)
        self.load_newclient_lineedit.setPlaceholderText("Add meg az új ügyfél nevét")
        self.ui.load_pages.search_search_layout.addWidget(self.load_newclient_lineedit)

        self.load_newclient_button1 = PyPushButton(
            text="Ellenőrzés",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_newclient_button1.setMinimumHeight(100)
        self.load_newclient_button1.setMinimumWidth(250)
        self.ui.load_pages.search_search_layout.addWidget(self.load_newclient_button1)
        self.load_newclient_button1.clicked.connect(lambda: modifyFunctions.page_modify_insertnewclient(self))
        # self.load_newclient_button1.clicked.connect(lambda: table1Functions.search_destroyer(self))

#----------------existing client event page search----------------------------------------------------------------------

        self.load_existing_event_cilent_lineedit = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.load_existing_event_cilent_lineedit.setMinimumHeight(60)
        self.load_existing_event_cilent_lineedit.setMaximumHeight(100)
        self.load_existing_event_cilent_lineedit.setMinimumWidth(320)
        self.load_existing_event_cilent_lineedit.setMaximumWidth(1500)
        self.load_existing_event_cilent_lineedit.setPlaceholderText("Írd be a keresett ügyfelet")
        self.ui.load_pages.search_exist_event_search_layout.addWidget(self.load_existing_event_cilent_lineedit)

        self.load_existing_event_button1 = PyPushButton(
            text="Ügyfél keresése",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_existing_event_button1.setMinimumHeight(100)
        self.load_existing_event_button1.setMinimumWidth(250)
        self.ui.load_pages.search_exist_event_search_layout.addWidget(self.load_existing_event_button1)
        self.load_existing_event_button1.clicked.connect(lambda: modifyFunctions.page_modify_event_setter(self))
        #self.load_existing_event_button1.clicked.connect(lambda: table1Functions.search_destroyer(self))


#-----------------existing client data page search---------------------------------------------------------------------

        self.load_existing_data_cilent_lineedit = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.load_existing_data_cilent_lineedit.setMinimumHeight(60)
        self.load_existing_data_cilent_lineedit.setMaximumHeight(100)
        self.load_existing_data_cilent_lineedit.setMinimumWidth(320)
        self.load_existing_data_cilent_lineedit.setMaximumWidth(1500)
        self.load_existing_data_cilent_lineedit.setPlaceholderText("Írd be a keresett ügyfelet")
        self.ui.load_pages.search_exist_data_search_layout.addWidget(self.load_existing_data_cilent_lineedit)

        self.load_existing_data_button1 = PyPushButton(
            text="Ügyfél keresése",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.load_existing_data_button1.setMinimumHeight(100)
        self.load_existing_data_button1.setMinimumWidth(250)
        self.ui.load_pages.search_exist_data_search_layout.addWidget(self.load_existing_data_button1)
        self.load_existing_data_button1.clicked.connect(lambda: modifyFunctions.page_modify_data_setter(self))
        #self.load_existing_data_button1.clicked.connect(lambda: table1Functions.search_destroyer(self))

#------------------------ finder page --------------------------------------------------------------------------------

        self.finder_table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["white"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["dark_two"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"], )
           # font="13pt Comic Sans MS",
           # grid_color=self.themes["app_color"]['grid_color'],)

        self.finder_table.setColumnCount(13)
        self.finder_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.finder_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.finder_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.load_pages.finder_table_layout.addWidget(self.finder_table)


        self.finder_client_button = PyPushButton(
            text="Ügyfél neve: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_client_button.setMinimumHeight(80)
        self.finder_client_button.setMinimumWidth(250)
        self.finder_client_button.setMaximumWidth(300)

        self.ui.load_pages.finder_client_layout.addWidget(self.finder_client_button)
        self.finder_client_button.clicked.connect(lambda: finderFunctions.finder_client(self))

        self.finder_client_lineedit = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_client_lineedit.setMinimumHeight(80)
        self.finder_client_lineedit.setMaximumHeight(80)
        self.finder_client_lineedit.setMinimumWidth(300)
        self.finder_client_lineedit.setMaximumWidth(600)
        self.ui.load_pages.finder_client_layout.addWidget(self.finder_client_lineedit)

        self.finder_bars1_button1 = PyPushButton(
            text="Sorszám: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars1_button1.setMinimumHeight(60)
        self.finder_bars1_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars1_layout.addWidget(self.finder_bars1_button1)
        self.finder_bars1_button1.clicked.connect(lambda: finderFunctions.finder_bar1(self))

        self.finder_bars1_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars1_lineedit1.setMinimumHeight(60)
        self.finder_bars1_lineedit1.setMaximumHeight(60)
        self.finder_bars1_lineedit1.setMinimumWidth(200)
        self.finder_bars1_lineedit1.setMaximumWidth(500)
        self.finder_bars1_lineedit1.setClearButtonEnabled(True)
        self.ui.load_pages.finder_bars1_layout.addWidget(self.finder_bars1_lineedit1)

        self.finder_bars1_button2 = PyPushButton(
            text="Dátum: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars1_button2.setMinimumHeight(60)
        self.finder_bars1_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars1_layout.addWidget(self.finder_bars1_button2)
        self.finder_bars1_button2.clicked.connect(lambda: finderFunctions.finder_bar1(self))

        self.finder_bars1_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars1_lineedit2.setMinimumHeight(60)
        self.finder_bars1_lineedit2.setMaximumHeight(60)
        self.finder_bars1_lineedit2.setMinimumWidth(200)
        self.finder_bars1_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars1_layout.addWidget(self.finder_bars1_lineedit2)

        self.finder_bars2_button1 = PyPushButton(
            text="Módozat: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars2_button1.setMinimumHeight(60)
        self.finder_bars2_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars2_layout.addWidget(self.finder_bars2_button1)
        #self.finder_bars2_button1.clicked.connect(lambda: finderFunctions.finder_bars2(self))

        self.finder_bars2_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars2_lineedit1.setMinimumHeight(60)
        self.finder_bars2_lineedit1.setMaximumHeight(60)
        self.finder_bars2_lineedit1.setMinimumWidth(200)
        self.finder_bars2_lineedit1.setMaximumWidth(500)
        self.ui.load_pages.finder_bars2_layout.addWidget(self.finder_bars2_lineedit1)

        self.finder_bars2_button2 = PyPushButton(
            text="Kötvényszám: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars2_button2.setMinimumHeight(60)
        self.finder_bars2_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars2_layout.addWidget(self.finder_bars2_button2)
        #self.finder_bars2_button2.clicked.connect(lambda: finderFunctions.finder_bars2(self))

        self.finder_bars2_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars2_lineedit2.setMinimumHeight(60)
        self.finder_bars2_lineedit2.setMaximumHeight(60)
        self.finder_bars2_lineedit2.setMinimumWidth(200)
        self.finder_bars2_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars2_layout.addWidget(self.finder_bars2_lineedit2)

        self.finder_bars3_button1 = PyPushButton(
            text="Szerzés/törlés: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars3_button1.setMinimumHeight(60)
        self.finder_bars3_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars3_layout.addWidget(self.finder_bars3_button1)
        #self.finder_bars3_button1.clicked.connect(lambda: finderFunctions.finder_bars3(self))

        self.finder_bars3_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars3_lineedit1.setMinimumHeight(60)
        self.finder_bars3_lineedit1.setMaximumHeight(60)
        self.finder_bars3_lineedit1.setMinimumWidth(200)
        self.finder_bars3_lineedit1.setMaximumWidth(500)
        self.ui.load_pages.finder_bars3_layout.addWidget(self.finder_bars3_lineedit1)

        self.finder_bars3_button2 = PyPushButton(
            text="Évforduló: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars3_button2.setMinimumHeight(60)
        self.finder_bars3_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars3_layout.addWidget(self.finder_bars3_button2)
        #self.finder_bars3_button2.clicked.connect(lambda: finderFunctions.finder_bars3(self))

        self.finder_bars3_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars3_lineedit2.setMinimumHeight(60)
        self.finder_bars3_lineedit2.setMaximumHeight(60)
        self.finder_bars3_lineedit2.setMinimumWidth(200)
        self.finder_bars3_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars3_layout.addWidget(self.finder_bars3_lineedit2)

        self.finder_bars4_button1 = PyPushButton(
            text="Éves díj: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars4_button1.setMinimumHeight(60)
        self.finder_bars4_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars4_layout.addWidget(self.finder_bars4_button1)
        #self.finder_bars4_button1.clicked.connect(lambda: finderFunctions.finder_bars4(self))

        self.finder_bars4_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars4_lineedit1.setMinimumHeight(60)
        self.finder_bars4_lineedit1.setMaximumHeight(60)
        self.finder_bars4_lineedit1.setMinimumWidth(200)
        self.finder_bars4_lineedit1.setMaximumWidth(500)
        self.ui.load_pages.finder_bars4_layout.addWidget(self.finder_bars4_lineedit1)

        self.finder_bars4_button2 = PyPushButton(
            text="Jutalék: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars4_button2.setMinimumHeight(60)
        self.finder_bars4_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars4_layout.addWidget(self.finder_bars4_button2)
        #self.finder_bars4_button2.clicked.connect(lambda: finderFunctions.finder_bars4(self))

        self.finder_bars4_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars4_lineedit2.setMinimumHeight(60)
        self.finder_bars4_lineedit2.setMaximumHeight(60)
        self.finder_bars4_lineedit2.setMinimumWidth(200)
        self.finder_bars4_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars4_layout.addWidget(self.finder_bars4_lineedit2)

        self.finder_bars5_button1 = PyPushButton(
            text="Díjfizetés üteme: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars5_button1.setMinimumHeight(60)
        self.finder_bars5_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars5_layout.addWidget(self.finder_bars5_button1)
        #self.finder_bars5_button1.clicked.connect(lambda: finderFunctions.finder_bars5(self))

        self.finder_bars5_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars5_lineedit1.setMinimumHeight(60)
        self.finder_bars5_lineedit1.setMaximumHeight(60)
        self.finder_bars5_lineedit1.setMinimumWidth(200)
        self.finder_bars5_lineedit1.setMaximumWidth(500)
        self.ui.load_pages.finder_bars5_layout.addWidget(self.finder_bars5_lineedit1)

        self.finder_bars5_button2 = PyPushButton(
            text="Irányítószám: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars5_button2.setMinimumHeight(60)
        self.finder_bars5_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars5_layout.addWidget(self.finder_bars5_button2)
        #self.finder_bars5_button2.clicked.connect(lambda: finderFunctions.finder_bars5(self))

        self.finder_bars5_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars5_lineedit2.setMinimumHeight(60)
        self.finder_bars5_lineedit2.setMaximumHeight(60)
        self.finder_bars5_lineedit2.setMinimumWidth(200)
        self.finder_bars5_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars5_layout.addWidget(self.finder_bars5_lineedit2)

        self.finder_bars6_button1 = PyPushButton(
            text="Cím: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars6_button1.setMinimumHeight(60)
        self.finder_bars6_button1.setMinimumWidth(200)
        self.ui.load_pages.finder_bars6_layout.addWidget(self.finder_bars6_button1)
        #self.finder_bars6_button1.clicked.connect(lambda: finderFunctions.finder_bars6(self))

        self.finder_bars6_lineedit1 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars6_lineedit1.setMinimumHeight(60)
        self.finder_bars6_lineedit1.setMaximumHeight(60)
        self.finder_bars6_lineedit1.setMinimumWidth(200)
        self.finder_bars6_lineedit1.setMaximumWidth(500)
        self.ui.load_pages.finder_bars6_layout.addWidget(self.finder_bars6_lineedit1)

        self.finder_bars6_button2 = PyPushButton(
            text="Email cím: ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            font="30pt Comic Sans MS",
        )
        self.finder_bars6_button2.setMinimumHeight(60)
        self.finder_bars6_button2.setMinimumWidth(200)
        self.ui.load_pages.finder_bars6_layout.addWidget(self.finder_bars6_button2)
        #self.finder_bars6_button2.clicked.connect(lambda: finderFunctions.finder_bars6(self))

        self.finder_bars6_lineedit2 = PyLineEdit(
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            bg_color=self.themes["app_color"]["dark_four"],
            bg_color_active=self.themes["app_color"]["dark_one"],
            context_color=self.themes["app_color"]["context_color"],
            font="19pt Comic Sans MS",
        )
        self.finder_bars6_lineedit2.setMinimumHeight(60)
        self.finder_bars6_lineedit2.setMaximumHeight(60)
        self.finder_bars6_lineedit2.setMinimumWidth(200)
        self.finder_bars6_lineedit2.setMaximumWidth(500)
        self.ui.load_pages.finder_bars6_layout.addWidget(self.finder_bars6_lineedit2)

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

