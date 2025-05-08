def parse_colors(file_path):
    colors = []
    with open(file_path, 'r') as file:
        for line in file:
            color = line.strip()
            if is_valid_hex(color):
                colors.append(color)
            else:
                print(f"Invalid hex color: {color}")
    return colors

def is_valid_hex(color):
    if color.startswith('#') and len(color) == 7:
        try:
            int(color[1:], 16)
            return True
        except ValueError:
            return False
    return False