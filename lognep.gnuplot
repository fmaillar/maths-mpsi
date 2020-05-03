reset
set terminal postscript enhanced color
set output "lognep.ps"
set grid
set size square
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
plot [-0.5:3] log(x) w l ls 1 title "ln x", x-1 w l ls 2 title "x-1"
