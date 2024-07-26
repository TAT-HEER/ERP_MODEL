
import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect('client_reg.db')

c = conn.cursor()
# c.execute("""CREATE TABLE journal_entries (
#     id integer,
#     entry_date text,
#     particulars_dr TEXT,
#     amount_dr integer,
#     particulars_cr TEXT,
#     amount_cr integer

# )""")

conn.commit()
conn.close()

sg.theme('Dark Blue 3')
sg.set_options(font=('Courier 15'),text_color='black')

layout = [
    [sg.T("Journal General Entries ")],
    [sg.T("ID"),sg.Push(), sg.I(size=(30,3),key='id')],
    [sg.CalendarButton(button_text="Date",format='%d-%m-%y',no_titlebar=True,close_when_date_chosen=True,target='date', default_date_m_d_y=(1,6,1980)), sg.Push(), sg.I(size=(30, 3), key='date')],
    [sg.T("Particulars(dr)"), sg.Push(), sg.ML(size=(30, 3), key='partd')],
    [sg.T("Debit Amount"), sg.Push(), sg.I(size=(30, 3), key='amntd')],
    # [sg.T("Debit Amount"), sg.Push(), sg.Combo(size=(30, 3), values=('Debit', 'Credit'), key='amntd')],
    [sg.T("Particulars(cr)"), sg.Push(), sg.ML(size=(30, 3), key='partc')],
    # [sg.T("Credit Amount"), sg.Push(), sg.Combo(size=(30, 3), values=('Debit', 'Credit'), key='amntc')],
    [sg.T("Credit Amount"), sg.Push(), sg.I(size=(30, 3), key='amntc')],
    [sg.Button('Submit',expand_x=True),sg.Button('Clear',expand_x=True),sg.Button('Show Records',expand_x=True),sg.Button('Exit',expand_x=True)]

]

window = sg.Window("Database App", layout)

def retrieve_clients_records():
    results = []
    conn = sqlite3.connect('client_reg.db')
    c = conn.cursor()
    query = "SELECT id,entry_date, particulars_dr, amount_dr, particulars_cr, amount_cr from journal_entries"
    c.execute(query)
    for row in c:
        results.append(list(row))
    return results  


def get_client_records():
    clients_records =  retrieve_clients_records()
    return clients_records 


def create_records():
    client_records_array = get_client_records()
    headings = ['ID','Entry_date', 'Particulars_dr', 'Amount_dr', 'Particulars_cr', 'Amount_cr' ]
    layout_for_display = [

        [sg.Table(values=client_records_array, headings = headings, max_col_width=35, auto_size_columns=True,
                  display_row_numbers=True, justification='left',num_rows=10,key= 'CLIENTABLE',row_height=60, enable_events=True,
                  tooltip='all clients results'
                  )]
    ]
    windr = sg.Window('Summary Results: ', layout_for_display, modal = True)
    while True:
        events , values  = windr.read()
        if events ==sg.WIN_CLOSED:
            break




def clear_inputs():
    for key in values:
        window['id'].update('')
        window['date'].update('')
        window['partd'].update('')
        window['amntd'].update('')
        window['partc'].update('')
        window['amntc'].update('')

    return None

def save_data_to_database():
    conn = sqlite3.connect('client_reg.db')
    c = conn.cursor()
    c.execute("INSERT INTO journal_entries VALUES (:id, :entry_date, :particulars_dr, :amount_dr, :particulars_cr, :amount_cr)",
        {'id': values['id'] ,
        'entry_date': values['date'],
        'particulars_dr': values['partd'] ,
        'amount_dr' : values['amntd'],
        'particulars_cr': values['partc'] ,
        'amount_cr' : values['amntc']
        })
        

    conn.commit()
    conn.close()

    

while True:
    events, values = window.read()
    if events in (sg.WIN_CLOSED, 'Exit'):
        break
    if events == 'Show Records':
        create_records()
    if events == 'Clear':
        clear_inputs()
    if events == 'Submit':
        ID = values['id']
        if ID == '':
            sg.PopupError('Missing id no, Please enter to continue')

        date = values['date']
        if date == '':
            sg.PopupError('Missing Date, Please enter to continue')

        particular_d = values['partd']
        if particular_d == '':
            sg.PopupError('Please entry your particulars to continue')

        amount_d = values['amntd']
        if amount_d == '':
            sg.PopupError('Please pick one entry to continue')

        particular_c = values['partc']
        if particular_c == '':
            sg.PopupError('Please entry your particulars to continue')

        amount_c = values['amntc']
        if amount_c == '':
            sg.PopupError('Please pick one entry to continue')
        else:
            try:
                summary_list = "the following information has been saved to the database: "
                nid = "\nI'd: " + values['id']
                summary_list += nid

                ndate = "\nDate: " + values['date']
                summary_list += ndate

                dpart = "\nParticulars(dr): " + values['partd']
                summary_list += dpart
                dval = "\nValue(dr): "+ values['amntd']
                summary_list += dval

                cpart = "\nParticulars(cr): " + values['partc']
                summary_list += cpart
                cval = "\nValue(cr): " + values['amntc']
                summary_list += cval


                choice = sg.PopupOKCancel(summary_list, 'Please Confirm Entry ')
                if choice == 'OK':
                    clear_inputs()
                    save_data_to_database()
                    sg.PopupQuick("saved to database ")
                else:
                    sg.PopupOK('Edit entry')
            except Exception as e:
                sg.Popup('Some error occurred:', e)


