reset
set terminal png
set output "logbase.png"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
plot [-3:3] log(x) w l ls 1 title "a>0", -log(x) w l ls 2 title "a<0"
