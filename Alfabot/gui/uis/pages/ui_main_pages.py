# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod2JAfCLl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.verticalLayout_3 = QVBoxLayout(self.page_welcome)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.welcome_title = QVBoxLayout()
        self.welcome_title.setObjectName(u"welcome_title")

        self.verticalLayout_3.addLayout(self.welcome_title)

        self.welcome_buttons = QHBoxLayout()
        self.welcome_buttons.setObjectName(u"welcome_buttons")

        self.verticalLayout_3.addLayout(self.welcome_buttons)

        self.pages.addWidget(self.page_welcome)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 269, 239))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_search_main = QWidget()
        self.page_search_main.setObjectName(u"page_search_main")
        self.verticalLayout_6 = QVBoxLayout(self.page_search_main)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.search_main_newc = QVBoxLayout()
        self.search_main_newc.setObjectName(u"search_main_newc")

        self.verticalLayout_6.addLayout(self.search_main_newc)

        self.search_main_existc = QVBoxLayout()
        self.search_main_existc.setObjectName(u"search_main_existc")

        self.verticalLayout_6.addLayout(self.search_main_existc)

        self.pages.addWidget(self.page_search_main)
        self.page_search_new_client = QWidget()
        self.page_search_new_client.setObjectName(u"page_search_new_client")
        self.verticalLayout_5 = QVBoxLayout(self.page_search_new_client)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.search_search_layout = QHBoxLayout()
        self.search_search_layout.setObjectName(u"search_search_layout")

        self.verticalLayout_5.addLayout(self.search_search_layout)

        self.search_label1_layout = QHBoxLayout()
        self.search_label1_layout.setObjectName(u"search_label1_layout")

        self.verticalLayout_5.addLayout(self.search_label1_layout)

        self.search_line1_layout = QHBoxLayout()
        self.search_line1_layout.setObjectName(u"search_line1_layout")

        self.verticalLayout_5.addLayout(self.search_line1_layout)

        self.search_label2_layout = QHBoxLayout()
        self.search_label2_layout.setObjectName(u"search_label2_layout")

        self.verticalLayout_5.addLayout(self.search_label2_layout)

        self.search_line2_layout = QHBoxLayout()
        self.search_line2_layout.setObjectName(u"search_line2_layout")

        self.verticalLayout_5.addLayout(self.search_line2_layout)

        self.search_label3_layout = QHBoxLayout()
        self.search_label3_layout.setObjectName(u"search_label3_layout")

        self.verticalLayout_5.addLayout(self.search_label3_layout)

        self.search_line3_layout = QHBoxLayout()
        self.search_line3_layout.setObjectName(u"search_line3_layout")

        self.verticalLayout_5.addLayout(self.search_line3_layout)

        self.search_sidenote_layout = QVBoxLayout()
        self.search_sidenote_layout.setObjectName(u"search_sidenote_layout")

        self.verticalLayout_5.addLayout(self.search_sidenote_layout)

        self.search_buttons_layout = QHBoxLayout()
        self.search_buttons_layout.setObjectName(u"search_buttons_layout")

        self.verticalLayout_5.addLayout(self.search_buttons_layout)

        self.pages.addWidget(self.page_search_new_client)
        self.page_search_exist_event = QWidget()
        self.page_search_exist_event.setObjectName(u"page_search_exist_event")
        self.verticalLayout_2 = QVBoxLayout(self.page_search_exist_event)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.search_exist_event_search_layout = QHBoxLayout()
        self.search_exist_event_search_layout.setObjectName(u"search_exist_event_search_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_search_layout)

        self.search_exist_event_label1_layout = QHBoxLayout()
        self.search_exist_event_label1_layout.setObjectName(u"search_exist_event_label1_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_label1_layout)

        self.search_exist_event_line1_layout = QHBoxLayout()
        self.search_exist_event_line1_layout.setObjectName(u"search_exist_event_line1_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_line1_layout)

        self.search_exist_event_label2_layout = QHBoxLayout()
        self.search_exist_event_label2_layout.setObjectName(u"search_exist_event_label2_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_label2_layout)

        self.search_exist_event_line2_layout = QHBoxLayout()
        self.search_exist_event_line2_layout.setObjectName(u"search_exist_event_line2_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_line2_layout)

        self.search_exist_event_label3_layout = QHBoxLayout()
        self.search_exist_event_label3_layout.setObjectName(u"search_exist_event_label3_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_label3_layout)

        self.search_exist_event_line3_layout = QHBoxLayout()
        self.search_exist_event_line3_layout.setObjectName(u"search_exist_event_line3_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_line3_layout)

        self.search_exist_event_sidenote_layout = QVBoxLayout()
        self.search_exist_event_sidenote_layout.setObjectName(u"search_exist_event_sidenote_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_sidenote_layout)

        self.search_exist_event_buttons_layout = QHBoxLayout()
        self.search_exist_event_buttons_layout.setObjectName(u"search_exist_event_buttons_layout")

        self.verticalLayout_2.addLayout(self.search_exist_event_buttons_layout)

        self.pages.addWidget(self.page_search_exist_event)
        self.page_search_exist_data = QWidget()
        self.page_search_exist_data.setObjectName(u"page_search_exist_data")
        self.verticalLayout_4 = QVBoxLayout(self.page_search_exist_data)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.search_exist_data_search_layout = QHBoxLayout()
        self.search_exist_data_search_layout.setObjectName(u"search_exist_data_search_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_search_layout)

        self.search_exist_data_label1_layout = QHBoxLayout()
        self.search_exist_data_label1_layout.setObjectName(u"search_exist_data_label1_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_label1_layout)

        self.search_exist_data_line1_layout = QHBoxLayout()
        self.search_exist_data_line1_layout.setObjectName(u"search_exist_data_line1_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_line1_layout)

        self.search_exist_data_label2_layout = QHBoxLayout()
        self.search_exist_data_label2_layout.setObjectName(u"search_exist_data_label2_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_label2_layout)

        self.search_exist_data_line2_layout = QHBoxLayout()
        self.search_exist_data_line2_layout.setObjectName(u"search_exist_data_line2_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_line2_layout)

        self.search_exist_data_buttons_layout = QHBoxLayout()
        self.search_exist_data_buttons_layout.setObjectName(u"search_exist_data_buttons_layout")

        self.verticalLayout_4.addLayout(self.search_exist_data_buttons_layout)

        self.pages.addWidget(self.page_search_exist_data)
        self.page_finder = QWidget()
        self.page_finder.setObjectName(u"page_finder")
        self.verticalLayout_8 = QVBoxLayout(self.page_finder)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.finder_table_layout = QVBoxLayout()
        self.finder_table_layout.setObjectName(u"finder_table_layout")

        self.verticalLayout_8.addLayout(self.finder_table_layout)

        self.finder_client_layout = QHBoxLayout()
        self.finder_client_layout.setObjectName(u"finder_client_layout")

        self.verticalLayout_8.addLayout(self.finder_client_layout)

        self.finder_bars1_layout = QHBoxLayout()
        self.finder_bars1_layout.setObjectName(u"finder_bars1_layout")

        self.verticalLayout_8.addLayout(self.finder_bars1_layout)

        self.finder_bars2_layout = QHBoxLayout()
        self.finder_bars2_layout.setObjectName(u"finder_bars2_layout")

        self.verticalLayout_8.addLayout(self.finder_bars2_layout)

        self.finder_bars3_layout = QHBoxLayout()
        self.finder_bars3_layout.setObjectName(u"finder_bars3_layout")

        self.verticalLayout_8.addLayout(self.finder_bars3_layout)

        self.finder_bars4_layout = QHBoxLayout()
        self.finder_bars4_layout.setObjectName(u"finder_bars4_layout")

        self.verticalLayout_8.addLayout(self.finder_bars4_layout)

        self.finder_bars5_layout = QHBoxLayout()
        self.finder_bars5_layout.setObjectName(u"finder_bars5_layout")

        self.verticalLayout_8.addLayout(self.finder_bars5_layout)

        self.finder_bars6_layout = QHBoxLayout()
        self.finder_bars6_layout.setObjectName(u"finder_bars6_layout")

        self.verticalLayout_8.addLayout(self.finder_bars6_layout)

        self.pages.addWidget(self.page_finder)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainPages)

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Demo oldal mintának", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Ez itt akár lorem ipsum is lehetne de épp nem az.\n"
"Új sorban folytathatnám bölcsességeim, de inkább nem teszem", None))


