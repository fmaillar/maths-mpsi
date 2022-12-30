all: fig
	latexmk
fig:
	python *.py
cleanTemp:
	latexmk -c
cleanAll:
	latexmk -C
