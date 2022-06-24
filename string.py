#Convert half of string into capital 
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
   
  
   
full()   
def pali(words):
    y=words.split()
    y[0],y[-1]=y[-1],y[0]
    left=0
    right=len(words)-1
    while left<right:
        left+=1
        right-=1
    
pali(input("Enter word:"))                