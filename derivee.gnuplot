reset
set terminal postscript enhanced color
set output "derivee.ps"
#set yrange [0:5]
set size square
set grid
set style line 1 lt 1 lw 1 pt 1 linecolor rgb "red"
set style line 2 lt 1 lw 1 pt 1 linecolor rgb "blue"
set yzeroaxis lt -1
set xzeroaxis lt -1
coef1=-0.5-2*(2-10*(2)**0.5)/(10-2**0.5)**2
coef2=2**(-0.5)
plot [0.1:5] 1/x-(x**2-2)/(x-10) w l ls 1 title "", coef1*(x-2**0.5)+coef2 w l ls 2 title ""
