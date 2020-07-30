reset
set terminal png
set output "arccos.png"
set grid
set size square
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key right bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set samples 10000
f(x) = x < 0 ? 0/0 \
: cos(x)
#plot [-1.2:pi] acos(x) w l ls 1 title "arccos x", cos(x) w l ls 2 title "cos x", x w l ls 3
plot [-1.2:pi] acos(x) w l ls 1 title "arccos x", f(x) w l ls 2 title "cos x", x w l ls 3
