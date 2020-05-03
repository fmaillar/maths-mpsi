reset
set terminal postscript enhanced color
set output "trigh.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [-2:2]
plot [-2:2] sinh(x) w l ls 1 title "sinh x", cosh(x) w l ls 2 title "cosh x"
