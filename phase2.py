lst = [1]
final = "1"
for j in range(1,6):
	lst.append(lst[j-1]*(j+1))
	final = final + " "+str(lst[-1])
print final

