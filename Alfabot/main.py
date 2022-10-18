
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from gui.uis.windows.main_window.modify import *
from qt_core import *
from gui.core.json_settings import Settings
from gui.uis.windows.main_window import *
from gui.widgets import *

os.environ["QT_FONT_DPI"] = "96"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        settings = Settings()
        self.settings = settings.items
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)
        self.show()

    def btn_clicked(self):
        btn = SetupMainWindow.setup_btns(self)

        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_welcome)
        if btn.objectName() == "btn_widgets":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        if btn.objectName() == "btn_modify_user":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_search_main)
        if btn.objectName() == "btn_finder":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_finder)
        if btn.objectName() == "btn_info":
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )
        if btn.objectName() == "btn_top_settings":
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)
                MainFunctions.toggle_right_column(self)
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

        print(f"Button {btn.objectName()}, clicked!")

    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)
        print(f"Button {btn.objectName()}, released!")
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())