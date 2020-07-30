filename=mathematiques

pdf: ps
	 ps2pdf ${filename}.ps 
	 
ps: dvi
	dvips -t a4 ${filename}.dvi -o ${filename}.ps 
	
dvi:
#	gnuplot *.gnuplot||true
#	as *.asy||true
	latex ${filename}
#	bibtex ${filename}||true
#	makeindex ${filename}.idx
#	latex ${filename}> /dev/null
	latex ${filename} #> /dev/null
	latex ${filename} #> /dev/null

read:
	evince ${filename}.pdf &

aread:
	acroread ${filename}.pdf &

clean:
	rm -f *.log *.aux *.out *.bbl *.blg *.lof *.lot *.toc *.ilg *.idx *.ind *~ ${filename}.m*
