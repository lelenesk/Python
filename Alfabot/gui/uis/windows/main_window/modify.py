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


class modifyFunctions:
    def __init__(self):
        super().__init__()

    gc = gspread.service_account(filename='client.json')
    client_doc = gc.open('Ügyfélállomány')
    all_doc = gc.open('Állományom')
    worksheet_list_client = client_doc.worksheets()
    worksheet_list_all = all_doc.worksheets()

    def search_destroyer(self):
        #meglévő event
        try:
            self.load_existing_event_label1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label5.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label6.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label7.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label11.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label12.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label13.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit5.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit6.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit7.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit11.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit12.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_wrongname_label.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_textbrowser.setParent(None)
        except:
            print("nincs widget")

        try:
            self.load_existing_event_button2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_button3.setParent(None)
        except:
            print("nincs widget")
        #meglévő data
        try:
            self.load_existing_data_label1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_label2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_label3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_lineedit1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_lineedit2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_lineedit3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_wrongname_label.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_button2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_button3.setParent(None)
        except:
            print("nincs widget")
        #newclient
        try:
            self.load_newclient_label1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label5.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label6.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label7.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label11.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label12.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label13.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit1.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit5.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit6.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit7.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit11.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit12.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_wrongname_label.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_textbrowser.setParent(None)
        except:
            print("nincs widget")

        try:
            self.load_newclient_button2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_button3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label15.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label16.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_label17.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit15.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit16.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_lineedit17.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_wrongname_label.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_button2.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_newclient_button3.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label15.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label16.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_label17.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit8.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit9.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_event_lineedit10.setParent(None)
        except:
            print("nincs widget")
        try:
            self.existing_data_label4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.existing_data_label5.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_lineedit4.setParent(None)
        except:
            print("nincs widget")
        try:
            self.load_existing_data_lineedit5.setParent(None)
        except:
            print("nincs widget")




    def load_google_test_data(self, worksheet_list_client):

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()

        for worksheet in worksheet_list_client:
            current_sheet_data = pd.DataFrame(worksheet.get_all_records())
            sheet_title = worksheet.title
            sql_table_name = 'tbl_' + sheet_title

            #current_sheet_data['Dátum'] = pd.to_datetime(current_sheet_data['Dátum'],format='%Y.%m.%d.').day_name()
            current_sheet_data['Kötvényszám'] = current_sheet_data['Kötvényszám'].astype(str, errors='ignore')
            current_sheet_data['Éves díj'] = current_sheet_data['Éves díj'].astype(int, errors='ignore')
            current_sheet_data['Évforduló'] = current_sheet_data['Évforduló'].astype('datetime64[ns]', errors='ignore')
            current_sheet_data['Index'] = current_sheet_data['Index'].astype(int, errors='ignore')

            c.execute("DROP TABLE " + sql_table_name)
            """
            c.execute(
                'CREATE TABLE IF NOT EXISTS' + ' ' + 'tbl_Kovács_Géza' + '( "Sorszám" INTEGER, "Esemény Dátuma" TEXT,'
                                                                         '"Szerzés vagy Törlés" TEXT,'
                                                                         '"Módozat" TEXT,'
                                                                         '"Kötvényszám"	TEXT,'
                                                                         '"Kötés ádtuma"	TEXT,'
                                                                         '"Éves díj"	INTEGER,'
                                                                         '"Jutalék"	INTEGER,'
                                                                         '"Évforduló" TEXT,'
                                                                         '"Díjfizetés üteme"	TEXT,'
                                                                         '"Irányítószám"	TEXT,'
                                                                         '"Cím"	TEXT,'
                                                                         '"Telefonszám"	TEXT,'
                                                                         '"E-mail cím"	TEXT,'
                                                                         '"Megjegyzés"	TEXT,'
                                                                         '"Milye nincs"	TEXT,'
                                                                         '"Állomány"	TEXT);')
            conn.commit()
            print("A generalo kész")
            """

            c.execute("CREATE TABLE IF NOT EXISTS" + " " + str(sql_table_name) + " ("
            "'Index' INTEGER, Dátum TEXT, Módozat TEXT, Kötvényszám TEXT, 'Szerzés vagy Törlés' TEXT, Évforduló TEXT,"
            "'Éves díj' TEXT, Jutalék TEXT, 'Díjfizetés üteme' TEXT, Irányítószám TEXT, Cím TEXT, 'E-mail cím' TEXT, Megjegyzés TEXT)")
            current_sheet_data.to_sql(sql_table_name, conn, if_exists='replace', index=False)
            conn.commit()
        print("A példa ügyfelek google tablazatból betöltve")
        c.close()
        conn.close()

    def page_modify_insertnewclient(self):
        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        client_list_raw = c.fetchall()
        client_list = []
        for title in client_list_raw:
            client_list.append(title[0].replace('tbl_', '').replace('_', ' '))

        searched_client = self.load_newclient_lineedit.text()
        searched_client_tabeled = 'tbl_' + searched_client.replace(" ", "_")
        if searched_client not in client_list:
            modifyFunctions.search_destroyer(self)

            self.load_newclient_label15 = PyLabel(
                text="Cím",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label15.setMinimumHeight(60)
            self.load_newclient_label15.setMaximumHeight(60)
            self.load_newclient_label15.setMinimumWidth(1)
            self.load_newclient_label15.setMaximumWidth(300)
            self.ui.load_pages.search_label1_layout.addWidget(self.load_newclient_label15)

            self.load_newclient_label16 = PyLabel(
                text="Irányítószám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label16.setMinimumHeight(60)
            self.load_newclient_label16.setMaximumHeight(60)
            self.load_newclient_label16.setMinimumWidth(1)
            self.load_newclient_label16.setMaximumWidth(300)
            self.ui.load_pages.search_label2_layout.addWidget(self.load_newclient_label16)

            self.load_newclient_label17 = PyLabel(
                text="Email cím",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label17.setMinimumHeight(60)
            self.load_newclient_label17.setMaximumHeight(60)
            self.load_newclient_label17.setMinimumWidth(1)
            self.load_newclient_label17.setMaximumWidth(300)
            self.ui.load_pages.search_label3_layout.addWidget(self.load_newclient_label17)

            self.load_newclient_lineedit15 = PyLineEdit(
                text="        ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit15.setMaximumWidth(400)
            self.load_newclient_lineedit15.setMaximumHeight(80)
            self.load_newclient_lineedit15.setMinimumWidth(150)
            self.load_newclient_lineedit15.setMinimumHeight(80)
            self.ui.load_pages.search_line1_layout.addWidget(self.load_newclient_lineedit15)

            self.load_newclient_lineedit16 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit16.setMaximumWidth(400)
            self.load_newclient_lineedit16.setMaximumHeight(80)
            self.load_newclient_lineedit16.setMinimumWidth(150)
            self.load_newclient_lineedit16.setMinimumHeight(80)
            self.ui.load_pages.search_line2_layout.addWidget(self.load_newclient_lineedit16)

            self.load_newclient_lineedit17 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit17.setMaximumWidth(400)
            self.load_newclient_lineedit17.setMaximumHeight(80)
            self.load_newclient_lineedit17.setMinimumWidth(150)
            self.load_newclient_lineedit17.setMinimumHeight(80)
            self.ui.load_pages.search_line3_layout.addWidget(self.load_newclient_lineedit17)

            self.load_newclient_label1 = PyLabel(
                text="Kötvényszám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label1.setMinimumHeight(60)
            self.load_newclient_label1.setMaximumHeight(60)
            self.load_newclient_label1.setMinimumWidth(1)
            self.load_newclient_label1.setMaximumWidth(300)
            self.ui.load_pages.search_label1_layout.addWidget(self.load_newclient_label1)

            self.load_newclient_label2 = PyLabel(
                text="Módozat",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label2.setMinimumHeight(60)
            self.load_newclient_label2.setMaximumHeight(60)
            self.load_newclient_label2.setMinimumWidth(1)
            self.load_newclient_label2.setMaximumWidth(300)
            self.ui.load_pages.search_label1_layout.addWidget(self.load_newclient_label2)

            self.load_newclient_label3 = PyLabel(
                text="Szerzés v. Törlés",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label3.setMinimumHeight(60)
            self.load_newclient_label3.setMaximumHeight(60)
            self.load_newclient_label3.setMinimumWidth(1)
            self.load_newclient_label3.setMaximumWidth(300)
            self.ui.load_pages.search_label1_layout.addWidget(self.load_newclient_label3)

            self.load_newclient_lineedit1 = PyLineEdit(
                text="        ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit1.setMaximumWidth(400)
            self.load_newclient_lineedit1.setMaximumHeight(80)
            self.load_newclient_lineedit1.setMinimumWidth(150)
            self.load_newclient_lineedit1.setMinimumHeight(80)
            self.ui.load_pages.search_line1_layout.addWidget(self.load_newclient_lineedit1)

            self.load_newclient_lineedit2 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit2.setMaximumWidth(400)
            self.load_newclient_lineedit2.setMaximumHeight(80)
            self.load_newclient_lineedit2.setMinimumWidth(150)
            self.load_newclient_lineedit2.setMinimumHeight(80)
            self.ui.load_pages.search_line1_layout.addWidget(self.load_newclient_lineedit2)

            self.load_newclient_lineedit3 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit3.setMaximumWidth(400)
            self.load_newclient_lineedit3.setMaximumHeight(80)
            self.load_newclient_lineedit3.setMinimumWidth(150)
            self.load_newclient_lineedit3.setMinimumHeight(80)
            self.ui.load_pages.search_line1_layout.addWidget(self.load_newclient_lineedit3)

            self.load_newclient_label4 = PyLabel(
                text="Kötés dátuma",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label4.setMinimumHeight(60)
            self.load_newclient_label4.setMaximumHeight(60)
            self.load_newclient_label4.setMinimumWidth(1)
            self.load_newclient_label4.setMaximumWidth(300)
            self.ui.load_pages.search_label2_layout.addWidget(self.load_newclient_label4)

            self.load_newclient_label5 = PyLabel(
                text="Éves díj",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label5.setMinimumHeight(60)
            self.load_newclient_label5.setMaximumHeight(60)
            self.load_newclient_label5.setMinimumWidth(1)
            self.load_newclient_label5.setMaximumWidth(300)
            self.ui.load_pages.search_label2_layout.addWidget(self.load_newclient_label5)

            self.load_newclient_label6 = PyLabel(
                text="Jutalékom",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label6.setMinimumHeight(60)
            self.load_newclient_label6.setMaximumHeight(60)
            self.load_newclient_label6.setMinimumWidth(1)
            self.load_newclient_label6.setMaximumWidth(300)
            self.ui.load_pages.search_label2_layout.addWidget(self.load_newclient_label6)

            self.load_newclient_label7 = PyLabel(
                text="Fizetési ütem",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label7.setMinimumHeight(60)
            self.load_newclient_label7.setMaximumHeight(60)
            self.load_newclient_label7.setMinimumWidth(1)
            self.load_newclient_label7.setMaximumWidth(300)
            self.ui.load_pages.search_label3_layout.addWidget(self.load_newclient_label7)

            self.load_newclient_lineedit4 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit4.setMaximumWidth(400)
            self.load_newclient_lineedit4.setMaximumHeight(80)
            self.load_newclient_lineedit4.setMinimumWidth(150)
            self.load_newclient_lineedit4.setMinimumHeight(80)
            self.ui.load_pages.search_line2_layout.addWidget(self.load_newclient_lineedit4)

            self.load_newclient_lineedit5 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit5.setMaximumWidth(400)
            self.load_newclient_lineedit5.setMaximumHeight(80)
            self.load_newclient_lineedit5.setMinimumWidth(150)
            self.load_newclient_lineedit5.setMinimumHeight(80)
            self.ui.load_pages.search_line2_layout.addWidget(self.load_newclient_lineedit5)

            self.load_newclient_lineedit6 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit6.setMaximumWidth(400)
            self.load_newclient_lineedit6.setMaximumHeight(80)
            self.load_newclient_lineedit6.setMinimumWidth(150)
            self.load_newclient_lineedit6.setMinimumHeight(80)
            self.ui.load_pages.search_line2_layout.addWidget(self.load_newclient_lineedit6)

            self.load_newclient_lineedit7 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit7.setMaximumWidth(400)
            self.load_newclient_lineedit7.setMaximumHeight(80)
            self.load_newclient_lineedit7.setMinimumWidth(150)
            self.load_newclient_lineedit7.setMinimumHeight(80)
            self.ui.load_pages.search_line3_layout.addWidget(self.load_newclient_lineedit7)

            self.load_newclient_label12 = PyLabel(
                text="Dátum",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label12.setMinimumHeight(60)
            self.load_newclient_label12.setMaximumHeight(60)
            self.load_newclient_label12.setMinimumWidth(1)
            self.load_newclient_label12.setMaximumWidth(300)
            self.ui.load_pages.search_label3_layout.addWidget(self.load_newclient_label12)

            self.load_newclient_lineedit11 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit11.setMaximumWidth(400)
            self.load_newclient_lineedit11.setMaximumHeight(80)
            self.load_newclient_lineedit11.setMinimumWidth(150)
            self.load_newclient_lineedit11.setMinimumHeight(80)
            self.ui.load_pages.search_line3_layout.addWidget(self.load_newclient_lineedit11)

            self.load_newclient_label13 = PyLabel(
                text="Sorszám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_newclient_label13.setMinimumHeight(60)
            self.load_newclient_label13.setMaximumHeight(60)
            self.load_newclient_label13.setMinimumWidth(1)
            self.load_newclient_label13.setMaximumWidth(300)
            self.ui.load_pages.search_label3_layout.addWidget(self.load_newclient_label13)

            self.load_newclient_lineedit12 = PyLineEdit(
                text="       ",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_newclient_lineedit12.setMaximumWidth(400)
            self.load_newclient_lineedit12.setMaximumHeight(80)
            self.load_newclient_lineedit12.setMinimumWidth(150)
            self.load_newclient_lineedit12.setMinimumHeight(80)
            self.ui.load_pages.search_line3_layout.addWidget(self.load_newclient_lineedit12)

            self.load_newclient_label11 = PyLabel(
                text="Megjegyzések",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS", )

            self.load_newclient_label11.setMinimumHeight(60)
            self.load_newclient_label11.setMaximumHeight(60)
            self.load_newclient_label11.setMinimumWidth(1)
            self.load_newclient_label11.setMaximumWidth(300)
            self.ui.load_pages.search_sidenote_layout.addWidget(self.load_newclient_label11,
                                                                            alignment=Qt.AlignCenter)

            self.load_newclient_textbrowser = PyTextBrowser(
                radius=8,
                color=self.themes["app_color"]["context_color"],
                bg_color=self.themes["app_color"]["dark_four"],
                selection_color=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["dark_four"],
                scroll_bar_bg_color=self.themes["app_color"]["dark_four"],
                scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS",
            )
            self.load_newclient_textbrowser.setMinimumHeight(200)
            self.load_newclient_textbrowser.setMaximumHeight(500)
            self.load_newclient_textbrowser.setMinimumWidth(400)
            self.load_newclient_textbrowser.setMaximumWidth(1900)
            self.load_newclient_textbrowser.setReadOnly(False)
            self.ui.load_pages.search_sidenote_layout.addWidget(self.load_newclient_textbrowser)

            self.load_newclient_button3 = PyPushButton(
                text="Visszalépés (bevitel nélkül)",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_newclient_button3.setMinimumHeight(100)
            self.load_newclient_button3.setMinimumWidth(250)
            self.ui.load_pages.search_buttons_layout.addWidget(self.load_newclient_button3)
            self.load_newclient_button3.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            self.load_newclient_button2 = PyPushButton(
                text="Új ügyfél rögzítése",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_newclient_button2.setMinimumHeight(100)
            self.load_newclient_button2.setMinimumWidth(250)
            self.load_newclient_button2.clicked.connect(lambda: modifyFunctions.page_modify_insert_client(self))
            self.ui.load_pages.search_buttons_layout.addWidget(self.load_newclient_button2)
            self.load_newclient_button3.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            c.close()
            conn.close()

        else:
            modifyFunctions.search_destroyer(self)
            self.load_newclient_wrongname_label = PyLabel(
                text="Az ügyfél már létezik az adatbázisban, ellenőrizd!",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS", )

            self.load_newclient_wrongname_label.setMinimumHeight(60)
            self.load_newclient_wrongname_label.setMaximumHeight(60)
            self.load_newclient_wrongname_label.setMinimumWidth(1)
            self.load_newclient_wrongname_label.setMaximumWidth(300)
            self.ui.load_pages.search_sidenote_layout.addWidget(self.load_newclient_wrongname_label,
                                                                           alignment=Qt.AlignCenter)
            c.close()
            conn.close()

    def page_modify_event_setter(self):

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        client_list_raw = c.fetchall()
        client_list =[]
        for title in client_list_raw:
            client_list.append(title[0].replace('tbl_', '').replace('_', ' '))

        searched_client = self.load_existing_event_cilent_lineedit.text()
        searched_client_tabeled = 'tbl_' + searched_client.replace(" ","_")
        if searched_client in client_list:
            modifyFunctions.search_destroyer(self)
            self.load_existing_event_label1 = PyLabel(
                text="Kötvényszám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label1.setMinimumHeight(60)
            self.load_existing_event_label1.setMaximumHeight(60)
            self.load_existing_event_label1.setMinimumWidth(1)
            self.load_existing_event_label1.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label1_layout.addWidget(self.load_existing_event_label1)

            self.load_existing_event_label2 = PyLabel(
                text="Módozat",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label2.setMinimumHeight(60)
            self.load_existing_event_label2.setMaximumHeight(60)
            self.load_existing_event_label2.setMinimumWidth(1)
            self.load_existing_event_label2.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label1_layout.addWidget(self.load_existing_event_label2)

            self.load_existing_event_label3 = PyLabel(
                text="Szerzés v. Törlés",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label3.setMinimumHeight(60)
            self.load_existing_event_label3.setMaximumHeight(60)
            self.load_existing_event_label3.setMinimumWidth(1)
            self.load_existing_event_label3.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label1_layout.addWidget(self.load_existing_event_label3)

            self.load_existing_event_lineedit1 = PyLineEdit(
                text="1",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit1.setMaximumWidth(400)
            self.load_existing_event_lineedit1.setMaximumHeight(80)
            self.load_existing_event_lineedit1.setMinimumWidth(150)
            self.load_existing_event_lineedit1.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line1_layout.addWidget(self.load_existing_event_lineedit1)

            self.load_existing_event_lineedit2 = PyLineEdit(
                text="2",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit2.setMaximumWidth(400)
            self.load_existing_event_lineedit2.setMaximumHeight(80)
            self.load_existing_event_lineedit2.setMinimumWidth(150)
            self.load_existing_event_lineedit2.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line1_layout.addWidget(self.load_existing_event_lineedit2)

            self.load_existing_event_lineedit3 = PyLineEdit(
                text="3",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit3.setMaximumWidth(400)
            self.load_existing_event_lineedit3.setMaximumHeight(80)
            self.load_existing_event_lineedit3.setMinimumWidth(150)
            self.load_existing_event_lineedit3.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line1_layout.addWidget(self.load_existing_event_lineedit3)

            self.load_existing_event_label4 = PyLabel(
                text="Esemény dátuma",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label4.setMinimumHeight(60)
            self.load_existing_event_label4.setMaximumHeight(60)
            self.load_existing_event_label4.setMinimumWidth(1)
            self.load_existing_event_label4.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label2_layout.addWidget(self.load_existing_event_label4)

            self.load_existing_event_label5 = PyLabel(
                text="Éves díj",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label5.setMinimumHeight(60)
            self.load_existing_event_label5.setMaximumHeight(60)
            self.load_existing_event_label5.setMinimumWidth(1)
            self.load_existing_event_label5.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label2_layout.addWidget(self.load_existing_event_label5)

            self.load_existing_event_label6 = PyLabel(
                text="Jutalékom",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label6.setMinimumHeight(60)
            self.load_existing_event_label6.setMaximumHeight(60)
            self.load_existing_event_label6.setMinimumWidth(1)
            self.load_existing_event_label6.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label2_layout.addWidget(self.load_existing_event_label6)

            self.load_existing_event_label7 = PyLabel(
                text="Fizetési ütem",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label7.setMinimumHeight(60)
            self.load_existing_event_label7.setMaximumHeight(60)
            self.load_existing_event_label7.setMinimumWidth(1)
            self.load_existing_event_label7.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label3_layout.addWidget(self.load_existing_event_label7)

            self.load_existing_event_lineedit4 = PyLineEdit(
                text="4",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit4.setMaximumWidth(400)
            self.load_existing_event_lineedit4.setMaximumHeight(80)
            self.load_existing_event_lineedit4.setMinimumWidth(150)
            self.load_existing_event_lineedit4.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line2_layout.addWidget(self.load_existing_event_lineedit4)

            self.load_existing_event_lineedit5 = PyLineEdit(
                text="5",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit5.setMaximumWidth(400)
            self.load_existing_event_lineedit5.setMaximumHeight(80)
            self.load_existing_event_lineedit5.setMinimumWidth(150)
            self.load_existing_event_lineedit5.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line2_layout.addWidget(self.load_existing_event_lineedit5)

            self.load_existing_event_lineedit6 = PyLineEdit(
                text="6",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit6.setMaximumWidth(400)
            self.load_existing_event_lineedit6.setMaximumHeight(80)
            self.load_existing_event_lineedit6.setMinimumWidth(150)
            self.load_existing_event_lineedit6.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line2_layout.addWidget(self.load_existing_event_lineedit6)

            self.load_existing_event_lineedit7 = PyLineEdit(
                text="7",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit7.setMaximumWidth(400)
            self.load_existing_event_lineedit7.setMaximumHeight(80)
            self.load_existing_event_lineedit7.setMinimumWidth(150)
            self.load_existing_event_lineedit7.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line3_layout.addWidget(self.load_existing_event_lineedit7)

            self.load_existing_event_lineedit8 = PyLineEdit(
                text="8",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit8.setMaximumWidth(400)
            self.load_existing_event_lineedit8.setMaximumHeight(80)
            self.load_existing_event_lineedit8.setMinimumWidth(150)
            self.load_existing_event_lineedit8.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line1_layout.addWidget(self.load_existing_event_lineedit8)

            self.load_existing_event_lineedit9 = PyLineEdit(
                text="9",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit9.setMaximumWidth(400)
            self.load_existing_event_lineedit9.setMaximumHeight(80)
            self.load_existing_event_lineedit9.setMinimumWidth(150)
            self.load_existing_event_lineedit9.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line2_layout.addWidget(self.load_existing_event_lineedit9)

            self.load_existing_event_lineedit10 = PyLineEdit(
                text="10",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit10.setMaximumWidth(400)
            self.load_existing_event_lineedit10.setMaximumHeight(80)
            self.load_existing_event_lineedit10.setMinimumWidth(150)
            self.load_existing_event_lineedit10.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line3_layout.addWidget(self.load_existing_event_lineedit10)

            self.load_existing_event_label12 = PyLabel(
                text="Kötés Dátuma",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label12.setMinimumHeight(60)
            self.load_existing_event_label12.setMaximumHeight(60)
            self.load_existing_event_label12.setMinimumWidth(1)
            self.load_existing_event_label12.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label3_layout.addWidget(self.load_existing_event_label12)


            self.load_existing_event_label15 = PyLabel(
                text="Sorszám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label15.setMinimumHeight(60)
            self.load_existing_event_label15.setMaximumHeight(60)
            self.load_existing_event_label15.setMinimumWidth(1)
            self.load_existing_event_label15.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label1_layout.addWidget(self.load_existing_event_label15)

            self.load_existing_event_label16 = PyLabel(
                text="Évforduló",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label16.setMinimumHeight(60)
            self.load_existing_event_label16.setMaximumHeight(60)
            self.load_existing_event_label16.setMinimumWidth(1)
            self.load_existing_event_label16.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label2_layout.addWidget(self.load_existing_event_label16)

            self.load_existing_event_label17 = PyLabel(
                text="Állomány",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label17.setMinimumHeight(60)
            self.load_existing_event_label17.setMaximumHeight(60)
            self.load_existing_event_label17.setMinimumWidth(1)
            self.load_existing_event_label17.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label3_layout.addWidget(self.load_existing_event_label17)

            self.load_existing_event_lineedit11 = PyLineEdit(
                text="11",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit11.setMaximumWidth(400)
            self.load_existing_event_lineedit11.setMaximumHeight(80)
            self.load_existing_event_lineedit11.setMinimumWidth(150)
            self.load_existing_event_lineedit11.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line3_layout.addWidget(self.load_existing_event_lineedit11)

            self.load_existing_event_label13 = PyLabel(
                text="Valami üres",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_event_label13.setMinimumHeight(60)
            self.load_existing_event_label13.setMaximumHeight(60)
            self.load_existing_event_label13.setMinimumWidth(1)
            self.load_existing_event_label13.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_label3_layout.addWidget(self.load_existing_event_label13)

            self.load_existing_event_lineedit12 = PyLineEdit(
                text="12",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_event_lineedit12.setMaximumWidth(400)
            self.load_existing_event_lineedit12.setMaximumHeight(80)
            self.load_existing_event_lineedit12.setMinimumWidth(150)
            self.load_existing_event_lineedit12.setMinimumHeight(80)
            self.ui.load_pages.search_exist_event_line3_layout.addWidget(self.load_existing_event_lineedit12)

            self.load_existing_event_label11 = PyLabel(
                text="Megjegyzések",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS", )

            self.load_existing_event_label11.setMinimumHeight(60)
            self.load_existing_event_label11.setMaximumHeight(60)
            self.load_existing_event_label11.setMinimumWidth(1)
            self.load_existing_event_label11.setMaximumWidth(300)
            self.ui.load_pages.search_exist_event_sidenote_layout.addWidget(self.load_existing_event_label11,
                                                                  alignment=Qt.AlignCenter)

            self.load_existing_event_textbrowser = PyTextBrowser(
                radius=8,
                color=self.themes["app_color"]["context_color"],
                bg_color=self.themes["app_color"]["dark_four"],
                selection_color=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["dark_four"],
                scroll_bar_bg_color=self.themes["app_color"]["dark_four"],
                scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS",
            )
            self.load_existing_event_textbrowser.setMinimumHeight(200)
            self.load_existing_event_textbrowser.setMaximumHeight(500)
            self.load_existing_event_textbrowser.setMinimumWidth(400)
            self.load_existing_event_textbrowser.setMaximumWidth(1900)
            self.load_existing_event_textbrowser.setReadOnly(False)
            self.ui.load_pages.search_exist_event_sidenote_layout.addWidget(self.load_existing_event_textbrowser)

            self.load_existing_event_button3 = PyPushButton(
                text="Visszalépés (módosítás nélkül)",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_existing_event_button3.setMinimumHeight(100)
            self.load_existing_event_button3.setMinimumWidth(250)
            self.ui.load_pages.search_exist_event_buttons_layout.addWidget(self.load_existing_event_button3)
            self.load_existing_event_button3.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            self.load_existing_event_button2 = PyPushButton(
                text="Új esemény felvitele",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_existing_event_button2.setMinimumHeight(100)
            self.load_existing_event_button2.setMinimumWidth(250)
            self.load_existing_event_button2.clicked.connect(lambda: modifyFunctions.page_modify_insert_event(self))
            self.ui.load_pages.search_exist_event_buttons_layout.addWidget(self.load_existing_event_button2)
            self.load_existing_event_button2.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            c.close()
            conn.close()

        else:
            modifyFunctions.search_destroyer(self)
            self.load_existing_event_wrongname_label = PyLabel(
                text="Rossz nevet írtál be, a keresett ügyfél nincs az adatbázisban",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS", )

            self.load_existing_event_wrongname_label.setMinimumHeight(200)
            self.load_existing_event_wrongname_label.setMaximumHeight(300)
            self.load_existing_event_wrongname_label.setMinimumWidth(300)
            self.load_existing_event_wrongname_label.setMaximumWidth(500)
            self.ui.load_pages.search_exist_event_buttons_layout.addWidget(self.load_existing_event_wrongname_label,alignment=Qt.AlignCenter)
            c.close()
            conn.close()

    def page_modify_data_setter(self):

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        client_list_raw = c.fetchall()
        client_list =[]
        for title in client_list_raw:
            client_list.append(title[0].replace('tbl_', '').replace('_', ' '))

        searched_client = self.load_existing_data_cilent_lineedit.text()
        searched_client_tabeled = 'tbl_' + searched_client.replace(" ","_")
        if searched_client in client_list:
            modifyFunctions.search_destroyer(self)
            self.load_existing_data_label1 = PyLabel(
                text="Cím",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_data_label1.setMinimumHeight(60)
            self.load_existing_data_label1.setMaximumHeight(60)
            self.load_existing_data_label1.setMinimumWidth(1)
            self.load_existing_data_label1.setMaximumWidth(300)
            self.ui.load_pages.search_exist_data_label1_layout.addWidget(self.load_existing_data_label1)

            self.load_existing_data_label2 = PyLabel(
                text="Irányítószám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_data_label2.setMinimumHeight(60)
            self.load_existing_data_label2.setMaximumHeight(60)
            self.load_existing_data_label2.setMinimumWidth(1)
            self.load_existing_data_label2.setMaximumWidth(300)
            self.ui.load_pages.search_exist_data_label1_layout.addWidget(self.load_existing_data_label2)

            self.load_existing_data_label3 = PyLabel(
                text="Email cím",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_data_label3.setMinimumHeight(60)
            self.load_existing_data_label3.setMaximumHeight(60)
            self.load_existing_data_label3.setMinimumWidth(1)
            self.load_existing_data_label3.setMaximumWidth(300)
            self.ui.load_pages.search_exist_data_label1_layout.addWidget(self.load_existing_data_label3)

            self.load_existing_data_label4 = PyLabel(
                text="Telefonszám",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_data_label4.setMinimumHeight(60)
            self.load_existing_data_label4.setMaximumHeight(60)
            self.load_existing_data_label4.setMinimumWidth(1)
            self.load_existing_data_label4.setMaximumWidth(300)
            self.ui.load_pages.search_exist_data_label1_layout.addWidget(self.load_existing_data_label4)

            self.load_existing_data_label5 = PyLabel(
                text="Milye nincs",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="18pt Comic Sans MS", )

            self.load_existing_data_label5.setMinimumHeight(60)
            self.load_existing_data_label5.setMaximumHeight(60)
            self.load_existing_data_label5.setMinimumWidth(1)
            self.load_existing_data_label5.setMaximumWidth(300)
            self.ui.load_pages.search_exist_data_label1_layout.addWidget(self.load_existing_data_label5)

            self.load_existing_data_lineedit1 = PyLineEdit(
                text="",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_data_lineedit1.setMaximumWidth(400)
            self.load_existing_data_lineedit1.setMaximumHeight(80)
            self.load_existing_data_lineedit1.setMinimumWidth(150)
            self.load_existing_data_lineedit1.setMinimumHeight(80)
            self.ui.load_pages.search_exist_data_line1_layout.addWidget(self.load_existing_data_lineedit1)

            self.load_existing_data_lineedit2 = PyLineEdit(
                text="",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_data_lineedit2.setMaximumWidth(400)
            self.load_existing_data_lineedit2.setMaximumHeight(80)
            self.load_existing_data_lineedit2.setMinimumWidth(150)
            self.load_existing_data_lineedit2.setMinimumHeight(80)
            self.ui.load_pages.search_exist_data_line1_layout.addWidget(self.load_existing_data_lineedit2)

            self.load_existing_data_lineedit3 = PyLineEdit(
                text="",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_data_lineedit3.setMaximumWidth(400)
            self.load_existing_data_lineedit3.setMaximumHeight(80)
            self.load_existing_data_lineedit3.setMinimumWidth(150)
            self.load_existing_data_lineedit3.setMinimumHeight(80)
            self.ui.load_pages.search_exist_data_line1_layout.addWidget(self.load_existing_data_lineedit3)

            self.load_existing_data_lineedit4 = PyLineEdit(
                text="",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_data_lineedit4.setMaximumWidth(400)
            self.load_existing_data_lineedit4.setMaximumHeight(80)
            self.load_existing_data_lineedit4.setMinimumWidth(150)
            self.load_existing_data_lineedit4.setMinimumHeight(80)
            self.ui.load_pages.search_exist_data_line1_layout.addWidget(self.load_existing_data_lineedit4)

            self.load_existing_data_lineedit5 = PyLineEdit(
                text="",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["context_color"],
                selection_color=self.themes["app_color"]["dark_one"],
                bg_color=self.themes["app_color"]["dark_four"],
                bg_color_active=self.themes["app_color"]["dark_one"],
                context_color=self.themes["app_color"]["context_color"],
                font="19pt Comic Sans MS",
            )
            self.load_existing_data_lineedit5.setMaximumWidth(400)
            self.load_existing_data_lineedit5.setMaximumHeight(80)
            self.load_existing_data_lineedit5.setMinimumWidth(150)
            self.load_existing_data_lineedit5.setMinimumHeight(80)
            self.ui.load_pages.search_exist_data_line1_layout.addWidget(self.load_existing_data_lineedit5)

            self.load_existing_data_button3 = PyPushButton(
                text="Visszalépés (módosítás nélkül)",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_existing_data_button3.setMinimumHeight(100)
            self.load_existing_data_button3.setMinimumWidth(250)
            self.ui.load_pages.search_exist_data_buttons_layout.addWidget(self.load_existing_data_button3)
            self.load_existing_data_button3.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            self.load_existing_data_button2 = PyPushButton(
                text="Új adatok rögzítése",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["dark_four"],
                font="30pt Comic Sans MS",
            )
            self.load_existing_data_button2.setMinimumHeight(100)
            self.load_existing_data_button2.setMinimumWidth(250)
            self.ui.load_pages.search_exist_data_buttons_layout.addWidget(self.load_existing_data_button2)
            self.load_existing_data_button2.clicked.connect(lambda: modifyFunctions.page_modify_save_userdata(self))
            self.load_existing_data_button2.clicked.connect(lambda: modifyFunctions.search_destroyer(self))

            c.execute(f"""SELECT Irányítószám, Cím,'E-mail cím',Telefonszám,'Milye nincs' FROM {searched_client_tabeled}""")
            old_datas = c.fetchone()


            self.load_existing_data_lineedit2.setText(old_datas[0])
            self.load_existing_data_lineedit1.setText(old_datas[1])
            self.load_existing_data_lineedit3.setText(old_datas[2])
            self.load_existing_data_lineedit4.setText(old_datas[3])
            self.load_existing_data_lineedit5.setText(old_datas[4])
            c.close()
            conn.close()

        else:
            modifyFunctions.search_destroyer(self)
            self.load_existing_data_wrongname_label = PyLabel(
                text="Rossz nevet írtál be, a keresett ügyfél nincs az adatbázisban",
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_two"],
                selection_color=self.themes["app_color"]["bg_two"],
                context_color=self.themes["app_color"]["dark_four"],
                font="25pt Comic Sans MS", )

            self.load_existing_data_wrongname_label.setMinimumHeight(200)
            self.load_existing_data_wrongname_label.setMaximumHeight(300)
            self.load_existing_data_wrongname_label.setMinimumWidth(300)
            self.load_existing_data_wrongname_label.setMaximumWidth(500)
            self.ui.load_pages.search_exist_data_buttons_layout.addWidget(self.load_existing_data_wrongname_label,alignment=Qt.AlignCenter)
            c.close()
            conn.close()

    def page_modify_save_userdata(self):

        current_client_raw = self.load_existing_data_cilent_lineedit.text()
        current_client = "tbl_" + str(current_client_raw.replace(' ', '_'))

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()

        irsza = self.load_existing_data_lineedit2.text()
        adress = self.load_existing_data_lineedit1.text()
        phone = self.load_existing_data_lineedit4.text()
        email = self.load_existing_data_lineedit3.text()
        whatno = self.load_existing_data_lineedit5.text()

        c.execute(f"""UPDATE {current_client} SET  Irányítószám = ?, Cím = ?, 'E-mail cím' = ?, Telefonszám =  ?, 'Milye nincs' = ? """,
                  [str(irsza),str(adress),str(email),str(phone),str(whatno)])
        conn.commit()
        c.close()
        conn.close()

    def page_modify_insert_event(self):
        current_client_raw = self.load_existing_event_cilent_lineedit.text()
        current_client = "tbl_" + str(current_client_raw.replace(' ', '_'))

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()

        event_date = self.load_existing_event_lineedit4.text()
        ins_number = self.load_existing_event_lineedit1.text()
        ins_mode = self.load_existing_event_lineedit2.text()
        sz_or_t = self.load_existing_event_lineedit3.text()
        date = self.load_existing_event_lineedit10.text()
        yearly_price = self.load_existing_event_lineedit5.text()
        mymoney = self.load_existing_event_lineedit6.text()
        pay_tempo = self.load_existing_event_lineedit7.text()
        sidenote = self.load_existing_event_textbrowser.toPlainText()

        index = self.load_existing_event_lineedit8.text()
        turn_date = self.load_existing_event_lineedit9.text()
        allomany = self.load_existing_event_lineedit11.text()


        sqlite_insert_with_param = f"INSERT INTO {current_client} (Sorszám, 'Esemény dátuma', 'Szerzés vagy Törlés', Módozat, Kötvényszám,'Kötés dátuma', 'Éves díj', Jutalék, Évforduló, 'Díjfizetés üteme',Megjegyzés, Állomány) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        data_tuple = (index,event_date,sz_or_t, ins_mode, ins_number,date,yearly_price,mymoney,turn_date,pay_tempo,sidenote,allomany)
        c.execute(sqlite_insert_with_param,data_tuple)
        conn.commit()
        c.close()
        conn.close()

    def page_modify_insert_client(self):
        new_client_name = self.load_newclient_lineedit.text()
        new_client_tablename = "tbl_" + str(new_client_name.replace(' ', '_'))

        conn = sqlite3.connect(r'db/ugyfelek.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS" + " " + str(new_client_tablename) + " ("
          "'Index' INTEGER, Dátum TEXT, Módozat TEXT, Kötvényszám TEXT, 'Szerzés vagy Törlés' TEXT, Évforduló TEXT,"
        "'Éves díj' TEXT, Jutalék TEXT, 'Díjfizetés üteme' TEXT, Irányítószám TEXT, Cím TEXT, 'E-mail cím' TEXT, Megjegyzés TEXT)")

        date = self.load_newclient_lineedit11.text()
        ins_number = self.load_newclient_lineedit1.text()
        ins_mode = self.load_newclient_lineedit2.text()
        sz_or_t = self.load_newclient_lineedit3.text()
        sz_date = self.load_newclient_lineedit4.text()
        yearly_price = self.load_newclient_lineedit5.text()
        mymoney = self.load_newclient_lineedit6.text()
        pay_tempo = self.load_newclient_lineedit7.text()
        sidenote = self.load_newclient_textbrowser.toPlainText()

        adress = self.load_newclient_lineedit15.text()
        email = self.load_newclient_lineedit17.text()
        irsza = self.load_newclient_lineedit16.text()

        sqlite_insert_with_param = f"""INSERT INTO {new_client_tablename} (Dátum, Kötvényszám, Módozat, 'Szerzés vagy Törlés', 
                Évforduló,'Éves díj',Jutalék,'Díjfizetés üteme', Megjegyzés, Cím, Irányítószám, "E-mail cím") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?);"""

        data_tuple = (date, ins_number, ins_mode, sz_or_t, sz_date, yearly_price, mymoney, pay_tempo, sidenote,adress,irsza,email)
        c.execute(sqlite_insert_with_param, data_tuple)

        conn.commit()
        print("új ügyfél mentve")
        c.close()
        conn.close()



