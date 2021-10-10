
class R1M:	
  def __init__(self,model,exhaust,suspension,wheel,clothes,hp,speed,price):	
    self.model = model
    self.exhaust = exhaust
    self.suspension = suspension
    self.wheel = wheel
    self.clothes = clothes
    self.hp = hp
    self.speed = speed
    self.price = price

  def mymotoa(self):
    print("Xe "+ self.model)

  def mymotob(self):
  	print("Ống xả "+ self.exhaust)

  def mymotoc(self):
  	print("Phuộc "+self.suspension)

  def mymotod(self):
  	print("Mâm "+self.wheel)

  def mymotoe(self):
  	print("Dàn áo "+self.clothes)

  def mymotof(self):
  	print("Công suất "+self.hp)

  def mymotox(self):
  	print("Tốc độ tối đa "+self.speed)
  def mymotoz(self):
  	print("Giá bán "+self.price)


r1 = R1M("YAMAHA YFZ R1M","Akrapovic","Ohlins","OZ racing","carbon","199 HP","325 KM/h","1 Tỷ 300 Triệu")
r1.mymotoa()
r1.mymotob()
r1.mymotoc()
r1.mymotod()
r1.mymotoe()
r1.mymotof()
r1.mymotox()
r1.mymotoz()


# 3
# 1 0
# 2 $
# 3 1
# # Error Code: integer division or modulo by zero
# # Error Code: invalid literal for int() with base 10: '$'
# # 3

