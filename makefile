build : clean
	python setup.py sdist bdist_wheel
clean :
	rm -rf build dist etronome.egg-info
deploy : build
	twine upload dist/*
