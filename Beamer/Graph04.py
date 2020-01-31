import math

write = open("Graph04.tex","w")
Max = 20000
s = 0.0
for i in range (1,Max+1,400):
	write.write ("\\fill [vermillion](%d,%f) circle (2pt);\n" % (i,math.log(i)))

s = 0.0
write.write ("\\draw [vermillion] ")
for i in range (1,Max+1,400):
	write.write ("(%d,%f)" % (i,math.log(i)))
	if i<Max-400:
		write.write(" -- ")
write.write(";\n")




