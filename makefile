deploy : test
	tox -e deploy
test :
	tox -qqe test
clean :
	rm -rf build dist etronome.egg-info
