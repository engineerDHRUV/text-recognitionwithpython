import os.path
#made by dhruv fauzdar

checkDirs = ['words/', 'words/a01/a01-000u/']
checkFiles = ['words.txt', 'test.png', 'words/a01/a01-000u/a01-000u-00-00.png']
#made by dhruv fauzdar

for f in checkDirs:
	if os.path.isdir(f):
		print('[OK]', f)
	else:
		print('[ERR]', f)

#made by dhruvfayzdar
for f in checkFiles:
	if os.path.isfile(f):
		print('[OK]', f)
	else:
		print('[ERR]', f)
