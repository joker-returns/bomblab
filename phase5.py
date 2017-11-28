# ebx == input string
esi = ['i', 's', 'r', 'v', 'e', 'a', 'w', 'h', 'o', 'b', 'p', 'n', 'u', 't', 'f', 'g']
alp = "abcdefghijklmnopqrstuvwxyz"
cur = ""
final = "giants"
"""
for char in input_string:
	char = char & 0xf
	char2 = esi[char]
	cur.append(char2)
"""
for letter in final:
	for l in alp:
		m = l
		l = ord(l) & 0xf
		char2 = esi[l]

		if(char2 == letter):
			print m+" "+letter
			cur = cur + m
			break

print cur