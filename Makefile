all:
	latexmk
fig:
	py process_fig.py
cleanTemp:
	latexmk -c
cleanAll:
	latexmk -C
