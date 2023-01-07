Ceci est mon cours de mathématiques de MPSI 2007-2008 dispensé au Lycée Pierre 
d'Ailly par Mme Sophie RAINERO.


Pour générer les figures, il est nécessaire d'utiliser Python (3.10 ici) et ses 
bibliothèques scientifiques NumPy, SciPy et MatplotLib.
Pour les tracer, il suffit de lancer le script process_fig.py ou bien le 
MakeFile :

make fig

Pour générer le cours en pdf, on lance le MakeFile qui utilise latexmk:

make

LaTeXMk gère automatiquement le nombre de compilations nécessaires pour générer 
les figures, les tables et les références croisées.
