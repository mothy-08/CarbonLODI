import os
from miscellaneous import AccountManager
import calculator

logo = '''
   ______           __                   __    ____  ____  ____
  / ____/___ ______/ /_  ____  ____     / /   / __ \/ __ \/  _/
 / /   / __ `/ ___/ __ \/ __ \/ __ \   / /   / / / / / / // /  
/ /___/ /_/ / /  / /_/ / /_/ / / / /  / /___/ /_/ / /_/ // /   
\____/\__,_/_/  /_.___/\____/_/ /_/  /_____/\____/_____/___/   

                                                               '''

main_menu = '''
                         Main Menu

                        1 - Register
                        2 - Login
                        0 - Exit
Response: '''

while True:  # Runs the Main Menu in loop
    os.system('cls')
    print(logo)
    choice = input(main_menu)
    print("")

    os.system('cls')  # Clear screen before processing user choice

    if choice == '1':
        current_user = AccountManager().register()
        calculator.CarbonEmission(current_user).housing_emissions()
        input("Press Enter to continue...")
    elif choice == '2':
        AccountManager().load_users()
        current_user = AccountManager().login()
        if current_user is None:
            input("Press Enter to continue...")
        else:
            calculator.CarbonEmission(current_user).housing_emissions()
            input("Press Enter to continue...")
        input("Press Enter to continue...")
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")