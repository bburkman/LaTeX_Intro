write = open("Graph01.tex","w")
Max = 10
s = 0.0
for i in range (2,Max,1):
	a = 1/float(i)
	s += a
	write.write ("\\fill (%d,%f) circle (2pt);\n" % (i,s))

s = 0.0
write.write ("\\draw ")
for i in range (2,Max,1):
	a = 1/float(i)
	s += a
	write.write ("(%d,%f)" % (i,s))
	if i<Max-1:
		write.write(" -- ")
write.write(";\n")




