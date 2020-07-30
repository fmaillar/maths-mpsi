reset
set terminal png
set output "courbepolaire.png"
set grid
set xzeroaxis 
set yzeroaxis 
set xtics axis
set ytics axis
set noborder
set size ratio 1/2.5
set style line 1 lt 1 lw 1 pt 1 linecolor rgb "red"
set polar
plot [0:pi] cos(t)+cos(3*t) w l ls 1 title ""