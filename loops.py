# while loops

num1=2
while num1<=15:
    print(num1)
    num1+=1
# run a loops that starts from 100 to 0 and decreases by 5
#the above is called the increment loop
num2=100
while num2>=0:
    print(num2)
    num2-=5
age=24
print(f"My age is {age}")
# the above is commonly known as the decrement loop

# for loop
name=["sally","gne","herts"]
for i in name:
    print(i)
num=[2,4,3,2,4,6,5,4]
total=0
# a loop to give the sum of the numbers
for n in num:
    total+=n
print(f"The total for all the numbers is: {total}")
numbers=[1,2,3,4,5,6,7,8,9,10,11]
evens=[]
for n in numbers:
    if n%2==0:
        evens.append(n)
    print(evens)
# time and space complexity
# big o anotations
