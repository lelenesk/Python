
style = '''

QComboBox {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    radius: 8;
	border-radius: {_radius};
	font:  {_font};
    color: {_color};
    background color: {_bg_color};
    scroll_bar_btn_color: {_context_color};
    
    selection-color: {_selection_color};
    selection-background-color: "#333645";		
}}
QComboBox:hover {{
	background-color: {_bg_color_hover};
    color: {_color};
    
    selection-color: {_selection_color};
    selection-background-color: "#333645";	
}}
QComboBox:pressed {{	
	background-color: {_bg_color};
	color: {_color};
    
    selection-color: {_selection_color};
    selection-background-color: "#333645";	
}}
QComboBox QAbstractItemView {{
    background-color: {_bg_color};
    color: {_color};
    
    selection-color: {_selection_color};
    selection-background-color: "#333645";
}}


QComboBox QAbstractItemView:Item {{
    background-color: {_bg_color_selection};
    color: "#282a36";
    
    selection-color: {_color};
    selection-background-color: {_color};	
}}
QComboBox QAbstractItemView:active {{
    background-color: {_bg_color_selection};
    color: {_color};
    
    selection-color: {_bg_color};
    selection-background-color: "#333645";
}} 

   
QComboBox:item:selected {{
    background-color: {_bg_color};
    color: {_color};
    
    selection-color: {_selection_color};
    selection-background-color: "#333645";
}}
QComboBox:editable {{
    background: {_bg_color};
}}
QComboBox:!editable, QComboBox::drop-down:editable {{
     background: {_bg_color};
}}


QScrollBar:horizontal {{
    color: {_context_color};
    border: 2px;
    background: {_scroll_bar_bg_color};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    color: {_context_color};
    background: {_context_color};
    min-width: 35px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    color: {_context_color};
    border: none;
    background: {_scroll_bar_btn_color};
    width: 25px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    color: {_context_color};
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     color: {_context_color};
     background: {_selection_color};
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     color: {_context_color};
     background: {_selection_color};
}}
QScrollBar:vertical {{
	color: {_context_color};
	border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	color: {_context_color};
	background: {_context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     color: {_context_color};
     border: none;
     background: {_scroll_bar_btn_color};
     height: 20px;
	 border-bottom-left-radius: 4px;
     border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	color: {_context_color};
	border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     color: {_context_color};
     background: {_selection_color};
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     color: {_context_color};
     background: {_selection_color};
}} '''