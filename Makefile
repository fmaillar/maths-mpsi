all:
	latexmk
fig:
	python3 process_fig.py
cleanTemp:
	latexmk -c
cleanAll:
	latexmk -C
