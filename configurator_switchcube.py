from random import choice, randint

# Asking the client if he needs illumination
illum = input('Do you want illumination for your switch on the bike(yes or no)?\n')

# Creating list of options for the buttons
button_a_options = ['ABS', 'Fog Lights', 'Heated Grip', 'ACC Control', 'LED', 'ASC']
button_cd_options = ['Programing + MENU', 'TRIP + INFO', 'TRIP + SET', 'MENU', 'Windshield',
                     'Power OFF + Suspension']
button_ef_options = ['KLR LOCK + Heated seat', 'Favourites + R', 'DTC', 'Automatic Lights + MODE',
                     'A/M Transmission', 'Wipers + Tire Pressure']
range_motor_var = '8G6260'

# If client wants illum. we continue here, otherwise we go to "no" condition
if illum.lower() == 'yes':

    # Creating empty vars for attaching the client's choice
    but_a_label = ''
    but_cd_label = ''
    but_ef_label = ''

    while True:
        but_a = input('Do you need Button A(yes or no)?\n')

        if but_a.lower() == 'yes':
            but_a_label = choice(button_a_options)  # we spawn our choice from random
        else:
            but_a_label = 'N/A'


        but_cd = input('Do you need Button C+D(yes or no)?\n')  # continue with the rest of the buttons

        if but_cd.lower() == 'yes':
            but_cd_label = choice(button_cd_options)
        else:
            but_cd_label = 'N/A'


        but_ef = input('Do you need Button E+F(yes or no)?\n')

        if but_ef.lower() == 'yes':
            but_ef_label = choice(button_ef_options)
        else:
            but_ef_label = 'N/A'

        print(f'Your configuration until now is following:\t{but_a_label} --- {but_cd_label} --- {but_ef_label}\n')

        # We ask the customer if he likes this configuration
        statement = input('Are you happy with this configuration(yes or no)?\n')

        # If he is not happy with it, we iterate over and over again
        if statement.lower() == 'yes':
            break
        elif statement.lower() == 'no':
            continue

    while True:
        # Now we will run random choice for the motor option of the engine
        print('Your bike number will be:', end="")
        end_number = randint(1024, 1029)
        var_motor = range_motor_var + str(end_number)
        print(var_motor)

        # Now we choose a motor engine HP based on the previous choice of the motor option engine
        horse_power = 0
        if var_motor.endswith("1024"):
            horse_power = 166
        elif var_motor.endswith("1025"):
            horse_power = 200
        elif var_motor.endswith("1026"):
            horse_power = 235
        elif var_motor.endswith("1027"):
            horse_power = 275
        elif var_motor.endswith("1028"):
            horse_power = 333
        elif var_motor.endswith("1029"):
            horse_power = 1000

        print(f'\nYour motor will have an engine of {horse_power}hp.')
        print('If you are not happy with that engine, run again your engine choice')
        print('Should engine choice run again(yes or no)?')
        eng_choice = input()

        if eng_choice.lower() == 'yes':
            continue
        elif eng_choice.lower() == 'no':
            break

    print(f'Your final choice is --->\nEngine power with {horse_power}hp and extra options '
          f'--> {but_a_label} -- {but_cd_label} -- {but_ef_label} and it has illumination switch!')


elif illum.lower() == 'no':
    # Creating empty vars for attaching the client's choice
    but_a_label = ''
    but_cd_label = ''
    but_ef_label = ''

    while True:
        but_a = input('Do you need Button A(yes or no)?\n')

        if but_a.lower() == 'yes':
            but_a_label = choice(button_a_options)  # we spawn our choice from random
        else:
            but_a_label = 'N/A'


        but_cd = input('Do you need Button C+D(yes or no)?\n')  # continue with the rest of the buttons

        if but_cd.lower() == 'yes':
            but_cd_label = choice(button_cd_options)
        else:
            but_cd_label = 'N/A'


        but_ef = input('Do you need Button E+F(yes or no)?\n')

        if but_ef.lower() == 'yes':
            but_ef_label = choice(button_ef_options)
        else:
            but_ef_label = 'N/A'

        print(f'Your configuration until now is following:\t{but_a_label} --- {but_cd_label} --- {but_ef_label}\n')

        # We ask the customer if he likes this configuration
        statement = input('Are you happy with this configuration(yes or no)?\n')

        # If he is not happy with it, we iterate over and over again
        if statement.lower() == 'yes':
            break
        elif statement.lower() == 'no':
            continue

    while True:
        # Now we will run random choice for the motor option of the engine
        print('\nYour bike number will be:', end="")
        end_number = randint(1024, 1029)
        var_motor = range_motor_var + str(end_number)
        print(var_motor)

        # Now we choose a motor engine HP based on the previous choice of the motor option engine
        horse_power = 0
        if var_motor.endswith("1024"):
            horse_power = 166
        elif var_motor.endswith("1025"):
            horse_power = 200
        elif var_motor.endswith("1026"):
            horse_power = 235
        elif var_motor.endswith("1027"):
            horse_power = 275
        elif var_motor.endswith("1028"):
            horse_power = 333
        elif var_motor.endswith("1029"):
            horse_power = 1000

        print(f'\nYour motor will have an engine of {horse_power}hp.')
        print('If you are not happy with that engine, run again your engine choice')
        print('Should engine choice run again(yes or no)?')
        eng_choice = input()

        if eng_choice.lower() == 'yes':
            continue
        elif eng_choice.lower() == 'no':
            break

    print(f'Your final choice is --->\nEngine power with {horse_power}hp and extra options '
          f'--> {but_a_label} -- {but_cd_label} -- {but_ef_label} and it has no integrated illumination!')
