all:
	latexmk
fig:
	python process_fig.py
cleanTemp:
	latexmk -c
cleanAll:
	latexmk -C
