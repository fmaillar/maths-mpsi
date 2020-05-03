reset
set terminal postscript enhanced color
set output "trig.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "green"
set style line 4 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [-2:2]
plot [-pi:pi] sin(x) w l ls 1 title "sin x", cos(x) w l ls 2 title "cos x", tan(x) w l ls 3 title "tan x", 1/tan(x) w l ls 4 title "cotan x"
