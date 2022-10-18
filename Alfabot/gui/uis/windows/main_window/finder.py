import gspread
import pandas as pd
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
from . ui_main import *
from qt_core import *
import sqlite3
import datetime
from gui.widgets import *
from . functions_main_window import *



class finderFunctions:
    def __init__(self):
        super().__init__()

    def finder_client(self):
        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        client_list_raw = c.fetchall()
        client_list = []
        for title in client_list_raw:
            client_list.append(title[0].replace('tbl_', '').replace('_', ' '))

        find_client = self.finder_client_lineedit.text()
        find_client_tabeled = 'tbl_' + find_client.replace(" ", "_")
        if find_client in client_list:
            c.execute(f"""SELECT * FROM {find_client_tabeled}""")
            client_all_row = c.fetchall()
            self.finder_table.setColumnCount(13)

            self.finder_table_column_1 = QTableWidgetItem()
            self.finder_table_column_1.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_1.setText("Sorszám")

            self.finder_table_column_2 = QTableWidgetItem()
            self.finder_table_column_2.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_2.setText("Dátum")

            self.finder_table_column_3 = QTableWidgetItem()
            self.finder_table_column_3.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_3.setText("Módozat")

            self.finder_table_column_4 = QTableWidgetItem()
            self.finder_table_column_4.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_4.setText("Kötvényszám")

            self.finder_table_column_5 = QTableWidgetItem()
            self.finder_table_column_5.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_5.setText("Sz vagy T")

            self.finder_table_column_6 = QTableWidgetItem()
            self.finder_table_column_6.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_6.setText("Évforduló")

            self.finder_table_column_7 = QTableWidgetItem()
            self.finder_table_column_7.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_7.setText("Éves díj")

            self.finder_table_column_8 = QTableWidgetItem()
            self.finder_table_column_8.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_8.setText("Jutalék")

            self.finder_table_column_9 = QTableWidgetItem()
            self.finder_table_column_9.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_9.setText("Díjfizteés üteme")

            self.finder_table_column_10 = QTableWidgetItem()
            self.finder_table_column_10.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_10.setText("Irányítószám")

            self.finder_table_column_11 = QTableWidgetItem()
            self.finder_table_column_11.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_11.setText("Cím")

            self.finder_table_column_12 = QTableWidgetItem()
            self.finder_table_column_12.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_12.setText("E-mail")

            self.finder_table_column_13 = QTableWidgetItem()
            self.finder_table_column_13.setTextAlignment(Qt.AlignCenter)
            self.finder_table_column_13.setText("Megjegyzés")

            # Set column
            self.finder_table.setHorizontalHeaderItem(0, self.finder_table_column_1)
            self.finder_table.setHorizontalHeaderItem(1, self.finder_table_column_2)
            self.finder_table.setHorizontalHeaderItem(2, self.finder_table_column_3)
            self.finder_table.setHorizontalHeaderItem(3, self.finder_table_column_4)
            self.finder_table.setHorizontalHeaderItem(4, self.finder_table_column_5)
            self.finder_table.setHorizontalHeaderItem(5, self.finder_table_column_6)
            self.finder_table.setHorizontalHeaderItem(6, self.finder_table_column_7)
            self.finder_table.setHorizontalHeaderItem(7, self.finder_table_column_8)
            self.finder_table.setHorizontalHeaderItem(8, self.finder_table_column_9)
            self.finder_table.setHorizontalHeaderItem(9, self.finder_table_column_10)
            self.finder_table.setHorizontalHeaderItem(10, self.finder_table_column_11)
            self.finder_table.setHorizontalHeaderItem(11, self.finder_table_column_12)
            self.finder_table.setHorizontalHeaderItem(12, self.finder_table_column_13)

            for row in client_all_row:
                row_number = self.finder_table.rowCount()
                self.finder_table.insertRow(row_number)  # Insert row

                self.finder_table.setItem(row_number, 0, QTableWidgetItem(str(row[0])))
                self.finder_table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
                self.finder_table.setItem(row_number, 2, QTableWidgetItem(str(row[2])))
                self.finder_table.setItem(row_number, 3, QTableWidgetItem(str(row[3])))
                self.finder_table.setItem(row_number, 4, QTableWidgetItem(str(row[4])))
                self.finder_table.setItem(row_number, 5, QTableWidgetItem(str(row[5])))
                self.finder_table.setItem(row_number, 6, QTableWidgetItem(str(row[6])))
                self.finder_table.setItem(row_number, 7, QTableWidgetItem(str(row[7])))
                self.finder_table.setItem(row_number, 8, QTableWidgetItem(str(row[8])))
                self.finder_table.setItem(row_number, 9, QTableWidgetItem(str(row[9])))
                self.finder_table.setItem(row_number, 10, QTableWidgetItem(str(row[10])))
                self.finder_table.setItem(row_number, 11, QTableWidgetItem(str(row[11])))
                self.finder_table.setItem(row_number, 12, QTableWidgetItem(str(row[12])))
                self.finder_table.setRowHeight(row_number, 50)

                #self.ui.load_pages.finder_table_layout.addWidget(self.finder_table)

            c.close()
            conn.close()
        else:
            print("nincs ilyen ügyfél")
            c.close()
            conn.close()

    def finder_bar1(self):
        self.finder_table.setRowCount(0)
        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        client_list_raw = c.fetchall()






        index = self.finder_bars1_lineedit1.text()
        date = self.finder_bars1_lineedit2.text()

        datas = []
        for x in client_list_raw:
            c.execute(f'SELECT * FROM "{x[0]}" WHERE "Index" LIKE ? AND "Dátum" LIKE ?',['%' + index + '%', '%' + date + '%'])
            current = c.fetchall()
            for y in current:
                datas.append(y)
        self.finder_table.setColumnCount(13)

        self.finder_table_column_1 = QTableWidgetItem()
        self.finder_table_column_1.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_1.setText("Sorszám")

        self.finder_table_column_2 = QTableWidgetItem()
        self.finder_table_column_2.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_2.setText("Dátum")

        self.finder_table_column_3 = QTableWidgetItem()
        self.finder_table_column_3.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_3.setText("Módozat")

        self.finder_table_column_4 = QTableWidgetItem()
        self.finder_table_column_4.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_4.setText("Kötvényszám")

        self.finder_table_column_5 = QTableWidgetItem()
        self.finder_table_column_5.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_5.setText("Sz vagy T")

        self.finder_table_column_6 = QTableWidgetItem()
        self.finder_table_column_6.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_6.setText("Évforduló")

        self.finder_table_column_7 = QTableWidgetItem()
        self.finder_table_column_7.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_7.setText("Éves díj")

        self.finder_table_column_8 = QTableWidgetItem()
        self.finder_table_column_8.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_8.setText("Jutalék")

        self.finder_table_column_9 = QTableWidgetItem()
        self.finder_table_column_9.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_9.setText("Díjfizteés üteme")

        self.finder_table_column_10 = QTableWidgetItem()
        self.finder_table_column_10.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_10.setText("Irányítószám")

        self.finder_table_column_11 = QTableWidgetItem()
        self.finder_table_column_11.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_11.setText("Cím")

        self.finder_table_column_12 = QTableWidgetItem()
        self.finder_table_column_12.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_12.setText("E-mail")

        self.finder_table_column_13 = QTableWidgetItem()
        self.finder_table_column_13.setTextAlignment(Qt.AlignCenter)
        self.finder_table_column_13.setText("Megjegyzés")

        # Set column
        self.finder_table.setHorizontalHeaderItem(0, self.finder_table_column_1)
        self.finder_table.setHorizontalHeaderItem(1, self.finder_table_column_2)
        self.finder_table.setHorizontalHeaderItem(2, self.finder_table_column_3)
        self.finder_table.setHorizontalHeaderItem(3, self.finder_table_column_4)
        self.finder_table.setHorizontalHeaderItem(4, self.finder_table_column_5)
        self.finder_table.setHorizontalHeaderItem(5, self.finder_table_column_6)
        self.finder_table.setHorizontalHeaderItem(6, self.finder_table_column_7)
        self.finder_table.setHorizontalHeaderItem(7, self.finder_table_column_8)
        self.finder_table.setHorizontalHeaderItem(8, self.finder_table_column_9)
        self.finder_table.setHorizontalHeaderItem(9, self.finder_table_column_10)
        self.finder_table.setHorizontalHeaderItem(10, self.finder_table_column_11)
        self.finder_table.setHorizontalHeaderItem(11, self.finder_table_column_12)
        self.finder_table.setHorizontalHeaderItem(12, self.finder_table_column_13)

        for row in datas:
            row_number = self.finder_table.rowCount()
            self.finder_table.insertRow(row_number)  # Insert row

            self.finder_table.setItem(row_number, 0, QTableWidgetItem(str(row[0])))
            self.finder_table.setItem(row_number, 1, QTableWidgetItem(str(row[1])))
            self.finder_table.setItem(row_number, 2, QTableWidgetItem(str(row[2])))
            self.finder_table.setItem(row_number, 3, QTableWidgetItem(str(row[3])))
            self.finder_table.setItem(row_number, 4, QTableWidgetItem(str(row[4])))
            self.finder_table.setItem(row_number, 5, QTableWidgetItem(str(row[5])))
            self.finder_table.setItem(row_number, 6, QTableWidgetItem(str(row[6])))
            self.finder_table.setItem(row_number, 7, QTableWidgetItem(str(row[7])))
            self.finder_table.setItem(row_number, 8, QTableWidgetItem(str(row[8])))
            self.finder_table.setItem(row_number, 9, QTableWidgetItem(str(row[9])))
            self.finder_table.setItem(row_number, 10, QTableWidgetItem(str(row[10])))
            self.finder_table.setItem(row_number, 11, QTableWidgetItem(str(row[11])))
            self.finder_table.setItem(row_number, 12, QTableWidgetItem(str(row[12])))
            self.finder_table.setRowHeight(row_number, 50)
            # self.ui.load_pages.finder_table_layout.addWidget(self.finder_table)
        c.close()
        conn.close()





