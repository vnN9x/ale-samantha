import json
from tkinter import *

BTN01_CLICKED = False
BTN02_CLICKED = False
BTN03_CLICKED = False
BTN04_CLICKED = False

def main():
    with open('Model/json_text.json', encoding='utf-8') as f:
        global BTN01_CLICKED, BTN02_CLICKED, BTN03_CLICKED, BTN04_CLICKED
        json_data =json.load(f)

        #root window
        window = Tk()
        window.geometry('600x400')
        window.title(json_data['titulo'])
        window.config(bg= "white")

        #first_frame window
        first_frame = Frame(window)
        first_frame.pack()

        #buttons_frame window
        buttons_frame = Frame(window)

        def change_to_buttons():
            buttons_frame.pack()
            button01_frame.forget()
            button02_frame.forget()
            button03_frame.forget()
            button04_frame.forget()
            first_frame.forget()

        #first_frame widgets
        first_frame.config(bg= "white")
        label = Label(first_frame, text=json_data['texto-pagina01'], wraplength=600, bg ='white')
        label.pack()
        botao_continue = Button(first_frame, activebackground='blue', bg='white', justify='center', text= json_data['botao-continue'],
        command=change_to_buttons)
        botao_continue.pack()

        #button_panels
        button01_frame = Frame(window)
        label = Label(button01_frame, text=json_data['dentro-botao01'], wraplength=600, bg ='white')
        label.pack()
        botao_continue = Button(button01_frame, activebackground='blue', bg='white', justify='center', text= json_data['botao-continue'],
        command=change_to_buttons)
        button01_frame.config(bg= "white")
        botao_continue.pack()

        button02_frame = Frame(window)
        label = Label(button02_frame, text=json_data['dentro-botao02'], wraplength=600, bg ='white')
        label.pack()
        button02_frame.config(bg= "white")
        botao_continue = Button(button02_frame, activebackground='blue', bg='white', justify='center', text= json_data['botao-continue'],
        command=change_to_buttons)
        botao_continue.pack()

        button03_frame = Frame(window)
        button03_frame.config(bg= "white")
        label = Label(button03_frame, text=json_data['dentro-botao03'], wraplength=600, bg ='white')
        label.pack()
        botao_continue = Button(button03_frame, activebackground='blue', bg='white', justify='center', text= json_data['botao-continue'],
        command=change_to_buttons)
        botao_continue.pack()

        button04_frame = Frame(window)
        button04_frame.config(bg= "white")
        label = Label(button04_frame, text=json_data['dentro-botao04'], wraplength=600, bg ='white')
        label.pack()
        botao_continue = Button(button04_frame, activebackground='blue', bg='white', justify='center', text= json_data['botao-continue'],
        command=change_to_buttons)
        botao_continue.pack()

        label = Label(buttons_frame, text='                        ', bg ='white')
        label.grid(row=0, column=1)
        label = Label(buttons_frame, text='                        ', bg ='white')
        label.grid(row=1, column=1)


        def button01():
            global BTN01_CLICKED
            BTN01_CLICKED = True
            botao01.configure(bg='#00FA9A')
            button01_frame.pack()
            surprise_button()
            buttons_frame.forget()

        def button02():
            global BTN02_CLICKED
            BTN02_CLICKED = True
            botao02.configure(bg='#00FA9A')
            button02_frame.pack()
            surprise_button()
            buttons_frame.forget()
        
        def button03():
            global BTN03_CLICKED
            BTN03_CLICKED = True
            botao03.configure(bg='#00FA9A')
            button03_frame.pack()
            surprise_button()
            buttons_frame.forget()
        
        def button04():
            global BTN04_CLICKED
            BTN04_CLICKED = True
            botao04.configure(bg='#00FA9A')
            button04_frame.pack()
            surprise_button()
            buttons_frame.forget()

        #buttons_frame widgets
        buttons_frame.config(bg= "white")
        botao01 = Button(buttons_frame, activebackground='#00FA9A', bg='white', justify='center', text= json_data['texto-botao01'],
        command=button01)
        botao02 = Button(buttons_frame, activebackground='#00FA9A', bg='white', justify='center', text= json_data['texto-botao02'],
        command=button02)
        botao03 = Button(buttons_frame, activebackground='#00FA9A', bg='white', justify='center', text= json_data['texto-botao03'],
        command=button03)
        botao04 = Button(buttons_frame, activebackground='#00FA9A', bg='white', justify='center', text= json_data['texto-botao04'],
        command=button04)

        botao01.grid(row=0, column=0)
        botao02.grid(row=0, column=2)
        botao03.grid(row=1, column=0)
        botao04.grid(row=1, column=2)

        def surprise_button():
            if BTN01_CLICKED and BTN02_CLICKED and BTN03_CLICKED and BTN04_CLICKED:
                botao05 = Button(buttons_frame, activebackground='#00FA9A', bg='white', justify='center', text= json_data['texto-botao05'],
            command=button01)
                botao05.grid(row=2, column=1)
            
        window.mainloop()

if __name__ == '__main__':
    main()
