from tkinter import *
from tkinter import messagebox

	# окно программы
root = Tk()

root.resizable (width = False, height = False)
root.geometry ('300x250')
root.title ('LogIn system')
root.wm_attributes('-alpha', 0.94)
root['bg'] = '#ccc'
root.iconbitmap('F:/New folder/python/tkinter/icon.ico')

#функции
def check (event):
	L = login.get()
	P = password.get()

	if L and P:
		messagebox.showinfo('Success', 'Доступ разрешен')
	if not L and P:
		messagebox.showerror('LoginError', 'Отказано в доступе. Введите логин')
	elif not P and L:
		messagebox.showerror('PassError', 'Отказано в доступе. Введите пароль')
	if not L and not P:
		messagebox.showerror('AccessError', 'Отказано в доступе. Введите данные')

	#события в окне
#LOGIN
text_login = Label ( text = 'Login', font = 'ComicSans 20',
	fg = '#666666',
	bg = '#ccc' )
login = Entry (root, font = 'Consolas 14',
	fg = '#fbffe3',
	bg = '#3c3d42',
	relief = 'solid',
	justify = 'center')

#PASSWORD
text_password = Label ( text = 'Password', font = 'ComicSans 20',
	fg = '#666666',
	bg = '#ccc' )
password = Entry (root, font = 'Consolas 14',
	fg = '#fbffe3',
	bg = '#3c3d42',
	relief = 'solid',
	justify = 'center',
	show = '*' )

#status
check_status = Checkbutton (text = 'Не выходить из системы', font = 'ComicSans 13',
	bg = '#ccc',
	fg = '#666666',
	activebackground = '#ccc',
	activeforeground = '#666666',
	)

enter = Button (text = 'Войти', font = 'Consolas 13',
	fg = '#fbffe3',
	bg = '#3c3d42',
	activebackground = '#eff5c9',
	activeforeground = '#6e6f73',
	width = '30')


	#элементы окна, которые будут отображаться в программе
text_login.pack()
login.pack()
text_password.pack()
password.pack()
check_status.pack()
enter.pack()

#всплывающие окна
enter.bind( '<Button-1>', check )

#запуск
root.mainloop()