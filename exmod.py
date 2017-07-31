#Function File
#Basic Interface
class CollectData:
	def __init__(self,price_purchased,lifespan, data1, data2, data3, data4):
		self.pp = price_purchased
		self.ls = lifespan
		self.d1 = data1
		self.d2 = data2
		self.d3 = data3
		self.d4 = data4

	def printVal(self):
		print(self.pp, self.yo, self.d1,self.d2,self.d3,self.d4)


	def calcSalvageValue(self):
		return self.d1 + self.d2 + self.d3 + self.d4


	#def MlAlgorithm(): #one of the algorithms to train on data sets

	def StraightLineAlgorithm(self, purchase_price, longetivity, salvage_Value):
		depreciation_rate = 1/longetivity
		annual_depreciation = depreciation_rate * (purchase_price - salvage_Value)
		final_price = purchase_price - annual_depreciation
		return final_price

#the salvage 1-4 values should be such that their sum is less than purchase price
purchase_price = int(input("Enter current price of product : "))
lifespan = int(input("Enter the lifespan of the product : "))
salvage_v1 = int(input("Enter the salvage value 1 of the product : "))
salvage_v2 = int(input("Enter the salvage value 2 of the product : "))
salvage_v3 = int(input("Enter the salvage value 3 of the product : "))
salvage_v4 = int(input("Enter the salvage value 4 of the product : "))

Item1 = CollectData(purchase_price, lifespan, salvage_v1, salvage_v2, salvage_v3, salvage_v4) 
SalvageValue = Item1.calcSalvageValue()
print(Item1.StraightLineAlgorithm(purchase_price, lifespan, SalvageValue))
 




