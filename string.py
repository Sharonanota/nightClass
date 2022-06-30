#Convert half of string into capital 
from doctest import script_from_examples
from numpy import array


def full():
 a="siara"
 b=len(a)
 c=a.lower()
 d=a.upper()
 e=b//2
 print(c[:e]+d[e:])
 
f=" i love akirachix"
print(f.title() )

d="python is cool"
print(d.center(50, '*'))

text = "pYtHon"
print(text.casefold())
   
text1 = 'groß'
print(text1.casefold())
print(text1.lower())

string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)
print(count)

s='siara'
print(s[::2])
print(s[2::])

count = 0
for letter in 'Hello World':
    if(letter == 'e'):
        count += 1
print(count,'letters found')

# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")
   
  
   
# full()   
# def pali(words):
#     y=words.split()
#     y[0],y[-1]=y[-1],y[0]
#     left=0
#     right=len(words)-1
#     while left<right:
#         left+=1
#         right-=1
    
# pali(input("Enter word:"))    
# person="Elon mask"
# reaction="cool"
# print("wow," +person + "!" +reaction + "!")
# print("wow, %s! %s!" %(person,reaction) )
# print("wow, {}! {}!".format(person,reaction))
# print(f"wow,{person}!{reaction}!")



# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

# def donuts(count):
#     if count<9:
#         print("number of donuts is many")
#     if count>10:
#         w=str(count)
#         print("number of donuts:"+w)
# donuts(int(input("Enter number:")))   

# a="I am AkiraChix"
# y=a.split() 
# start=[0]
# end=len(a)-1
# while start < end:
#     y[start],y[end]=y[end],y[start]
#     start+=1
#     end-=1
#     s=""
#     z=(y.join(s))
#     if z==a:
#         print("palindrome")
#     else:
#         print("not")    
        
        
def palindrome(x):
    start=0
    end=len(x)-1
    result=x.split()
    while start<end:
        result[start],result[end]=result[end],result[start]
        start +=1
        end-=1
        s="".join(result)
        print(s)
        if s==x:
            print("This is  not a palindrome")
        else:
            print("This is a palindrome")
        # break
palindrome(input("Enter a word:"))   



  
    
    

           