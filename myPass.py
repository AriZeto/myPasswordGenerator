# Name: Ariel Zeto
# Project: MyPasswordGenerator
# Version 0.1.0
# Designed for CS361

# Import library and functionality for CLI GUI and rich-content display.
import typer
from rich import print
from rich.table import Table
from rich.console import Console

# Import library and functionality for secure content.
import secrets

# Import to access ascii content.
import string

# Define variables that contain all digits, letters, and special characters.
digitCharacters = string.digits
letterCharacters = string.ascii_letters
specialCharacters = string.punctuation


# Define string variable that contains all digits, letters, and special characters.
accessibleCharacters = specialCharacters + letterCharacters + digitCharacters

app = typer.Typer()

# Define boolean to determine if user is in generator functionality.
isInGenerator = False

# Welcome Screen commands columns
welcomeScreen = Table(title="Startup commands:")
welcomeScreen.add_column("Command", justify="center", style="cyan", no_wrap=True)
welcomeScreen.add_column("Description", justify="left", style="magenta")

# Welcome Screen commands rows
welcomeScreen.add_row("generate", "Generates requested password.")
welcomeScreen.add_row("docs", "View the documentation of the application.")
welcomeScreen.add_row("quit", "Quits the application.")

# Password commands columns
passwordTable = Table(title="Password strength commands:")
passwordTable.add_column("Command", justify="center", style="cyan", no_wrap=True)
passwordTable.add_column("Description", justify="left", style="magenta")

# Password commands rows
passwordTable.add_row("easy", "Generates an easy password (not recommended). (Password length is 8 chars, all lowercase, one number)")
passwordTable.add_row("\nmedium", "\nGenerates a medium password (not recommended). (Password length is 10 chars, all lowercase, one uppercase, one number).")
passwordTable.add_row("\nstrong", "\nGenerates a strong password. (Password length is 16 chars, mix of uppercase and lowercase, few numbers, special character).")
passwordTable.add_row("\nvery strong", "\nGenerates a very strong password. (Password length is 20 chars, mix of uppercase, lowercase, numbers, and special characters).")
passwordTable.add_row("\nspecify", "\nThe user can specify length, as well as how many characters of each type they want.")
passwordTable.add_row("\nask", "\nWhy does a secure password matter? Find out by using this command.")

# Basic commands columns
table = Table(title="myPassGenerator Commands:")
table.add_column("Command", justify="center", style="cyan", no_wrap=True)
table.add_column("Description", justify="left", style="magenta")

# Basic commands rows
table.add_row("get_help", "Provides help with using the software.")
table.add_row("docs", "Provides user documentation (you are on this page)")
table.add_row("faqs", "Provides FAQS to user.")
table.add_row("generate", "Prompt to begin generating password")
table.add_row("quit", "Close the program")

# Advanced commands columns
advScreen = Table(title="Startup commands:")
advScreen.add_column("Command", justify="center", style="cyan", no_wrap=True)
advScreen.add_column("Description", justify="left", style="magenta")

# Advanced commands rows
advScreen.add_row("undo", "Undoes a prior command in the password generator screen")
advScreen.add_row("redo", "Redoes a command in the password generator screen")
advScreen.add_row("credits", "Displays credits for the application")
advScreen.add_row("save", "Saves password to a text file after password is generated.")

# For displaying the table to the console.
console = Console()

# Splash / Welcome Screen. Set as default command.
@app.callback(invoke_without_command=True)
def home():
    print("\nWelcome to [bold green]myPassGenerator![/bold green] "
          "\nThis password generator application is designed to be simple to use"
          " and design a secure password for your applications. To get started, we have provided some basic, most common commands.\n")

    # Print table welcome screen commands.
    console.print(welcomeScreen)

    print("\nTo get started, type 'python mypass.py' along with a command. For example, 'python mypass docs', "
          "which will take you to the documents page.\n")

@app.command()
def close():
    exit()

