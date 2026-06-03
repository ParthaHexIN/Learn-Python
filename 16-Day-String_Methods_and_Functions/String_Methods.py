# s = "hello world" #string are immutable
# a = len(s) #length of string
# print(a) #11

# print (s.upper()) #HELLO WORLD
# print (s.lower()) #hello world
# print (s.capitalize()) #Hello world
# print (s.title()) #Hello World


# text=" \nhello world "
# print (text.split()) #['hello', 'world']
# print (text.strip ()) #hello world
# print (text.lstrip()) #hello world
# print (text.rstrip()) #hello world


# text="python is great language and python is easy to learn"
# print (text.count('python') ) #2
# print (text.find('great')) #10
# print (text.replace('python', 'java')) #java is great language and java is easy


# text= " apple , banana, orange "
# print (text.split(","))
# print (text.strip())
# print(",".join(['Apple', 'Banana', 'orange']))


text ="partha12345"
print (text.isalpha()) #False
print (text.isdecimal()) #False
print (text.isdigit()) #False
print (text.isalnum()) #True


# print (text.count('o')) #2
# print (text.find('o')) #4
# print (text.replace('o', 'a')) #hella warld
# print (text.split()) #['hello', 'world']
# print (text.strip()) #hello world
# print (text.lstrip()) #hello world