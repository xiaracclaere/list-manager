#  |█'$ thank me later

# Older Style
def style1(options):
    r_option = " "
    for number, i in enumerate(options, start=1):
        r_option += f"{i}({number}) "
    return r_option

# Best Style
def style2(options):
    r_option = "|"
    for i in options:
        r_option += f" {i} |"
    return r_option

# New Style
def style3(options):
    r_option = "█"
    for i in options:
        r_option += f" {i} █"
    return r_option

# Bad Style
def style4(options):
    r_option = "'"
    for i in options:
        r_option += f" {i} '"
    return r_option

# Weird Style
def style5(options):
    r_option = "$"
    for i in options:
        r_option += f" {i} $"
    return r_option

# Create UI
def cui(style, options):
    ui = style(options)
    return ui