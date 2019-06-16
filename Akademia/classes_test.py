x = 44
class nad:
	x = 0
	def a(self):
		print('nad')

class a1(nad):
	pass

class a2(nad):
	def a(self):
		print('a2')

class b1(nad):
	def a(self):
		print('b1')

class b2(nad):
	def b(self):
		print('b2')

class a(a1, a2):
	pass

class b(b1, b2):
	pass

class children(a,b):
	pass

class klasa:
    def metoda(self):
        print (self.a)

k = klasa()
klasa.a = 9
k.metoda()



a1_ = a1()
a1_.x = 99
d= children()
print(d.b())
print(d.x)