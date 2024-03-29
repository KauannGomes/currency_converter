from tkinter import Tk,ttk #type:ignore
from tkinter import * #type:ignore
#----------------------------------------------------------
#root

root = Tk()
root.title('Conversor')
root.geometry('300x300')
root.resizable(False,False)
ICON = 'img/icon.ico'
root.iconbitmap('img/icon.ico')
root['bg'] = '#EDEDED'

frame = Frame(root,pady=25,bg='#2D728F')
frame_bottom = Frame(root,bg='#EDEDED',pady=20)
value_ = IntVar()
from_options = StringVar()
to_options = StringVar()

from_converter_options = ['USD','BRL']
to_converter_options = ['USD','BRL']

#----------------------------------------------------------
#func

def converter():
    try:
        from_value = from_converter.get()
        to_value = to_converter.get()
        money_value = int(box_entry_value.get())

        if from_value == 'BRL' and to_value == 'USD':
            result = f'${round(money_value * 0.2,3)}'
            box_value['text'] = result
            
        if from_value == 'USD' and to_value == 'BRL':
            result = f'R${round(money_value * 5.01,3)}'
            box_value['text'] = result

    except ValueError:
      box_value['text'] = 'Campos inválidos' 

    except Exception as e:
        print(f'erro: {e}')
    
#----------------------------------------------------------
#creating widgets

text_title = Label(frame, text='Conversor de moeda',fg='#FFFFFF',pady=3,bg='#2D728F',font=('Arial',10))
box_value = Label(frame,text='0',bd=1,relief=SOLID,width=30,height=3,bg = '#2D728F',fg='#FFFFFF',font=('Arial',10))

from_text = Label(frame_bottom,text='De', fg='#000000',bg = '#EDEDED')
from_converter = ttk.Combobox(frame_bottom,textvariable=from_options,values=from_converter_options,state='readonly',)


to_text = Label(frame_bottom,text='Para',fg='#000000',bg = '#EDEDED')
to_converter = ttk.Combobox(frame_bottom,textvariable=to_options,values= to_converter_options,state='readonly',)

box_entry_value = Entry(frame_bottom,bd=1,relief=SOLID,)
box_entry_value.focus()

btn_converter = Button(frame_bottom,text='Converter',command=converter, bd=0,relief=SOLID,bg='#2D728F',fg='#FFFFFF',font=('Arial',12))

#----------------------------------------------------------
#placing widgets on the screen

frame.grid()
frame_bottom.grid()

text_title.grid(row=0,column=0,columnspan=2,padx=90)
box_value.grid(row=1,column=0,columnspan=2)

from_text.grid(row=1,column=0,sticky=W)
from_converter.grid(row=2,column=0,pady=0)

to_text.grid(row=1,column=1,sticky=W)
to_converter.grid(row=2,column=1,pady=0)

box_entry_value.grid(row=3,column=0,columnspan=2,pady=30,)

btn_converter.grid(row=4,column=0,columnspan=2)

#----------------------------------------------------------
#Final

root.mainloop()

