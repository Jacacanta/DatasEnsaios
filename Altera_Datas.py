# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:30:15 2021

@author: josecorreia
\\servidor\ngeosys1\Aplic\Dbfs
"""

import tkinter as tk   
from dbfread import DBF
amostras = DBF('C:\\Users\\josecorreia\\Desktop\\MyDocs\\OBRAS\\DBASE\\DBFS\\amostras.dbf', encoding='latin1')
registos = DBF('C:\\Users\\josecorreia\\Desktop\\MyDocs\\OBRAS\\DBASE\\DBFS\\registo.dbf', encoding='latin1')

lista=[]
lista_Am=[]
lista_Reg=[]
dic={1:'Resultados',2:'PEN',3:'EA',4:'W',5:'LCA',6:'CBR',7:'C_DIR_CU',8:'C_DIR_CD',9:'C_DIR_UU',10:'PRO+M',11:'PRO+N',
     12:'PERM_CC',13:'PERM_CV',14:'G',15:'EDOM',16:'AZMET',17:'TEOR_MO',18:'COMP_SIMP',19:'SED',20:'A_GRAN',
     21:'ABS_AGUA',22:'LOS_A_BRIT',23:'GAMA',24:'ST',25:'COMP_MARSH',26:'DENS_APAR',27:'T_BET',28:'T_AGUA'}
i=1

def seleciona():
    lista_Am=[]
    for record in amostras:
        lista=[list(record.values())[::]]
        if (lista[0])[3]== txt.get():
            lst.insert (i+1, (lista[0])[0])
            lista_Am.append((lista[0])[0])
            #print((lista[0])[0],(lista[0])[2])
    print(lista_Am)
i+=1

app = tk.Tk()
app.title("Registos de Datas")
app.geometry('400x200')

def openNewWindow(arg):
    newWindow = tk.Toplevel(app)
    newWindow.title(lst.get(0))
    newWindow.geometry("600x200")
    tk.Label(newWindow, text ="Registos da amostra").pack()
    lst.delete(0)
    btn = tk.Button(newWindow, text='Selecionar Registos', command=registosAm)
    btn.place(x=30,y=90)
    ls=tk.Listbox(newWindow, width=40).pack()
    ls=tk.Listbox(newWindow,  fill=tk.Y)
    ls.tk.insert(i+1, (lista[0])[0])
    
lbl = tk.Label(app, text='Insira o Processo 17221')
lbl.place(x=10, y=10)

txt = tk.Entry(app)
txt.place(x=10,y=30)

btn = tk.Button(app, text='Selecionar Amostras', command=seleciona)
btn.place(x=10,y=90)


lst = tk.Listbox(app, width=17)
lst.bind('<Double-1>', openNewWindow)
lst.pack(side=tk.RIGHT, fill=tk.Y)

def registosAm():
    for record in registos:
        lista_Reg=[list(record.values())[::]]    
        if (lista_Reg[0])[0]==66350:       #(lst.get(0)):
            print((lista_Reg[0])[0:9])
            dia=(lista_Reg[0])[6]
            mes=(lista_Reg[0])[5]
            ano=(lista_Reg[0])[4]
            print(lista_Reg)
            print("Data: ",dia,"-",mes,"-",ano)

            #tk.Listbox.insert(i+1, (lista_Reg[0])[1])
            
            
            
            
#print(record)
#print(lista[0])
#print(lista_Reg[0])
#print((lista_Reg[0])[8])
  
app.mainloop()    
    



   
    

