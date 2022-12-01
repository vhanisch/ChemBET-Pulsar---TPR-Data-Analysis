# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:56:55 2020

@author: vhanisch
"""

import tkinter as tk
import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



def fgraficos():
    Temperatura = entry_temp.get()
    Nome1 = entry1.get()
    Nome2 = entry2.get()
    Nome3 = entry3.get()
    Nome4 = entry4.get()
    Nome5 = entry5.get()
    Nome6 = entry6.get()
    espacamento1 = int(entry_Espacamento1.get())
    espacamento2 = int(entry_Espacamento2.get())
    espacamento3 = int(entry_Espacamento3.get())
    espacamento4 = int(entry_Espacamento4.get())
    espacamento5 = int(entry_Espacamento5.get())

    if (entry_fonte_graf.get() == "0"):
        fonte = "Arial"
    else:
        fonte = entry_fonte_graf.get()
    
    ### Dados ###

    Temperatura = int(Temperatura)
    Temp = Temperatura+1
    Titulo = entry_title_graf.get()

    
    ## 1 Dado ##
    if (Nome2 == "0" and (Nome3== "0") and (Nome4== "0") and (Nome5== "0") and (Nome6== "0")) :
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        
        data_del = np.delete(data, 0, 1)
        data_del2 = np.delete(data_del, 2, 1)
        
        Matriz= data_del2.astype(np.float64)
        Matriz2 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz2[i,0] = i
        
        def find_nearest(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz2[i,1] = Matriz[smallest_difference_index,1]
        
        
        
        
        ### Plotando Gráfico ###
        
        plt.plot(Matriz2[:,0],Matriz2[:,1],linewidth=0.9)
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Signal (mV)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi = 500)
        plt.xticks(fontname = fonte)
        plt.yticks([])
        plt.show(block=True)

           
    ## 2 Dados ##
    if ((Nome3== "0") and (Nome4== "0" and (Nome5== "0") and (Nome6== "0")) and ((Nome1!= "0") and (Nome2 != "0"))):
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        data2 = np.loadtxt(Nome2, delimiter=":", dtype='str')
        
        data_del11 = np.delete(data, 0, 1)
        data_del12 = np.delete(data_del11, 2, 1)
        
        data_del21 = np.delete(data2, 0, 1)
        data_del22 = np.delete(data_del21, 2, 1)  
        
        Matriz11= data_del12.astype(np.float64)
        Matriz12 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz12[i,0] = i
            
        Matriz21= data_del22.astype(np.float64)
        Matriz22 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz22[i,0] = i
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz11[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz12[i,1] = Matriz11[smallest_difference_index,1]
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz21[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz22[i,1] = Matriz21[smallest_difference_index,1] + espacamento1
        
        
        
        ### Plotando Gráfico ###
        
        plt.plot(Matriz12[:,0],Matriz12[:,1], 'b-', label = entry_legenda1.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz22[:,1], 'r-', label = entry_legenda2.get(),linewidth=0.9)
        plt.legend(loc="best", prop={'family':fonte, 'size': 12},framealpha=1, frameon=True);
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Hydrogen Consumption (a.u.)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi=1000)
        plt.yticks([], fontname = fonte)
        plt.xticks(fontname = fonte)
        plt.show(block=True)


    
    ## 3 Dados ##    
    if (((Nome4== "0") and (Nome5== "0") and (Nome6== "0")) and ((Nome1!= "0") and (Nome2 != "0")and (Nome3 !="0"))):
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        data2 = np.loadtxt(Nome2, delimiter=":", dtype='str')
        data3 = np.loadtxt(Nome3, delimiter=":", dtype='str')
        
        data_del11 = np.delete(data, 0, 1)
        data_del12 = np.delete(data_del11, 2, 1)
        
        data_del21 = np.delete(data2, 0, 1)
        data_del22 = np.delete(data_del21, 2, 1)  
        
        data_del31 = np.delete(data3, 0, 1)
        data_del32 = np.delete(data_del31, 2, 1)
        
        Matriz11= data_del12.astype(np.float64)
        Matriz12 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz12[i,0] = i
            
        Matriz21= data_del22.astype(np.float64)
        Matriz22 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz22[i,0] = i
            
        Matriz31= data_del32.astype(np.float64)
        Matriz32 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz32[i,0] = i
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz11[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz12[i,1] = Matriz11[smallest_difference_index,1]
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz21[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz22[i,1] = Matriz21[smallest_difference_index,1] + espacamento1
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz31[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz32[i,1] = Matriz31[smallest_difference_index,1] + espacamento1 + espacamento2
        
        
        ### Plotando Gráfico ###
        
        plt.plot(Matriz12[:,0],Matriz12[:,1], 'b-', label = entry_legenda1.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz22[:,1], 'r-', label = entry_legenda2.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz32[:,1], 'g-',label = entry_legenda3.get(),linewidth=0.9)
        plt.legend(loc="best", prop={'family':fonte, 'size': 7},framealpha=1, frameon=True);
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Hydrogen Consumption (a.u.)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi=1000)
        plt.yticks([], fontname = fonte)
        plt.xticks(fontname = fonte)
        plt.show(block=True)


    ## 4 Dados ## 
    if (((Nome5 == "0") and (Nome6== "0")) and ((Nome1!= "0") and (Nome2 != "0")and (Nome3 !="0") and (Nome4 != "0"))):
        print("abriu o if")
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        data2 = np.loadtxt(Nome2, delimiter=":", dtype='str')
        data3 = np.loadtxt(Nome3, delimiter=":", dtype='str')
        data4 = np.loadtxt(Nome4, delimiter=":", dtype='str')
        
        data_del11 = np.delete(data, 0, 1)
        data_del12 = np.delete(data_del11, 2, 1)
        
        data_del21 = np.delete(data2, 0, 1)
        data_del22 = np.delete(data_del21, 2, 1)  
            
        data_del31 = np.delete(data3, 0, 1)
        data_del32 = np.delete(data_del31, 2, 1)

        data_del41 = np.delete(data4, 0, 1)
        data_del42 = np.delete(data_del41, 2, 1)
            
        Matriz11= data_del12.astype(np.float64)
        Matriz12 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz12[i,0] = i
                
        Matriz21= data_del22.astype(np.float64)
        Matriz22 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz22[i,0] = i
                
        Matriz31= data_del32.astype(np.float64)
        Matriz32 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz32[i,0] = i
            
        Matriz41= data_del42.astype(np.float64)
        Matriz42 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz42[i,0] = i
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz11[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz12[i,1] = Matriz11[smallest_difference_index,1]
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz21[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz22[i,1] = Matriz21[smallest_difference_index,1] + espacamento1
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz31[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz32[i,1] = Matriz31[smallest_difference_index,1] + espacamento1 + espacamento2
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz41[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz42[i,1] = Matriz41[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3

        ### Plotando Gráfico ###
        plt.plot(Matriz12[:,0],Matriz12[:,1], 'b-', label = entry_legenda1.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz22[:,1], 'r-', label = entry_legenda2.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz32[:,1], 'g-',label = entry_legenda3.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz42[:,1], 'y-',label = entry_legenda4.get(),linewidth=0.9)
        plt.legend(loc="best", prop={'family':fonte, 'size': 7},framealpha=1, frameon=True);
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Hydrogen Consumption (a.u.)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi=1000)
        plt.yticks([], fontname = fonte)
        plt.xticks(fontname = fonte)
        plt.show(block=True)

            
            
            
            
        ## 5 Dados ## 
    if ((Nome6== "0") and (Nome1!= "0") and (Nome2 != "0") and (Nome3 !="0")and (Nome4 !="0") and (Nome5 !="0")):
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        data2 = np.loadtxt(Nome2, delimiter=":", dtype='str')
        data3 = np.loadtxt(Nome3, delimiter=":", dtype='str')
        data4 = np.loadtxt(Nome4, delimiter=":", dtype='str')
        data5 = np.loadtxt(Nome5, delimiter=":", dtype='str')
        
        data_del11 = np.delete(data, 0, 1)
        data_del12 = np.delete(data_del11, 2, 1)
        
        data_del21 = np.delete(data2, 0, 1)
        data_del22 = np.delete(data_del21, 2, 1)  
            
        data_del31 = np.delete(data3, 0, 1)
        data_del32 = np.delete(data_del31, 2, 1)

        data_del41 = np.delete(data4, 0, 1)
        data_del42 = np.delete(data_del41, 2, 1)
            
        data_del51 = np.delete(data5, 0, 1)
        data_del52 = np.delete(data_del51, 2, 1)
            
        Matriz11= data_del12.astype(np.float64)
        Matriz12 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz12[i,0] = i
                
        Matriz21= data_del22.astype(np.float64)
        Matriz22 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz22[i,0] = i
                
        Matriz31= data_del32.astype(np.float64)
        Matriz32 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz32[i,0] = i
            
        Matriz41= data_del42.astype(np.float64)
        Matriz42 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz42[i,0] = i
            
                    
        Matriz51= data_del52.astype(np.float64)
        Matriz52 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz52[i,0] = i
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz11[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz12[i,1] = Matriz11[smallest_difference_index,1]
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz21[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz22[i,1] = Matriz21[smallest_difference_index,1] + espacamento1
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz31[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz32[i,1] = Matriz31[smallest_difference_index,1] + espacamento1 + espacamento2
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz41[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz42[i,1] = Matriz41[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3

        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz51[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz52[i,1] = Matriz51[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3 + espacamento4

        ### Plotando Gráfico ###
        
        plt.plot(Matriz12[:,0],Matriz12[:,1], 'b-', label = entry_legenda1.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz22[:,1], 'r-', label = entry_legenda2.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz32[:,1], 'g-',label = entry_legenda3.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz42[:,1], 'y-', label = entry_legenda4.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz52[:,1], 'm-', label = entry_legenda5.get(),linewidth=0.9)
        plt.legend(loc="best", prop={'family':fonte, 'size': 7},framealpha=1, frameon=True);
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Hydrogen Consumption (a.u.)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi=1000)
        plt.yticks([], fontname = fonte)
        plt.xticks(fontname = fonte)
        plt.show(block=True)



    ## 6 Dados ## 
    if ((Nome6 != "0") and (Nome1!= "0") and (Nome2 != "0") and (Nome3 !="0")and (Nome4 !="0") and (Nome5 !="0")):
        ### Lendo e Alterando Dados ###
        data = np.loadtxt(Nome1, delimiter=":", dtype='str')
        data2 = np.loadtxt(Nome2, delimiter=":", dtype='str')
        data3 = np.loadtxt(Nome3, delimiter=":", dtype='str')
        data4 = np.loadtxt(Nome4, delimiter=":", dtype='str')
        data5 = np.loadtxt(Nome5, delimiter=":", dtype='str')
        data6 = np.loadtxt(Nome6, delimiter=":", dtype='str')
        
        data_del11 = np.delete(data, 0, 1)
        data_del12 = np.delete(data_del11, 2, 1)
        
        data_del21 = np.delete(data2, 0, 1)
        data_del22 = np.delete(data_del21, 2, 1)  
            
        data_del31 = np.delete(data3, 0, 1)
        data_del32 = np.delete(data_del31, 2, 1)

        data_del41 = np.delete(data4, 0, 1)
        data_del42 = np.delete(data_del41, 2, 1)
            
        data_del51 = np.delete(data5, 0, 1)
        data_del52 = np.delete(data_del51, 2, 1)

        data_del61 = np.delete(data6, 0, 1)
        data_del62 = np.delete(data_del61, 2, 1)
            
        Matriz11= data_del12.astype(np.float64)
        Matriz12 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz12[i,0] = i
                
        Matriz21= data_del22.astype(np.float64)
        Matriz22 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz22[i,0] = i
                
        Matriz31= data_del32.astype(np.float64)
        Matriz32 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz32[i,0] = i
            
        Matriz41= data_del42.astype(np.float64)
        Matriz42 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz42[i,0] = i
            
                    
        Matriz51= data_del52.astype(np.float64)
        Matriz52 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz52[i,0] = i

        Matriz61= data_del62.astype(np.float64)
        Matriz62 = np.zeros((Temp,2),float)
        for i in range (0,Temp):
            Matriz62[i,0] = i
        
        
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz11[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz12[i,1] = Matriz11[smallest_difference_index,1]
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz21[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz22[i,1] = Matriz21[smallest_difference_index,1] + espacamento1
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz31[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz32[i,1] = Matriz31[smallest_difference_index,1] + espacamento1 + espacamento2
            
        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz41[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz42[i,1] = Matriz41[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3

        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz51[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz52[i,1] = Matriz51[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3 + espacamento4

        for i in range(0,Temp):
            absolute_val_array = np.abs(Matriz61[:,0] - i)
            smallest_difference_index = absolute_val_array.argmin()
            Matriz62[i,1] = Matriz61[smallest_difference_index,1] + espacamento1 + espacamento2 + espacamento3 + espacamento4 + espacamento5


        ### Plotando Gráfico ###
        
        plt.plot(Matriz12[:,0],Matriz12[:,1], 'b-', label = entry_legenda1.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz22[:,1], 'r-', label = entry_legenda2.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz32[:,1], 'g-',label = entry_legenda3.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz42[:,1], 'y-', label = entry_legenda4.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz52[:,1], 'm-', label = entry_legenda5.get(),linewidth=0.9)
        plt.plot(Matriz12[:,0],Matriz62[:,1], 'k-', label = entry_legenda6.get(),linewidth=0.9)
        plt.legend(loc="best", prop={'family':fonte, 'size': 7},framealpha=1, frameon=True);
        plt.title(Titulo, fontname = fonte)
        plt.xlabel(u"Temperature ($^\circ$C)", fontname = fonte)
        plt.ylabel("Hydrogen Consumption (a.u.)", fontname = fonte)
        plt.savefig("Grafico.png", format = 'png', dpi=1000)
        plt.yticks([], fontname = fonte)
        plt.xticks(fontname = fonte)
        plt.show(block=True)
    

#%% ################# Colocando Dados no GUI ###############################

alt = 1200
lar = 800

disty = np.zeros(20)
for i in range(0,20):
    disty[i] = 0.16 + i*0.04

root = tk.Tk()

canvas = tk.Canvas(root, height=alt, width=lar, bg = '#FF6100')
canvas.pack()


title = tk.Label(root, text = "Análise de Dados - ChemBET - v1.1", bg = '#FF6100')
title.place(relx=0.5, rely=0.01, relwidth=0.75, relheight=0.05, anchor='n')
title.config(font=("Arial",25,"bold"))

sub = tk.Label(root, text = "© Laboratório de Combustão e Catálise - 2022", bg = '#FF6100')
sub.place(relx=0.5, rely=0.06, relwidth=0.75, relheight=0.03, anchor='n')
sub.config(font=("Arial",12,"italic"))

instruc = tk.Label(root, text = "Os arquivos devem conter apenas os dados, o cabeçalho e a última linha devem ser deletados \nCaso não deseje utilizar todos os arquivos, digite 0 no lugar do nome/espaçamento \n Escolha uma fonte, caso digite 0 a fonte padrão é Arial", anchor="w", bg = '#FF6100')
instruc.place(relx=0.5, rely=0.06, relwidth=0.75, relheight=0.1, anchor='n')
instruc.config(font=("Arial",14))

temp = tk.Label(root, text = "Temperatura da Análise:", bg = '#FF6100')
temp.place(relwidth = 0.2, relheight = 0.03, rely = disty[0], relx = 0.2)
entry_temp = tk.Entry(root, font = 15)
entry_temp.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[0])

label_entry1 = tk.Label(root, text = "Nome do Arquivo 1:", bg = '#FF6100')
label_entry1.place(relwidth = 0.2, relheight = 0.03, rely = disty[1], relx = 0.2)
entry1 = tk.Entry(root, font = 15)
entry1.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[1])

legenda1 = tk.Label(root, text = "Legenda 1:", bg = '#FF6100')
legenda1.place(relwidth = 0.2, relheight = 0.03, rely = disty[2], relx = 0.2)
entry_legenda1 = tk.Entry(root, font = 15)
entry_legenda1.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[2])

label_entry2 = tk.Label(root, text = "Nome do Arquivo 2:", bg = '#FF6100')
label_entry2.place(relwidth = 0.2, relheight = 0.03, rely = disty[3], relx = 0.2)
entry2 = tk.Entry(root, font = 15)
entry2.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[3])

legenda2 = tk.Label(root, text = "Legenda 2:", bg = '#FF6100')
legenda2.place(relwidth = 0.2, relheight = 0.03, rely = disty[4], relx = 0.2)
entry_legenda2 = tk.Entry(root, font = 15)
entry_legenda2.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[4])

label_entry3 = tk.Label(root, text = "Nome do Arquivo 3:", bg = '#FF6100')
label_entry3.place(relwidth = 0.2, relheight = 0.03, rely = disty[5], relx = 0.2)
entry3 = tk.Entry(root, font = 15)
entry3.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[5])

legenda3 = tk.Label(root, text = "Legenda 3:", bg = '#FF6100')
legenda3.place(relwidth = 0.2, relheight = 0.03, rely = disty[6], relx = 0.2)
entry_legenda3 = tk.Entry(root, font = 15)
entry_legenda3.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[6])

label_entry4 = tk.Label(root, text = "Nome do Arquivo 4:", bg = '#FF6100')
label_entry4.place(relwidth = 0.2, relheight = 0.03, rely = disty[7], relx = 0.2)
entry4 = tk.Entry(root, font = 15)
entry4.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[7])

legenda4 = tk.Label(root, text = "Legenda 4:", bg = '#FF6100')
legenda4.place(relwidth = 0.2, relheight = 0.03, rely = disty[8], relx = 0.2)
entry_legenda4 = tk.Entry(root, font = 15)
entry_legenda4.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[8])

label_entry5 = tk.Label(root, text = "Nome do Arquivo 5:", bg = '#FF6100')
label_entry5.place(relwidth = 0.2, relheight = 0.03, rely = disty[9], relx = 0.2)
entry5 = tk.Entry(root, font = 15)
entry5.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[9])

legenda5 = tk.Label(root, text = "Legenda 5:", bg = '#FF6100')
legenda5.place(relwidth = 0.2, relheight = 0.03, rely = disty[10], relx = 0.2)
entry_legenda5 = tk.Entry(root, font = 15)
entry_legenda5.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[10])

label_entry6 = tk.Label(root, text = "Nome do Arquivo 6:", bg = '#FF6100')
label_entry6.place(relwidth = 0.2, relheight = 0.03, rely = disty[11], relx = 0.2)
entry6 = tk.Entry(root, font = 15)
entry6.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[11])

legenda6 = tk.Label(root, text = "Legenda 6:", bg = '#FF6100')
legenda6.place(relwidth = 0.2, relheight = 0.03, rely = disty[12], relx = 0.2)
entry_legenda6 = tk.Entry(root, font = 15)
entry_legenda6.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[12])


Espacamento1 = tk.Label(root, text = "Espaçamento entre 1 e 2:", bg = '#FF6100')
Espacamento1.place(relwidth = 0.2, relheight = 0.03, rely = disty[13], relx = 0.2)
entry_Espacamento1 = tk.Entry(root, font = 15)
entry_Espacamento1.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[13])


Espacamento2 = tk.Label(root, text = "Espaçamento entre 2 e 3:", bg = '#FF6100')
Espacamento2.place(relwidth = 0.2, relheight = 0.03, rely = disty[14], relx = 0.2)
entry_Espacamento2 = tk.Entry(root, font = 15)
entry_Espacamento2.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[14])

Espacamento3 = tk.Label(root, text = "Espaçamento entre 3 e 4:", bg = '#FF6100')
Espacamento3.place(relwidth = 0.2, relheight = 0.03, rely = disty[15], relx = 0.2)
entry_Espacamento3 = tk.Entry(root, font = 15)
entry_Espacamento3.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[15])

Espacamento4 = tk.Label(root, text = "Espaçamento entre 4 e 5:", bg = '#FF6100')
Espacamento4.place(relwidth = 0.2, relheight = 0.03, rely = disty[16], relx = 0.2)
entry_Espacamento4 = tk.Entry(root, font = 15)
entry_Espacamento4.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[16])

Espacamento5 = tk.Label(root, text = "Espaçamento entre 5 e 6:", bg = '#FF6100')
Espacamento5.place(relwidth = 0.2, relheight = 0.03, rely = disty[17], relx = 0.2)
entry_Espacamento5 = tk.Entry(root, font = 15)
entry_Espacamento5.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[17])


title_graf = tk.Label(root, text = "Titulo do grafico:", bg = '#FF6100')
title_graf.place(relwidth = 0.2, relheight = 0.03, rely = disty[18], relx = 0.2)
entry_title_graf = tk.Entry(root, font = 15)
entry_title_graf.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[18])

fonte_graf = tk.Label(root, text = "Fonte do grafico:", bg = '#FF6100')
fonte_graf.place(relwidth = 0.2, relheight = 0.03, rely = disty[19], relx = 0.2)
entry_fonte_graf = tk.Entry(root, font = 15)
entry_fonte_graf.place(relwidth = 0.4, relheight = 0.03, relx = 0.4, rely = disty[19])

botao = tk.Button(root, text = "Plotar Gráfico", command = fgraficos)
botao.place(relwidth = 0.15, relheight = 0.04, rely = 0.96, relx = 0.5, anchor='n')






root.mainloop()