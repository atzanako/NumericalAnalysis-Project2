import numpy as np
import math


def polynomial2(company, x):
    a = np.zeros([10, 3], dtype=float)
    b = np.zeros([10, 1], dtype=float)

    for i in range(10):
        a[i][0] = 1
        a[i][1] = x[i]
        a[i][2] = math.pow(x[i], 2)
        b[i] = company[i]

    AT = a.transpose()
    a_new = np.dot(AT, a)
    b_new = np.dot(AT, b)
    solution = np.linalg.solve(a_new, b_new)
    return solution


def polynomial3(company, x):
    a = np.zeros([10, 4], dtype=float)
    b = np.zeros([10, 1], dtype=float)

    for i in range(10):
        a[i][0] = 1
        a[i][1] = x[i]
        a[i][2] = math.pow(x[i], 2)
        a[i][3] = math.pow(x[i], 3)
        b[i] = company[i]

    AT = a.transpose()
    a_new = np.dot(AT, a)
    b_new = np.dot(AT, b)
    solution = np.linalg.solve(a_new, b_new)
    return solution


def polynomial4(company, x):
    a = np.zeros([10, 5], dtype=float)
    b = np.zeros([10, 1], dtype=float)

    for i in range(10):
        a[i][0] = 1
        a[i][1] = x[i]
        a[i][2] = math.pow(x[i], 2)
        a[i][3] = math.pow(x[i], 3)
        a[i][4] = math.pow(x[i], 4)
        b[i] = company[i]

    AT = a.transpose()
    a_new = np.dot(AT, a)
    b_new = np.dot(AT, b)
    solution = np.linalg.solve(a_new, b_new)
    return solution


# Ημέρα γενεθλίων 12/12/2019
nextS = 12  # 10η μέρα είναι τα γενέθλια άρα 11η είναι η επόμενη συνεδρίαση (13/12/2019)
fifthS = 16  # και η έτσι η 5η συνδράση αντιστοιχεί στο νούμερο 16 (19/12/2019)

OPAP = [10.96, 11.16, 11.07, 10.9, 11, 11.02, 11, 10.93, 11.05, 11.48]
DEH = [3.202, 3.234, 3.29, 3.26, 3.33, 3.296, 3.278, 3.244, 3.296, 3.49]

x = np.zeros([10, 1], dtype=float)
j = 1
for i in range(10):
    x[i] = j
    j = j + 1

# Πολυώνυμο 2ου βαθμού
# ΟPAP

OPAP_sol_p2 = polynomial2(OPAP, x)
OPAP_solFirstDay_p2 = OPAP_sol_p2[0] + OPAP_sol_p2[1]*nextS + OPAP_sol_p2[2] * math.pow(nextS, 2)
OPAP_solFifthDay_p2 = OPAP_sol_p2[0] + OPAP_sol_p2[1]*fifthS + OPAP_sol_p2[2] * math.pow(fifthS, 2)
print("Η πρόβλεψη για την επόμενη συνεδρίαση του ΟΠΑΠ (13/12/2019) με πολυώνυμο 2ου βαθμού είναι: " +
      str(OPAP_solFirstDay_p2))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (19/12/2019) του ΟΠΑΠ με πολυώνυμο 2ου βαθμού είναι: " +
      str(OPAP_solFifthDay_p2))
print("\n")

# DEH

DEH_sol_p2 = polynomial2(DEH, x)
DEH_solFirstDay_p2 = DEH_sol_p2[0] + DEH_sol_p2[1]*nextS + DEH_sol_p2[2] * math.pow(nextS, 2)
DEH_solFifthDay_p2 = DEH_sol_p2[0] + DEH_sol_p2[1]*fifthS + DEH_sol_p2[2] * math.pow(fifthS, 2)
print("Η πρόβλεψη για την επόμενη συνεδρίαση της ΔΕΗ (13/12/2019) με πολυώνυμο 2ου βαθμού είναι: " +
      str(DEH_solFirstDay_p2))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (19/12/2019) της ΔΕΗ με πολυώνυμο 2ου βαθμού είναι: " +
      str(DEH_solFifthDay_p2))
print("\n\n")

# Πολυώνυμο 3ου βαθμού
# ΟPAP

