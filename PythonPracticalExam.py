#Question no.1) Write a function that finds the sum of the 

#(a)First n odd terms

def odd_sum():
    user_input = int(input("Enter the number: "))
    sum=0
    i=1
    while(i<=user_input):
        sum=sum+i
        i=i+2
    print("sum of odd numbers upto",user_input,"=",sum)

odd_sum()

#(b)First n even 
def even_sum():
    user_input = int(input("Enter the number: "))
    sum=0
    i=2
    while(i<=user_input):
        sum=sum+i
        i=i+2
    print("sum of even numbers upto",user_input,"=",sum)

even_sum()

#(c)1,2,4,3,5,7,9,6,8,10,11,13...till n-th term
def sumodd(num):
    return num*num

def sumeven(num):
    return (num*(num+1))

def series_sum():
    user_input = int(input("Enter the number: "))
    odd = 0
    even = 0
    pow = 1 
    check = 0
    count = 0
    while (user_input > 0):
        minimum = min(pow,user_input)
        user_input -= minimum

        if (check == 0):
            count = count + sumodd(odd+minimum) - sumodd(odd) 
            odd += minimum

        else:
            count = count+ sumeven(even + minimum) - sumeven(even)
            even += minimum

        pow *= 2

        check ^= 1

    return count

print(series_sum())

#Question no.2)Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10) and perform following operations.

t1 = (1,2,5,7,9,2,4,6,8,10)

user_input = int(input('''What you want to do?
1 = Print half the values of tuple in one line and other half in the next line
2 = Print another tuple whose values are even numbers in the given tuple
3 = Concatenate a tuple t2 (11,13,15) with t1
4 = Return  maximun and minimum value from this tuple'''))

if user_input == 1 :
    a = t1[:5]
    b = t1[5:]
    print(a)
    print(b)

elif user_input == 2 :  
    n = list(t1)
    m = list()

    for x in n :
        if x in n:
            if (x%2 == 0) :
                m.append(x)
        s = tuple(m)
    print("Tuple =",s) 

elif user_input == 3 :  
    t2 = (11,13,15)
    a = list(t1)
    b = list(t2)
    c = a+b
    print(c)

elif user_input == 4 :  
    print("Max number = ",max(t1) )
    print("Min number = ",min(t1))

else:
    print("please enter the number from the given choice only")


#Question no 3) Write a menu driven program to perform following operations on strings.

def string():
    choice =int(input('''Enter your choice 
1 = length of the string
2 = maximum of three strrings
3 = Replace every successive character with #
4 = number of words in the string
'''))

    if choice == 1:
        n = input("Enter a string : ")
        l=len(n)
        print("The length of the string is =",l)      
    elif choice == 2:
        n1 = input("Enter 1st string : ")
        n2 = input("Enter 2nd string : ")
        n3 = input("Enter 3rd string : ")
        print("The maximum of the three strings is =",max(n1,n2,n3))    
    elif choice == 3:
        n = input("Enter a string : ")
        s = ""
        m = list(n)
        for i in range(len(n)):
            if (i%2 != 0):
                if m[i] == " ":
                    m[i] = " "
                else:
                    m[i] = "#"
        for x in m:
            s=s+x
        print("The sucessive character in the string is replaced with # :",s) 
    elif choice == 4:
            n = input("Enter a string : ")
            c = 0
            for y in n :
                if y == " " :
                    c += 1
            w = c+1
            print("The number of words = ",w) 
    else :
        print("please enter the number from the given choice only")

string()
