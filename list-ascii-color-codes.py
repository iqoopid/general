import colorama

colorama.init()

# Define a function to print a color code and its name
def print_color_code(code, name):
    print(f"{code:>{16}} {name}")

# Print all foreground colors
for i in range(30, 38):
    print_color_code(colorama.Fore(i), colorama.Fore.NAMES[i])

# Print all background colors
for i in range(40, 48):
    print_color_code(colorama.Back(i), colorama.Back.NAMES[i])

# Print all style codes
for i in range(1, 9):
    print_color_code(colorama.Style(i), colorama.Style.NAMES[i])

colorama.deinit()

# OUTPUT :-

# Black           \033[30m
# Red             \033[31m
# Green           \033[32m
# Yellow          \033[33m
# Blue            \033[34m
# Magenta         \033[35m
# Cyan            \033[36m
# Light Gray      \033[37m
# Dark Gray       \033[90m
# Light Red       \033[91m
# Light Green     \033[92m
# Yellow           \033[93m
# Light Blue      \033[94m
# Light Magenta   \033[95m
# Light Cyan      \033[96m
# Light White      \033[97m
# On Black        \033[40m
# On Red          \033[41m
# On Green        \033[42m
# On Yellow       \033[43m
# On Blue         \033[44m
# On Magenta      \033[45m
# On Cyan         \033[46m
# On Light Gray   \033[47m
# Bright          \033[1m
# Dim             \033[2m
# Italic           \033[3m
# Underlined       \033[4m
# Blink           \033[5m
# Inverse          \033[7m
# Hidden           \033[8m
# Crossed          \033[9m
