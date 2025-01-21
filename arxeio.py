file =open("file1.txt","w")
line3= "Kostantina"
file.write(line3)
file.close()

file =open("file1.txt","r")

text= file.read()
print(text)
file.close()
    