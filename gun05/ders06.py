#If you use the nonlocal keyword, the variable will belong to the outer function
# nonlocal ustten erişilebilir fakat globalleştirmez değişkeni
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
print(x)