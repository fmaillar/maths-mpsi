reset
set terminal postscript enhanced color
set output "argtanh.ps"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key right bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set samples 10000
set yrange [-2:2]
plot [-2:2] tanh(x) w l ls 1 title "tanh x", 0.5*log((1+x)/(1-x)) w l ls 2 title "argtanh x", x w l ls 3