OPAP_sol_p3 = polynomial3(OPAP, x)
OPAP_solFirstDay_p3 = OPAP_sol_p3[0] + OPAP_sol_p3[1]*nextS + OPAP_sol_p3[2] * math.pow(nextS, 2) + OPAP_sol_p3[3] *\
                      math.pow(nextS, 3)
OPAP_solFifthDay_p3 = OPAP_sol_p3[0] + OPAP_sol_p3[1]*fifthS + OPAP_sol_p3[2] * math.pow(fifthS, 2) + OPAP_sol_p3[3] *\
                      math.pow(fifthS, 3)
print("Η πρόβλεψη για την επόμενη συνεδρίαση του ΟΠΑΠ (13/12/2019) με πολυώνυμο 3ου βαθμού είναι: " +
      str(OPAP_solFirstDay_p3))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (17/12/2019) του ΟΠΑΠ με πολυώνυμο 3ου βαθμού είναι: " +
      str(OPAP_solFifthDay_p3))
print("\n")

# DEH

DEH_sol_p3 = polynomial3(DEH, x)
DEH_solFirstDay_p3 = DEH_sol_p3[0] + DEH_sol_p3[1]*nextS + DEH_sol_p3[2] * math.pow(nextS, 2) + DEH_sol_p3[3] *\
                     math.pow(nextS, 3)
DEH_solFifthDay_p3 = DEH_sol_p3[0] + DEH_sol_p3[1]*fifthS + DEH_sol_p3[2] * math.pow(fifthS, 2) + DEH_sol_p3[3] *\
                     math.pow(fifthS, 3)
print("Η πρόβλεψη για την επόμενη συνεδρίαση της ΔΕΗ (13/12/2019) με πολυώνυμο 3ου βαθμού είναι: " +
      str(DEH_solFirstDay_p3))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (19/12/2019) της ΔΕΗ με πολυώνυμο 3ου βαθμού είναι: " +
      str(DEH_solFifthDay_p3))
print("\n\n")

# Πολυώνυμο 4ου βαθμού
# ΟPAP

OPAP_sol_p4 = polynomial4(OPAP, x)
OPAP_solFirstDay_p4 = OPAP_sol_p4[0] + OPAP_sol_p4[1]*nextS + OPAP_sol_p4[2] * math.pow(nextS, 2) + OPAP_sol_p4[3] *\
                      math.pow(nextS, 3) + OPAP_sol_p4[4] * math.pow(nextS, 4)
OPAP_solFifthDay_p4 = OPAP_sol_p4[0] + OPAP_sol_p4[1]*fifthS + OPAP_sol_p4[2] * math.pow(fifthS, 2) + OPAP_sol_p4[3] *\
                      math.pow(fifthS, 3) + OPAP_sol_p4[4] * math.pow(fifthS, 4)
print("Η πρόβλεψη για την επόμενη συνεδρίαση του ΟΠΑΠ (13/12/2019) με πολυώνυμο 4ου βαθμού είναι: " +
      str(OPAP_solFirstDay_p4))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (17/12/2019) του ΟΠΑΠ με πολυώνυμο 4ου βαθμού είναι: " +
      str(OPAP_solFifthDay_p4))
print("\n")

# DEH

DEH_sol_p4 = polynomial4(DEH, x)
DEH_solFirstDay_p4 = DEH_sol_p4[0] + DEH_sol_p4[1]*nextS + DEH_sol_p4[2] * math.pow(nextS, 2) + DEH_sol_p4[3] *\
                     math.pow(nextS, 3) + DEH_sol_p4[4] * math.pow(nextS, 4)
DEH_solFifthDay_p4 = DEH_sol_p4[0] + DEH_sol_p4[1]*fifthS + DEH_sol_p4[2] * math.pow(fifthS, 2) + DEH_sol_p4[3] * \
                     math.pow(fifthS, 3) + DEH_sol_p4[4] * math.pow(fifthS, 4)
print("Η πρόβλεψη για την επόμενη συνεδρίαση της ΔΕΗ (13/12/2019) με πολυώνυμο 4ου βαθμού είναι: " +
      str(DEH_solFirstDay_p4))
print("Η πρόβλεψη για 5 συνεδριάσεις μετά (19/12/2019) της ΔΕΗ με πολυώνυμο 4ου βαθμού είναι: " +
      str(DEH_solFifthDay_p4))

