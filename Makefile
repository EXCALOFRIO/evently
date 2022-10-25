run: 
	python3 src/inicio.py

test: 
	python3 src/TDD.py

commit:
	git add .
	git commit -m "Commit"
	git push