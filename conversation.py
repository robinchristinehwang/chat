def print_conversation(inputfile):
	lines = []
	with open(inputfile, 'r', encoding = 'utf-8-sig') as l:
		for line in l:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None #無預設值 虛無的
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = print_conversation('input.txt')
	lines = convert(lines)
	write_file('output1.txt', lines)


main() #


