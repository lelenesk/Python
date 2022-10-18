import random

if __name__ == '__main__':

    def decrypter(faked_letter, mode_setter):
        twist_number = random.randint(1, 4)
        if mode_setter == 0:
            if twist_number == 1:
                modified_file.append(faked_letter.replace(faked_letter, "l"))
            elif twist_number == 2:
                modified_file.append(faked_letter.replace(faked_letter, "z"))
            elif twist_number == 3:
                modified_file.append(faked_letter.replace(faked_letter, "s"))
            else:
                modified_file.append(faked_letter.replace(faked_letter, "b"))
        elif mode_setter == 1:
            if twist_number == 1:
                modified_file.append(faked_letter.replace(faked_letter, "i"))
            elif twist_number == 2:
                modified_file.append(faked_letter.replace(faked_letter, "u"))
            elif twist_number == 3:
                modified_file.append(faked_letter.replace(faked_letter, "e"))
            else:
                modified_file.append(faked_letter.replace(faked_letter, "o"))
        elif mode_setter == 2:
            if twist_number == 1:
                modified_file.append(faked_letter.replace(faked_letter, "6"))
            elif twist_number == 2:
                modified_file.append(faked_letter.replace(faked_letter, "2"))
            elif twist_number == 3:
                modified_file.append(faked_letter.replace(faked_letter, "8"))
            else:
                modified_file.append(faked_letter.replace(faked_letter, "4"))
        else:
            if twist_number == 1:
                modified_file.append(faked_letter.replace(faked_letter, "L"))
            elif twist_number == 2:
                modified_file.append(faked_letter.replace(faked_letter, "T"))
            elif twist_number == 3:
                modified_file.append(faked_letter.replace(faked_letter, "F"))
            else:
                modified_file.append(faked_letter.replace(faked_letter, "C"))
        return faked_letter

    file_name = "about_me"
    original_file = open(f"input/{file_name}.txt", "r", encoding="utf-8")
    modified_file = []

    try:
        end_file = open(f"output/{file_name}.txt", "x", encoding="utf-8")
        for row in original_file:
            for letter in row:
                if letter in ("l", "s", "t", "r", "v", "d", "k", "g", "w", "x", "m", "h"):
                    setter = 0
                    letter = decrypter(letter, setter)
                elif letter in ("a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"):
                    setter = 1
                    letter = decrypter(letter, setter)
                elif letter in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    setter = 2
                    letter = decrypter(letter, setter)
                elif letter in ("T", "A", "M", "K", "Ó", "Z", "S", "I"):
                    setter = 3
                    letter = decrypter(letter, setter)
                else:
                    modified_file.append(letter)

        end_text = "".join(modified_file)
        end_file.write(end_text)
        end_file.close()
    except:
        print("ezt a fájlt már átkonvertáltad, nézd meg az output mappát")








