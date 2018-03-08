#!/usr/bin/python3.5

class Persoana():

	nr_persoane = 0

	def __init__(self, nume, varsta):
		self.nume = nume
		self.varsta = varsta
		self.nr_persoane = self.nr_persoane + 1

	def getNume(self):
		return self.nume

	def setVarsta(self, varsta):
		self.varsta = varsta

	def getVarsta(self):
		return self.varsta

	def toatePersoanele(self):
		return self.nr_persoane


p1 = Persoana("Adi", 23)
p2 = Persoana("Ramon", 24)

print (p1.getNume())
print (p1.getVarsta())

p1.setVarsta(50)

print (p1.getNume())
print (p1.getVarsta())


print (p2.getNume())
print (p2.getVarsta())
