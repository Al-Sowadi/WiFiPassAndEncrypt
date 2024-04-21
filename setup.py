import random
from cx_Freeze import setup, Executable

# Generate a random number
r1 = random.randint(-100000, 100000)

# Write the random number to a file
with open("main.py", "a", encoding="utf-8") as file:
    file.write("\nvar = " + str(r1))
    file.write("\nprint(var)\n")

# Specify options for the build process
options = {
    'build_exe': {
        'packages': ['idna'],
    },
}

# Create an executable
executables = [Executable("main.py", base=None)]

# Setup parameters for the build
setup(
    name="Wifi",
    options=options,
    version="1.0.0",
    description='Wifi Password',
    executables=executables
)
