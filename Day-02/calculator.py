def add(n1,n2):
    return n1+n2
def subtractoin(n1,n2):
    return n1-n2
def divide(n1,n2):
    if(n2==0):print(" you cant put 0")
    return n1/n2
def multip(n1,n2):
    return n1*n2
def uslu(n1,n2):
    multiple=1
    for i in range(n2):
        multiple=multiple*n1
    return multiple
def faktoriyel(n1):
    multiple = 1
    for i in range(1, n1 + 1):
        multiple *= i
    return multiple
  

operations={
    "+": add,
    "-":subtractoin,
    "/":divide,
    "*":multip,
    "ˆ":uslu,
    "!":faktoriyel

}
should_contuniue=True
while should_contuniue:
    num1=int(input("enter num1:"))
    print(operations)
    operations_choice=input("pick operations:")
    num2=int(input("enter num2:"))
    answer=(num1)(operations[operations_choice])(num2)
    print(f"{num1}{operations_choice}{num2}={answer}")
    continu=input("would you like contuniue:")
    if continu=="no":
        print("exit")
        should_contuniue=False

    else:
        print(20*"\n")

    

       
       
    

