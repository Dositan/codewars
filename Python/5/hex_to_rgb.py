
def hex_string_to_RGB(hx):
    return {
        "r": int(hx[1: 3], 16), "g": int(hx[3: 5], 16), "b": int(hx[5: 7], 16)
    }


assert hex_string_to_RGB("#ff4000") == {"r": 255, "g": 64, "b": 0}
