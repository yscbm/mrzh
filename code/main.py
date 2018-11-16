# -*- coding: utf8 -*- 
import tkinter as tk
from tkinter import ttk

import cv2
import numpy as np
import json
from collections import OrderedDict
import math


class MrzhWindow():
	def __init__(self):
		self.win_root = tk.Tk()
		self.win_root.resizable(width=False, height=False)
		self.win_root.geometry('1000x800+300+120')
		self.win_root.title('xxxx')
		self.add_win_left()

	def add_win_left(self):
		self.left_label = tk.Label(self.win_root,bg='#dddddd',width = 10,compound='left',text='高级材料')
		self.left_label.place(x=0, y=0)
	
		number = tk.StringVar()
		self.numberChosen = ttk.Combobox(self.win_root, width=10, textvariable=number)
		self.numberChosen.place(x=100, y=0)
		self.numberChosen['values'] = (, 2, 4, 42, 100)     # 设置下拉列表的值
		self.numberChosen.current(0)
		self.numberChosen.bind("<<ComboboxSelected>>",self.win_print)
	def win_print(self,event):
		select = self.numberChosen.get()
		print(select)

	def show(self):
		self.win_root.mainloop()



def main():

	win = MrzhWindow()
	win.show()

if __name__ == '__main__':
	main()