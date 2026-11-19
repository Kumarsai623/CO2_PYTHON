def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


def is_valid(reg):

    if len(reg) != 9 and len(reg) != 10:
        return False

    # Check state code
    if not reg[0:2].isalpha():
        return False

    # Check district code
    if not reg[2:4].isdigit():
        return False

    # Check series and final digits
    if len(reg) == 9:
        if not reg[4:5].isalpha():
            return False
        if not reg[5:9].isdigit():
            return False

    elif len(reg) == 10:
        if not reg[4:6].isalpha():
            return False
        if not reg[6:10].isdigit():
            return False

    return True


def format_number(reg):

    if not is_valid(reg):
        return "Invalid Number"

    if len(reg) == 9:
        return (reg[0:2] + " " + reg[2:4] + " " +
                reg[4:5] + " " + reg[5:9])

    else:
        return (reg[0:2] + " " + reg[2:4] + " " +
                reg[4:6] + " " + reg[6:10])


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "AP 39 C 5678",
    "MH 12 XY 9876"
]

for raw in numbers:

    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", format_number(reg), "VALID")
    else:
        print(raw, "->", reg, "INVALID")
