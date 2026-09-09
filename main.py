import os

class browse:
	def clear():
		os.system('clear')
	def browse(url):
		os.system(f'curl -L -A "Mozilla/5.0" --compressed -s "{url}" | ''textutil -convert txt -stdin -stdout')
while True:
	try:
		url = input("Enter URL: ")
		browse.clear()
		browse.browse(url)
		continue
	except KeyboardInterrupt:
		print("\nGoodbye!")
		break
	except EOFError:
		print("\nGoodbye!")
		break
