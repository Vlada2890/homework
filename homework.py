#1.16
def my_function():
  print("Hello ")
my_function()
#2.16
A = ['a', 'b', 'c', 'd', 'e', '​', '​f']
def f(A):
  print(len(A))
f(A)
#3.16
letters = "ABCDEF"
letters = letters[::-1]
print(letters)
#1.17
a = int(input())
def t(a):
    if a % 2 == 0:
        print("odd number")
    else:
      print("even number")
t(a)
#2.17
yhn = input()
def tt(yhn):
    if type(yhn) == str:
      print("This type is str")
    if type(yhn) == int:
        print("This type is int")
tt(yhn)

#3.17
n = input()
c = type(n)
def yy(n):
    print('This is', (c))
yy(n)
