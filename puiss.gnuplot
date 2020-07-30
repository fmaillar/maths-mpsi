reset
set terminal png
set output "puiss.png"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "green"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set style line 4 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 5 lt 1 lw 3 pt 3 linecolor rgb "pink"
set key top
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [0:4]
plot [0:4] 1 w l ls 1 title "a=0", x**2 w l ls 4 title "a>1", x w l ls 5 title "a=1", sqrt(x) w l ls 2 title "0<a<1", 1/x w l ls 3 title "a<0"

