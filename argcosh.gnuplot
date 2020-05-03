reset
set terminal postscript enhanced color
set output "argcosh.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [0:5]
plot [0:5] cosh(x) w l ls 1 title "cosh x", log(x+sqrt(x**2-1)) w l ls 2 title "argch x", x w l ls 3
