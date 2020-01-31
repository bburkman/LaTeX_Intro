write = open("Graph03.tex","w")
Max = 20000
s = 0.0
for i in range (1,Max+1,1):
	a = 1/float(i)
	s += a
	if i%400==2:
		write.write ("\\fill (%d,%f) circle (2pt);\n" % (i,s))

s = 0.0
write.write ("\\draw ")
for i in range (1,Max+1,1):
	a = 1/float(i)
	s += a
	if i%400==2:
		write.write ("(%d,%f)" % (i,s))
		if i<19600:
			write.write(" -- ")
write.write(";\n")




