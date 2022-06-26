class Calculator:
  def __init__ (self,a,b):
    self.a = a
    self.b = b
  
  def add(self):
    
    result = self.a + self.b
    return result

  def subt(self):
    
    result = self.a - self.b
    return result
  def mul(self):

    result = self.a*self.b
    return result

  def quotient(self):
    result = self.a//self.b
    return result

  def remainder(self):

    result = self.a%self.b
    return result
  def div(self):
    result = format(self.a/self.b,'0.2f')
    return result 

a, b = input().split()
a = int(a)
b = int(b)

obj = Calculator(a,b)

print(obj.add())
print(obj.subt())
print(obj.mul())
print(obj.quotient())
print(obj.remainder())
print(obj.div())
