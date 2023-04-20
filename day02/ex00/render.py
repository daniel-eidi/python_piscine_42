from settings import *
import sys

def close_body(htmlFile):
	htmlFile.write('''
</body>

</html>''')
	return



def render():
	try:
		if(len(sys.argv) == 2 or sys.argv[1].split(".")[1] == "template"):
			print("Args Ok!")
	except:
		print("Wrong args\n")	
		sys.exit()
	try:
		template = open(sys.argv[1], "r")
	except:
		print("could not create file\n")	
		sys.exit()
	try:
		htmlFile = open(f'{sys.argv[1].split(".")[0]}.html', "w")
	except:
		print("could not open template file\n")	
		sys.exit()
	template = template.read()
	template = template.format(name = name, surname = surname, age = age , profession = profession, title = title)
	htmlFile.write(f'''
	{template}
	 ''')
	htmlFile.close()
    

if __name__ == '__main__':
	variables={'name' : 'NAME', 'surname' : 'SURNAME', 'age' : 'set your age', 'profession' : 'PROFESSSION', 'title' : 'TITLE'}
	for key , values in variables.items():
		globals().setdefault(key, values)

	render()
	