#BIM A+3
#Programming Asignment 3
#Cristian Rincon

#libraries
import math as mt

#Defined parameters
Mx=[]
My=[]
Dv=0
Sx=0
Sy=0
dix=0
diy=0
dxy=0

#Data input
n=int(input('Define number of sides of the polygon: '))

for n in range(1,n+1):
    print('')
    print(f'For point {n}')
    Cx=float(input('Define Coor. X: '))
    Cy=float(input('Define Coor. Y: '))
    Mx.append(Cx)
    My.append(Cy)

#Print table of coordinates
print('')
print('-'*60)
print(f"{' '*8}{'Point':17}{'Coor X':17}{'Coor Y':17}")
print('-'*60)

for n in range(1,n+1):
    print(f'{n:15.0f}{Mx[n-1]:15.2f}{My[n-1]:15.2f}')

for n in range(0,n-1):
    x0=Mx[n]
    x1=Mx[n+1]
    y0=My[n]
    y1=My[n+1]
    #Area Sumatory
    Ax= x1 + x0
    Ay= y1 - y0
    Dv= Dv + (Ax * Ay)
    #Static Moments of Inertia Sumatory
    px= x1 - x0
    Syx= (x1)**2 + (x1 * x0) + (x0)**2
    Syy= (y1)**2 + (y1 * y0) + (y0)**2
    Sx= Sx + (px * Syy)
    Sy= Sy + (Ay * Syx)
    #Moments of inertia from axes Sumatory
    pix=(x1)**3 + ((x1**2) * x0) + (x1 * (x0)**2) + (x0**3)
    piy=(y1)**3 + ((y1**2) * y0) + (y1 * (y0)**2) + (y0**3)
    dix= dix + (px * piy)
    diy= diy + (Ay * pix)
    dxy1=(3 * (x1)**2) + (2 * (x1) * (x0)) + (x0**2)
    dxy2=(3 * (x0)**2) + (2 * (x1) * (x0)) + (x1**2)
    dxy= dxy + Ay * (((y1 * dxy1)) + (y0 * dxy2))

#Section Properties
A= 0.5 * Dv
MSx= (-1/6) * Sx
MSy= (1/6) * Sy
Ix= (-1/12) * dix
Iy= (1/12) * diy
Ixy=(-1/24) * dxy
Xt=MSy/A
Yt=MSx/A
Ixt=Ix - ((Yt**2)*A)
Iyt=Iy - ((Xt**2)*A)
Ixyt=Ixy + (Xt * Yt * A) 

#Print Table of Section properties
print('')
print('Section Properties')
print('-'*60)
print(f'Ax:{A:20.2f}')
print(f'Sx:{MSx:20.2f}')
print(f'Sy:{MSy:20.2f}')
print(f'Ix:{Ix:20.2f}')
print(f'Iy:{Iy:20.2f}')
print(f'Ixy:{Ixy:19.2f}')
print(f'Xt:{Xt:20.2f}')
print(f'Yt:{Yt:20.2f}')
print(f'Ixt:{Ixt:19.2f}')
print(f'Iyt:{Iyt:19.2f}')
print(f'Ixyt:{Ixyt:18.2f}')
