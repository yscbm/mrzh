# -*- coding: utf8 -*- 
import tkinter as tk
from tkinter import ttk

import cv2
import numpy as np
import json
from collections import OrderedDict
import math
import mrzh_data

class MrzhWindow():
	def __init__(self):
		self.win_root = tk.Tk()
		self.win_root.resizable(width=False, height=False)
		self.win_root.geometry('500x600+300+120')
		self.win_root.title('xxxx')
		self.items = mrzh_data.ItemList()
		self.add_win_left()
		self.add_win_item_list()

	def add_win_left(self):
		self.left_label = tk.Label(self.win_root,bg='#dddddd',width = 10,compound='left',text='高级物品')
		self.left_label.place(x=0, y=0)
	
		number = tk.StringVar()
		self.numberChosen = ttk.Combobox(self.win_root, width=10, textvariable=number)
		self.numberChosen.place(x=100, y=0)
		self.numberChosen['values'] = ('uzi', '警用卫衣','铁铸件')     # 设置下拉列表的值
		self.numberChosen.current(0)
		self.numberChosen.bind("<<ComboboxSelected>>",self.show_info)

	def add_win_item_list(self):
		#self.item_list_label = 

		self.frame=ttk.Frame(self.win_root)
		self.frame.place(x=0, y=40)
		#self.frame.pack(fill='both',expand='false')

		self.tree=ttk.Treeview(self.frame,columns=['数量','基础物品','单价','物品总价'],show='headings',height=18)
		
		self.tree.column('数量', width=50) 
		self.tree.column('基础物品', width=100) 
		self.tree.column('单价', width=50) 
		self.tree.column('物品总价', width=100) 

		self.tree.heading('数量',text='数量')
		self.tree.heading('基础物品',text='基础物品')
		self.tree.heading('单价',text='单价')
		self.tree.heading('物品总价',text='物品总价')
		self.tree.pack()






	def show_info(self,event):
		select = self.numberChosen.get()
		print(select)
		need_list = mrzh_data.find_base_item(self.items,select,1)
		for i in need_list:
			print('%-4d  %-20s  '%(need_list[i],i.name))

		x = self.tree.get_children()
		for item in x:
			self.tree.delete(item)

		price_sum = 0
		for i in need_list:
			self.tree.insert('','end',values=(need_list[i],i.name,i.price,need_list[i]*i.price))
			price_sum+=need_list[i]*i.price
		self.tree.insert('','end',values=('','','总价',price_sum))

	def show(self):
		self.win_root.mainloop()



def main():

	win = MrzhWindow()
	win.show()

if __name__ == '__main__':
	main()