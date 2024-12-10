

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
files = [x.lower() for x in files if x.lower().count('png') > 0]
print(*sorted(set(files)))