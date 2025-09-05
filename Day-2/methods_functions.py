msg="Hello World!"
#STRING METHODS
print(len(msg))
print(msg.capitalize())
print(msg.upper())
print(msg.lower())
print(msg.center(0))
print(msg.casefold())
print(msg)
print(msg.title())

#remove whitespaces
newMsg="     hiiiii world     "
print(newMsg.strip())
print(newMsg.lstrip())
print(newMsg.rstrip())

#find and replace
text="coding is fun "
print(text.find('ing'))
print(text.replace("coding","dsa"))
print(text)

#Split and join
basket="apple,mangos,oranges,grapes"
fruits=basket.split(",")
print(fruits)
new_text = " * ".join(fruits)
print(new_text)

#string properties
fact="234"
print(fact.isalnum())
print(fact.isalpha())
print(fact.isascii())
print(fact.isdecimal())

#CHARACTER ENCODING
print(ord('e'))
print(chr(101))