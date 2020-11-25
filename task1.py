x = int(input("Enter interval: "))
y = int(input("Enter distance travelled: "))
z = int(input("Enter max distance: "))

if ((y%x) + z) >= x:
    print("YES")
else:
    print("NO")
