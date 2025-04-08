all: main.py graph.py
	python main.py pcv4.txt pcv10.txt pcv50.txt pcv177.txt

test: main.py graph.py
	python main.py pcv4.txt pcv10.txt pcv50.txt pcv177.txt

clean:
	rm -f *.pyc
	rm -rf __pycache__