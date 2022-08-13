import numpy as np
from math import pi, sqrt, sin



def suntelestes_lagrange(i, x, value):
    arithmitis = 1
    paranomastis = 1
    temp1 = 0
    temp2 = 0
    while temp1 < 9:
        if temp2 != i:
            arithmitis = arithmitis * (value - x[temp2])
            paranomastis = paranomastis * (x[i] - x[temp2])
            temp1 = temp1 + 1
        temp2 = temp2 + 1
    return arithmitis / paranomastis


def p(x, results, value):
    p = 0
    for i in range(10):
        p = p + results[i] * suntelestes_lagrange(i, x, value)
    return p


def least_square(A, x):
    l = len(A)
    A_new1 = np.zeros([l, 2])
    b = np.zeros([l, 1])

    for i in range(l):
        A_new1[i][0] = 1
        A_new1[i][1] = A[i][0]
        b[i] = A[i][1]

    AT = A_new1.transpose()
    A_new2 = np.dot(AT, A_new1)
    b_new = np.dot(AT, b)
    sol = np.linalg.solve(A_new2, b_new)
    y = np.zeros([len(x), 1])
    for i in range(len(x)):
        y[i] = sol[0] + sol[1] * x[i]
    return y


shmeia = [-pi, -5*pi/6, -3*pi/4, -pi/3, 0, pi/10, pi/6, pi/2, 2*pi/3, pi]
y = [0, -1/2, -sqrt(2)/2, -sqrt(3)/2, 0, (sqrt(5)-1)/4, 1/2, 1, sqrt(3)/2, 0]

pol_lagrange = [0 for i in range(10)]
for i in range(10):
    pol_lagrange[i] = p(shmeia, y, shmeia[i])

count1 = 0
A1 = np.zeros([10, 2])
for i in range(10):
    A1[count1][0] = shmeia[i]
    A1[count1][1] = y[i]
    count1 = count1 + 1

solution_least_square = least_square(A1, shmeia)

times_imitonou = [np.random.uniform(-pi, pi) for i in range(200)]
apotelesmata_timwn_imitonou = [0 for i in range(200)]
for i in range(200):
    apotelesmata_timwn_imitonou[i] = sin(times_imitonou[i])

count2 = 0
A2 = np.zeros([200, 2])
for i in range(200):
    A2[count2][0] = times_imitonou[i]
    A2[count2][1] = apotelesmata_timwn_imitonou[i]
    count2 = count2 + 1

y_leastsquare = least_square(A2, times_imitonou)
y_lagrange = [0 for i in range(200)]
for i in range(200):
    y_lagrange[i] = p(times_imitonou, apotelesmata_timwn_imitonou, times_imitonou[i])


sugkrisi_apotelesmatwn = np.zeros([10, 3])
for i in range(10):
    sugkrisi_apotelesmatwn[i][0] = y[i]
    sugkrisi_apotelesmatwn[i][1] = pol_lagrange[i]
    sugkrisi_apotelesmatwn[i][2] = solution_least_square[i]

print("   sin      Lagrange     Least Squares")
print(sugkrisi_apotelesmatwn)
