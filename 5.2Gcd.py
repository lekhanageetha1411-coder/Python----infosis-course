def calc_gcd(Varx, Vary):
    while(Vary):
        Varx, Vary = Vary, Varx % Vary
    return Varx


def calc_lcm(Varx, Vary):
    VarLCM = (Varx * Vary) // calc_gcd(Varx, Vary)
    return VarLCM


Varno1 = int(input("Enter the first number: "))
Varno2 = int(input("Enter the second number: "))

print("The L.C.M is", calc_lcm(Varno1, Varno2))
