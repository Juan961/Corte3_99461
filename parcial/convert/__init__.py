hex_table_let = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


hex_table_num = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def dec2bin(dec:int):
    bin_list = []

    last_num = dec

    for _ in range(100):
        if last_num <= 0:
            break

        bin_num = last_num % 2
        last_num = last_num // 2
        bin_list.insert(0, str(bin_num))

    return int("".join(bin_list))


def dec2hex(dec:int):
    hex_list = []

    last_num = dec

    for _ in range(100):
        if last_num <= 0:
            break

        hex_num = last_num % 16

        if hex_num >= 10:
            hex_list.insert(0, hex_table_num[hex_num])
            last_num = last_num // 16

        else:
            last_num = last_num // 16
            hex_list.insert(0, str(hex_num))

    return "".join(hex_list)


def bin2dec(bin:int):
    sum_values = 0

    last_index = len(str(bin))

    for num in str(bin):
        last_index -= 1

        sum_values += int( num ) * ( 2 ** last_index )

    return sum_values


def hex2dec(hex:str):
    sum_values = 0

    last_index = len(hex)

    for num in hex:
        last_index -= 1

        if hex_table_let.get(num) != None:
            sum_values += hex_table_let.get(num) * ( 16 ** last_index )

        else:   
            sum_values += int(num) * ( 16 ** last_index )

    return sum_values


if __name__ == "__main__":
    assert dec2bin(77) == 1001101
    assert dec2hex(23123) == "5A53"
    assert bin2dec(110101) == 53
    assert hex2dec("C92A") == 51498
