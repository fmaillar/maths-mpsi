reset
set terminal png
set output "argsinh.png"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key left bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [-4:4]
plot [-4:4] sinh(x) w l ls 1 title "sinh x", log(x+sqrt(x**2+1)) w l ls 2 title "argsinh x", x w l ls 3
