import math


def methodos_trapeziou(a, b):  # η συνάρτηση δέχεται τα άκρα του διαστήματος, ο αριθμός των σημείων είναι 11
    upodiasthmata = 10
    euros = (b-a) / upodiasthmata
    x = [0 for i in range(12)]
    for i in range(12):
        x[i] = a + i * euros

    y = [0 for i in range(12)]
    for i in range(12):
        y[i] = math.sin(x[i])

    sum = 0
    for i in range(1, 9):
        sum = sum + y[i]

    trapezio = round((b-a) / (2*upodiasthmata) * (y[0] + y[11] + 2*sum), 7)

    m = [0 for i in range(12)]
    for i in range(12):
        m[i] = -1 * math.sin(x[i])

    max_element = 0
    for i in range(1, 12):
        if math.fabs(m[i]) > math.fabs(m[max_element]):
            max_element = i

    error = round(math.fabs(math.pow(b-a, 3) / (12*math.pow(upodiasthmata, 2)) * m[max_element]), 7)
    print("Το αποτέλεσμα του ολοκληρώματος της συνάρτησης sinx με τη μέθοδο τραπεζίου είναι: " + str(trapezio))
    return error


def Simpson(a, b):  # η συνάρτηση δέχεται τα άκρα του διαστήματος, ο αριθμός των σημείων είναι 11
    upodiasthmata = 10
    euros = (b-a) / upodiasthmata
    x = [0 for i in range(12)]
    for i in range(12):
        x[i] = a + i * euros

    y = [0 for i in range(12)]
    for i in range(12):
        y[i] = math.sin(x[i])

    sum1 = 0
    for i in range(1, 5):   # upodiastimata/2 -1
        sum1 = sum1 + y[2*i]

    sum2 = 0
    for i in range(1, 6):   # upodiastimata/2
        sum2 = sum2 + y[2*i-1]

    integral_simpson = round(((b-a) / (3*upodiasthmata)) * (y[0] + y[11] + 2*sum1 + 4*sum2), 7)

    m = [0 for i in range(12)]
    for i in range(12):
        m[i] = math.sin(x[i])

    max_element = 0
    for i in range(1, 12):
        if math.fabs(m[i]) > math.fabs(m[max_element]):
            max_element = max_element + 1

    error = math.fabs(math.pow(b-a, 5) / (180*math.pow(upodiasthmata, 4)) * m[max_element])

    print("Το αποτέλεσμα του ολοκληρώματος της συνάρτησης sinx με τη μέθοδο Simpson είναι: " + str(integral_simpson))
    return error


print("Το σφάλμα που προκύπτει είναι: " + str(methodos_trapeziou(0, math.pi/2)))
print("Το σφάλμα που προκύπτει είναι: " + str(Simpson(0, math.pi/2)))
