clean :
	rm -rf build dist etronome.egg-info
build : clean
	python setup.py sdist bdist_wheel
