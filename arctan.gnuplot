reset
set terminal png
set output "arctan.png"
set size square
set grid
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set key right bottom
set yzeroaxis lt -1
set xzeroaxis lt -1
set yrange [-4:4]
set xrange [-4:4]
#set size ratio -1

f(x) = x<=-pi/2 ? 0/0:\
x <=pi/2 ? tan(x):\
0/0

plot [-5:5] atan(x) w l ls 1 title "arctan x", f(x) w l ls 2 title "tan x", x w l ls 3
