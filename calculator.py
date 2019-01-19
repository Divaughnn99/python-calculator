print("type a number")
n1 = int(input())
print("pick one of the following math symbols:x, /, +, -, \"%\", %")
symbol = input()
print("type another number")
n2 = int(input())

if symbol == 'x':
    n3 = n1 * n2
else:
    if symbol == '/':
        n3 = n1 / n2
    else:
        if symbol == '+':
            n3 = n1 + n2
        else:
            if symbol == '-':
                n3 = n1 - n2
            else:
                # if symbol == '\"%\"':
                #     n3 = n1 '%' n2
                # else:
                if symbol == '%':
                    n3 = n1 % n2

print("your awnser is", n3)
    