# Command to see frequently asked questions.
@app.command()
def faqs():
    print("\nWelcome to the [bold green]Frequently Asked Questions[/bold green] page for myPassGenerator! "
          "Down below you’ll find common frequently asked questions.")
    print("\n[bold red]Who is this application for?:[/bold red]")
    print("This application is designed to be simple and easy to use. The application’s design methods "
          "were implemented with standard heuristic design techniques. We welcome anyone to use "
          "myPassGenerator, including a range of people with low computer confidence, all the way "
          "through those with high confidence.")

    print("\n[bold red]Why a command-line interface?:[/bold red]")
    print("There are numerous password generators with graphical user interfaces. "
          "While these are great, they can often times be bogged down with a lot of on-screen elements"
          " that may hinder the experience. This application is designed to be as simple and intuitive,"
          " thus it was decided that the application would remain command-line based. "
          "However, a web-application is not out of question.")

    print("\n[bold red]Why should a password be secure?:[/bold red]")
    print("A password should be secure due to the concern of password cracking. "
          "In modern days, your digital footprint contains a lot of weight. This includes banking,"
          " social media, message board discussion, college access, shopping,"
          " and confidential information. Without a secure password (and updating it frequently),"
          " you expose risk to your digital footprint – and can compromise others.")

    print("\n[bold red]How can a password be considered 'strong'?:[/bold red]")
    print("Strong passwords typically consist of letters, numbers, a special character, "
          "and are longer (think 15 to 30 characters).\n")

    # Ask if user would like to return to splash screen.
    userPrompt = input("Would you like to return to the home screen?: Type command 'y' to return, 'n' otherwise. ").lower()
    if userPrompt == "y" or userPrompt == "yes":
        home()

# Command to see  documentation for basic user commands.
@app.command()
def docs():
    print("\n[bold red]'myPassGenerator' v.0.1.0[/bold red]")
    print("[bold green]Copyright Ariel Zeto, 2023.[/bold green]")
    print('[bold green]Designed for: OSU - CS361 - Software Engineering.[/bold green] \n')
    print("[bold blue]Hello![/bold blue] Welcome to the Documentation page.")
    print("Within this page, you will come across the documentation of this application.")
    print("Here is a short list of basic user commands: \n")

    # Displays the table of commands available to the user.
    console.print(table)

    # Remind user that advanced options are available.
    print("Reminder: Advanced command options: Try the command 'advDocs' if you'd like to see advanced user commands.\n")

    # Ask if user would like to go to password generator screen.
    passPrompt = input("Would you like to try generating a password: Type command 'y' to return, 'n' otherwise. ").lower()
    if passPrompt == "y" or passPrompt == "yes":
        generate()

# Command to see  documentation for advanced user commands.
@app.command()
def advDocs():
    print('\n These commands are typically used within the application "generate" functionality. Use responsibly. \n')

    # Displays the advanced table of commands that are available.
    console.print(advScreen)

    # Ask if user would like to go to password generator screen.
    passPrompt = input(f"\nWould you like to try generating a password: Type command 'y' to return, 'n' otherwise. ").lower()
    if passPrompt == "y" or passPrompt == "yes":
        generate()

