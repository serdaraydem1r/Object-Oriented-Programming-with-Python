class Calculator(object):
    # init metodu
    def __init__(self,a,b):
        """
                initialize -> values
        """
        self.value1 = a
        self.value2 = b
    def add(self):
        """
                 addition a+b = result
                :return: result
        """
        return self.value1 + self.value2

    def sub(self):
        """
                subtraction a-b = result
                :return: result
        """
        return self.value1 - self.value2

    def div(self):
        """
                division a/b = result
                :return: result
        """
        return self.value1 / self.value2

    def mul(self):
        """
                multiplication a*b = result
                :return: result
        """
        return self.value1 * self.value2

print("\n Choose add(1),\n Choose subtract(2),\n Choose Division(3),\n Choose Multiplication(4)")

selection = input("Select : ")
v1 = float(input("Enter a number: "))
v2 = float(input("Enter another number: "))
c1 = Calculator(v1,v2)
if selection == "1" :
    add_result = c1.add()
    print("Addition : {}".format(add_result))
elif selection == "2" :
    sub_result = c1.sub()
    print("Subraction : {}".format(sub_result))
elif selection == "3" :
    div_result = c1.div()
    print("Division : {}".format(div_result))
elif selection == "4" :
    mul_result = c1.mul()
    print("Multiplication : {}".format(mul_result))
else :
    print("Invalid selection")


