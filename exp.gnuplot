reset
set terminal postscript enhanced color
set output "exp.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "red"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
f(x) = x < -1 ? 0/0 \
: x+1
plot [-3:2] exp(x) w l ls 2 title "exp", f(x) w l ls 1 title "x-1"
