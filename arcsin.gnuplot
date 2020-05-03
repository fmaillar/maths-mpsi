reset
set terminal postscript enhanced color
set output "arcsin.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key right bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [-2:2]
set xrange [-2:2]
f(x) = x <= -pi/2 ? 0/0 \
:x <= pi/2 ? sin(x) \
: 0/0
plot [-2:2] asin(x) w l ls 1 title "arcsin x", f(x) w l ls 2 title "sin x", x w l ls 3
