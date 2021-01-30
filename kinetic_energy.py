# a task:  kinetic energy

# main function
def main():
    mass = float(input('Please, enter the value for mass (kg): '))
    velocity = float(input('Please, enter the value for velocity (m/s): '))
    KE = kinetic_energy(mass, velocity)
    print('\nThe kinetic energy =', format(KE, '.2f'), 'joules ')


# kinetic_energy function
def kinetic_energy(mass, velocity):
    KE = 0.5 * mass * (velocity ** 2)
    return KE


# call main function
main()
