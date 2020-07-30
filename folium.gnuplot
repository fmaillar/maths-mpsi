reset
set terminal png
set output "folium.png"
set grid
set noborder
set size 0.7,1
set style line 2 lt 1 lw 2 pt 2 linecolor rgb "red"
set style line 3 lt 0 lw 1 pt 1 linecolor rgb "blue"
set parametric
plot [-0.7:1] t/(1+t**3), t**2/(1+t**3) w l ls 2 title "", t**2/(1+t**3), t/(1+t**3) w l ls 2 title "", -t, t-0.333 w l ls 3 title ""
