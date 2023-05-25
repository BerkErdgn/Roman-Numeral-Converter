
input = input("Roman numerals : ")

result = 0
input_of_len = len(input)

syllable_list = []
for i in range(len(input)):
    syllable_list.append(input[i])

b = ["A", "B", "E", "F", "G", "H", "J", "K", "N", "O", "P", "Q", "R", "S", "T", "U",  "W",  "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

if any(x in syllable_list for x in b):
    print("Please write correctly.")
else:
    for i in range(len(syllable_list)):
        a = syllable_list[i]

        if a == "I":
            position_of_super_number_I = i + 1
            if len(syllable_list) > position_of_super_number_I:
                if syllable_list[position_of_super_number_I] == "V" or syllable_list[position_of_super_number_I] == "X":
                    result -= 1
                else:
                    result += 1
            else:
                result += 1

        elif a == "V":
            result += 5

        elif a == "X":
            position_of_super_number_X = i + 1
            if len(syllable_list) > position_of_super_number_X:
                if syllable_list[position_of_super_number_X] == "L" or syllable_list[position_of_super_number_X] == "C":
                    result -= 10
                else:
                    result += 10
            else:
                result += 10

        elif a == "L":
            result += 50

        elif a == "C":
            position_of_super_number_C = i + 1
            if len(syllable_list) > position_of_super_number_C:
                if syllable_list[position_of_super_number_C] == "D" or syllable_list[position_of_super_number_C] == "M":
                    result -= 100
                else:
                    result += 100
            else:
                result += 100

        elif a == "D":
            result += 500

        elif a == "M":
            result += 1000

    print("----------")
    print(result)





