from __future__ import annotations
from typing import List

class Product:
    def __init__(self, name: str, inventory: int = 0):
        self.__name = name
        self.__inventory = inventory
        self.__lastSale: Sale = None

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def decreaseInventory(self, amount: int):
        if self.__inventory >= amount:
            self.__inventory -= amount
        else:
            raise ValueError("Not enough inventory")

    def getInventory(self) -> int:
        return self.__inventory

    def __str__(self):
        return f"Product(name={self.__name}, inventory={self.__inventory})"

class Sale:
    __saleTimes = 0

    def __init__(self, products: List[Product]):
        Sale.__saleTimes += 1
        self.__saleNumber = Sale.__saleTimes
        self.__products = products

        for product in products:
            product.setLastSale(self)
            product.decreaseInventory(1)

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber

    def getProducts(self) -> List[Product]:
        return self.__products


# Example usage
productOne = Product(name="Widget", inventory=10)
productTwo = Product(name="Gadget", inventory=5)

saleOne = Sale([productOne, productTwo])
saleTwo = Sale([productOne])
saleThree = Sale([productTwo])

print(f"Sale 1: {productOne.getLastSale.getSaleNumber}, Sale 2: {productTwo.getLastSale.getSaleNumber}")
print(f"Remaining inventory for productOne: {productOne.getInventory()}")
print(f"Remaining inventory for productTwo: {productTwo.getInventory()}")
