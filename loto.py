from tkinter import *
import random

root= Tk()
root.geometry("600x200")
root.title('Generate Your Lucky Number')
root.resizable(width=False, height=False)
root.configure(background='green')


class Loto_btn:

    def __init__(self,a,b,c,d,max_range,numbers,txt):
        # a=x of buton_start
        # b=y of buton_start
        # c=x of lucky_nr
        # d=y of lucky_nr
        # numbers = how many numbers we want to extract
        # txt = the text that will appear on the button
        self.txt=txt
        self.buton_start = Button(root, text=self.txt, font=('arial', 14, 'bold'), command=lambda :self.extragere(max_range,numbers),bg='green')
        self.buton_start.place(x=a, y=b)
        self.lucky_nr = Label(root, text='The lucky numbers', font=('arial', 18, 'bold'),background='green')
        self.lucky_nr.place(x=c, y=d)
        self.joker_nr = Label(root,text='*', font=('arial', 19, 'bold'), foreground='green',
                              background='black',fg='green',bg='green')
        self.joker_nr.place(x=430, y=130)

    def extragere(self,max_range,numbers):
        nr_num = []
        numbers_extract = random.sample(range(1, max_range+1), numbers)
        for i in numbers_extract:
                nr_num.append(i)
                nr_num.append('*')
        self.lucky_nr.config(text=nr_num[:-1])
        if self.txt== 'Joker':
            txt_jkr = random.sample(range(1, 20), 1)

            self.joker_nr.config(text=f'* {txt_jkr[0]}',foreground='green',
                              background='green',fg='white',bg='green')

Loto_btn(20,20,200,20,49,6,'Loto 6 / 49')
Loto_btn(20,75,200,75,40,5,'Loto 5 / 40')
Loto_btn(20,130,200,130,45,5,'Joker')

root.mainloop()