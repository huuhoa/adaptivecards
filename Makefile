clean:
	rm -rf build dist adaptivecards.egg-info

sdist:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/* --verbose

bump_minor:
	bump2version minor

bump_major:
	bump2version major
