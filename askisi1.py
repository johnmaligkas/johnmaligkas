file= open("fakelos1.txt" ,"r")
text= file.read()
print(text)
file.close()

file =open("asd.txt","w")

file.write(text)
file.close()