# Command to begin generating password.
@app.command()
def generate():

    # Sets condition for running while loop.
    isInGenerator = True

    print("\n You have selected the option to generate a secure password. "
          "You will be asked a prompt for how strong you wish the PASSWORD STRENGTH to be.")

    # For displaying the table to the console.
    print("\n")
    console.print(passwordTable)

    while isInGenerator is True:

        # Define variable length for password length.
        passwordLength = 0

        getInput = input("\nWhat strength do you want your new password to be?: ").lower()

        if getInput is type(float) or getInput is type(int):
            print("Invalid input. Please enter in a valid password generator command. ")

        if getInput == "easy":

            # Redefine the length of the password.
            passwordLength = 8

            print(f"\nYou have selected AN '{getInput}' password. Generating password…: \n")

            while True:

                # Define empty string to contain password.
                userPassword = ""

                for i in range(passwordLength):
                    userPassword += ''.join(secrets.choice(accessibleCharacters))

                # Define easy password.
                if sum(char in digitCharacters for char in userPassword) == 1 and userPassword.islower() and sum(char in specialCharacters for char in userPassword) == 0:
                    break

            print(f"{userPassword}\n")

            isInGenerator = False

        elif getInput == "medium":

            # Redefine the length of the password.
            passwordLength = 10

            print(f"\nYou have selected AN '{getInput}' password. Generating password…: \n")

            while True:

                # Define empty string to contain password.
                userPassword = ""

                for i in range(passwordLength):
                    userPassword += ''.join(secrets.choice(accessibleCharacters))

                # Define medium password.
                if sum(char in digitCharacters for char in userPassword) == 1 and sum(char.isupper() for char in userPassword) >= 4 and sum(char in specialCharacters for char in userPassword) == 0:
                    break

            print(f"{userPassword}\n")

            isInGenerator = False

        # This is the default option if user responds with typical 'yes' or 'y' prompt (default behavior with command line).
        elif getInput == "strong" or getInput == "y" or getInput == "yes":

            # Redefine the length of the password.
            passwordLength = 16

            print(
                f"\nYou have selected AN '{getInput}' password. Generating password…: \n")

            while True:

                # Define empty string to contain password.
                userPassword = ""

                for i in range(passwordLength):
                    userPassword += ''.join(
                        secrets.choice(accessibleCharacters))

                # Define hard password.
                if sum(char in digitCharacters for char in userPassword) > 3 and sum(char in specialCharacters for char in userPassword) == 1 and sum(char in specialCharacters for char in userPassword) == 1:
                    break

            print(f"{userPassword}\n")

            isInGenerator = False

        elif getInput == "ask":
            print("FILL THIS OUT")

            isInGenerator = False

        elif getInput == "very strong":

            # Redefine the length of the password.
            passwordLength = 20

            print(f"\nYou have selected AN '{getInput}' password. Generating password…: \n")

            while True:

                # Define empty string to contain password.
                userPassword = ""

                for i in range(passwordLength):
                    userPassword += ''.join(secrets.choice(accessibleCharacters))

                # Define hard password.
                if sum(char in digitCharacters for char in userPassword) > 5 and sum(char in specialCharacters for char in userPassword) > 4:
                    break

            print(f"{userPassword}\n")

            isInGenerator = False

        elif getInput == "specify":

            # Redefine the length of the password.
            passwordLength = int(input("\nEnter in the number of characters you want the password to be. "))
            if passwordLength < 8 or passwordLength > 50:
                print("This program does not support password lengths longer than 50 characters. Please choose a number between 8 and 50.")

            # Define other characteristics for user prompt.
            isUpperCase = False
            isSpecialChars = False

            getUpperCond = input("\nDo you want your password to contain uppercase characters?: Submit 'y', otherwise press any key. ").lower()
            if getUpperCond == 'y' or getUpperCond == 'yes:':
                isUpperCase = True

            getSpecialCond = input("\nDo you want your password to contain special characters?: Submit 'y', otherwise press any key. ").lower()
            if getSpecialCond == 'y' or getSpecialCond == 'yes:':
                isSpecialChars = True

            while True:

                # Define empty string to contain password.
                userPassword = ""

                for i in range(passwordLength):
                    userPassword += ''.join(secrets.choice(accessibleCharacters))

                # If password contains uppercase and special characters.
                if isUpperCase is True and isSpecialChars is True:
                    # Define special case password.
                    if sum(char in digitCharacters for char in userPassword) >= 3 and any(char.isupper() for char in userPassword) and any(
                            char in specialCharacters for char in userPassword):
                        break

                # If password contains uppercase but not special characters.
                if isUpperCase is True and isSpecialChars is not True:
                    # Define special case password.
                    if sum(char in digitCharacters for char in userPassword) >= 3 and any(char.isupper() for char in userPassword) and sum(
                            char in specialCharacters for char in userPassword) == 0:
                        break

                # If password doesn't contain uppercase characters but includes special characters.
                if isUpperCase is not True and isSpecialChars is True:
                    # Define special case password.
                    if sum(char in digitCharacters for char in userPassword) >= 3 and sum(char.isupper() for char in userPassword) == 0 and any(
                            char in specialCharacters for char in userPassword):
                        break

                if isUpperCase is not True and isSpecialChars is not True:
                    if sum(char in digitCharacters for char in userPassword) >= 3 and sum(char.isupper() for char in userPassword) == 0 and sum(
                            char in specialCharacters for char in userPassword) == 0:
                        break

            print(f"\n{userPassword}\n")

            askForUsername = input(f"Would you like to associate this password to a username?: Type 'y' to continue, otherwise any other key: ").lower()
            if askForUsername == 'y' or askForUsername == 'yes':
                storeUsername = input(f"\nPlease enter in the associated username: ")

            askToSave = input(f"\nWould you like to export this password?: Type 'y' to continue, otherwise any other key: ").lower()
            if askToSave == 'y' or askToSave == 'yes':
                print("\nFile saved in specified directory.\n")

            isInGenerator = False

            askGoHome = input(f"Would you like to return home? Type 'y' to continue, otherwise any other key: ").lower()
            if askGoHome == 'y' or askGoHome == 'yes':
                home()

        else:
            print("Invalid input. Please enter in a valid password generator command. ")


if __name__ == "__main__":
    app()