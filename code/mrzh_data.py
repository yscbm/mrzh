# -*- coding: utf8 -*- 
import json
import codecs


class item(object):
	"""docstring for item"""
	def __init__(self,josn_str):
		super(item, self).__init__()
		self.name = josn_str['name']
		self.level = josn_str['level']
		self.quality = josn_str['quality'] 
		self.price = josn_str['price'] 
		self.combine = josn_str['combine'] == 1
		if self.combine == True:
			self.combine_list = josn_str['combine_list']




class ItemList(object):
	"""docstring for item_list"""
	def __init__(self):
		super(ItemList, self).__init__()
		self.item_list_ = {}
		json_path = '../resources/item.json'
		ff = codecs.open(json_path, 'r', 'utf-8')
		json_str = json.load(ff)

		for i in json_str:
			self.item_list_[i['name']] = item(i)
		
		#for i in self.item_list_:
		#	print(i)
		#	print (self.item_list_[i])




	def get_item_info(self,name):
		return self.item_list_[name]

def find_base_item(items,name,k):
	need_list = {}
	if items.get_item_info(name).combine == 0:
		need_list[items.get_item_info(name)] =k
		return need_list
	else:
		list_ = items.get_item_info(name).combine_list
		for i in list_:
			need_list_ = find_base_item(items,i,list_[i])
			
			for j in need_list_:
				if j in need_list:
					need_list[j] += need_list_[j]*k
				else:
					need_list[j] = need_list_[j]*k
	return need_list

def main():
	items = ItemList()

	#print(items.get_item_info('uzi').name)
	name = '警用卫衣'
	print (name)

	need_list = find_base_item(items,name,1)
	for i in need_list:
		print('%-4d  %-20s  '%(need_list[i],i.name))
		#print (i.name,' ',need_list[i])
	#print(need_list)

	#print(items.get_item_info('布').combine_list[0])

if __name__ == '__main__':
	main()
		
