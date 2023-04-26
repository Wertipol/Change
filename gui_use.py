from tkinter import *

win = Tk()
win.title('Сдача')
win.geometry('800x600')
win.resizable(True, False)

coins = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

def fun():
    changeCoins = []
    user = int(userMoney.get())
    product = int(productsMoney.get())
    value =  product - user #хз почему так
    txt3.configure(text= f'Ваша сдача должна быть: {value}')

    while value > 0:
        for i in range(len(coins)):
            while value >= coins[i]:
                value -= coins[i]
                changeCoins.append(coins[i])

    txt4.configure(text= f'По наличным это: {changeCoins}')

def null():
    userMoney.delete(0, END)
    productsMoney.delete(0, END)
    txt3.configure(text='Ваша сдача должна быть:')
    txt4.configure(text='По наличным это:')

txt1 = Label(win, text='Сумма всех продуктов:', font='Calibri 20')
txt1.place(x=40, y=50)

txt2 = Label(win, text='Сколько вы отдали денег:', font='Calibri 20')
txt2.place(x=10, y=150)

userMoney = Entry(win, font='Calibri 30')
userMoney.place(x=330, y=50)

productsMoney = Entry(win, font='Calibri 30')
productsMoney.place(x=330, y=150)

btn = Button(win, text='Расчитать', font='Calibri 20', command=fun)
btn.place(x=400, y=230)

btn1 = Button(win, text='Сброс', font='Calibri 20', command=null)
btn1.place(x=550, y=230)

txt3 = Label(win, text='Ваша сдача должна быть:', font='Calibri 20')
txt3.place(x=40, y=350)

txt4 = Label(win, text='По наличным это:', font='Calibri 20')
txt4.place(x=40, y=400)

win.mainloop()
