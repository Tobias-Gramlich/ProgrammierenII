import random as rnd

Field_Player = [["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"]]
Field_Enemy_Hidden = [["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"]]
Field_Enemy_Shown = [["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"]]

def start():
    print("Herzlich Willkommen zu unserem Schiffe versenken")
    print("~ bedeutet unbekanntes Gewässer")
    print("X bedeutet ein Schiff an diesem Ort")
    print("O bedeutet Gewässer ohne Schiff")
    print("# bedeutet eine getroffene Stelle")
    print(" ")
    
    return input("Welchen Modus wollen sie spielen?(1 = Mensch vs. Computer / 2 = Mensch vs. Mensch) -> ")

def draw():
    print()
    print("Eigenes Gewässer:              Gegnerisches Gewässer:")
    print(" ", " A", " B", " C", " D", " E", " F", " G", " H","      ", " A", " B", " C", " D", " E", " F", " G", " H")
    for i in range(8):
        print(i + 1,end = "")
        for j in range(8):
            print(" ",Field_Player[i][j],end = "")
        print("     ",i + 1,end = "")
            
        for j in range(0,8):
            print(" ", Field_Enemy_Shown[i][j], end ="")
        print()
    print()

def place_ship_player():
    print("Platzieren sie ihre Schiffe indem sie hintereinander die Felder angeben, auf welchen die Schiffe sein sollen (Bsp. A1,A2,A3,A4)")

    while True:
        ship_two_array = input("Wo soll das Zweier Schiff sein?->").split(",")
        if ship_checker(ship_two_array, 2):
            Field_Player[int(ship_two_array[0][1]) - 1][ord(ship_two_array[0][0]) - 65] = "X"
            Field_Player[int(ship_two_array[1][1]) - 1][ord(ship_two_array[1][0]) - 65] = "X"
            break

    while True:
        ship_three_array = input("Wo soll das Dreier Schiff sein?->").split(",")
        if ship_checker(ship_three_array, 3):
            Field_Player[int(ship_three_array[0][1]) - 1][ord(ship_three_array[0][0]) - 65] = "X"
            Field_Player[int(ship_three_array[1][1]) - 1][ord(ship_three_array[1][0]) - 65] = "X"
            Field_Player[int(ship_three_array[2][1]) - 1][ord(ship_three_array[2][0]) - 65] = "X"
            break

    while True:
        ship_four_array = input("Wo soll das Vierer Schiff sein?->").split(",")
        if ship_checker(ship_four_array, 4):
            Field_Player[int(ship_four_array[0][1]) - 1][ord(ship_four_array[0][0]) - 65] = "X"
            Field_Player[int(ship_four_array[1][1]) - 1][ord(ship_four_array[1][0]) - 65] = "X"
            Field_Player[int(ship_four_array[2][1]) - 1][ord(ship_four_array[2][0]) - 65] = "X"
            Field_Player[int(ship_four_array[3][1]) - 1][ord(ship_four_array[3][0]) - 65] = "X"
            break

    while True:
        ship_five_array = input("Wo soll das Fünfer Schiff sein?->").split(",")
        if ship_checker(ship_five_array, 5):
            Field_Player[int(ship_five_array[0][1]) - 1][ord(ship_five_array[0][0]) - 65] = "X"
            Field_Player[int(ship_five_array[1][1]) - 1][ord(ship_five_array[1][0]) - 65] = "X"
            Field_Player[int(ship_five_array[2][1]) - 1][ord(ship_five_array[2][0]) - 65] = "X"
            Field_Player[int(ship_five_array[3][1]) - 1][ord(ship_five_array[3][0]) - 65] = "X"
            Field_Player[int(ship_five_array[4][1]) - 1][ord(ship_five_array[4][0]) - 65] = "X"
            break

def place_ship_enemy_random():

    while True:
        if rnd.randint(1, 2) == 1:
            ship_enemy_random_letter = rnd.randint(0, 7)
            ship_enemy_random_number = rnd.randint(0, 6)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] = "X"
                break
        else:
            ship_enemy_random_letter = rnd.randint(0, 6)
            ship_enemy_random_number = rnd.randint(0, 7)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] = "X"
                break

    while True:
        if rnd.randint(1, 2) == 1:
            ship_enemy_random_letter = rnd.randint(1, 7)
            ship_enemy_random_number = rnd.randint(1, 5)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] = "X"
                break

        else:
            ship_enemy_random_letter = rnd.randint(1, 5)
            ship_enemy_random_number = rnd.randint(1, 7)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] = "X"
                break

    while True:
        if rnd.randint(1, 2) == 1:
            ship_enemy_random_letter = rnd.randint(1, 7)
            ship_enemy_random_number = rnd.randint(1, 4)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 3] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 3] = "X"
                break

        else:
            ship_enemy_random_letter = rnd.randint(1, 4)
            ship_enemy_random_number = rnd.randint(1, 7)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 3][ship_enemy_random_number] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 3][ship_enemy_random_number] = "X"
                break

    while True:
        if rnd.randint(1, 2) == 1:
            ship_enemy_random_letter = rnd.randint(1, 7)
            ship_enemy_random_number = rnd.randint(1, 3)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 3] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 4] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 1] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 2] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 3] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number + 4] = "X"
                break

        else:
            ship_enemy_random_letter = rnd.randint(1, 3)
            ship_enemy_random_number = rnd.randint(1, 7)

            if (Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 3][ship_enemy_random_number] == "~"
                    and Field_Enemy_Hidden[ship_enemy_random_letter + 4][ship_enemy_random_number] == "~"):

                Field_Enemy_Hidden[ship_enemy_random_letter][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 1][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 2][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 3][ship_enemy_random_number] = "X"
                Field_Enemy_Hidden[ship_enemy_random_letter + 4][ship_enemy_random_number] = "X"
                break

def play_game():
    player_hit_counter = 0
    enemy_hit_counter = 0
    while True:
        draw()
        #TODO: Versenktmeldung
        while True:
            shot_player = input("Wohin möchten sie schießen? ->")

            if Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] == "~":
                print("Daneben...")
                Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] = "O"
                Field_Enemy_Shown[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] = "O"
                break

            elif Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] == "X":
                print("Getroffen!")
                Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] = "#"
                Field_Enemy_Shown[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] = "#"
                player_hit_counter += 1
                break

            elif Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] == "O" or Field_Enemy_Hidden[int(shot_player[1]) - 1][ord(shot_player[0]) - 65] == "#":
                print("Du hast bereits dieses Feld angeschossen")

            else:
                print("Ungültige Eingabe")

        while True:
            shot_enemy_coord_one = rnd.randint(0, 7)
            shot_enemy_coord_two = rnd.randint(0, 7)

            if Field_Player[shot_enemy_coord_one][shot_enemy_coord_two] == "~":
                print("Gegner hat verfehlt!")
                Field_Player[shot_enemy_coord_one][shot_enemy_coord_two] = "O"
                break

            elif Field_Player[shot_enemy_coord_one][shot_enemy_coord_two] == "X":
                print("Gegner hat getroffen!")
                Field_Player[shot_enemy_coord_one][shot_enemy_coord_two] = "#"
                enemy_hit_counter += 1
                break

        if player_hit_counter == 14:
            print("Du hast gewonnen!")
            break
        elif enemy_hit_counter == 14:
            print("Gegner hat gewonnen!")
            break

def ship_checker(array, expected_length):
    checked_counter = 0
    # ship_amount_checker(array, length):
    if len(array) > expected_length:
        print("Bitte geben sie weniger Felder an")
    elif len(array) < expected_length:
        print("Bitte geben sie mehr Felder an")
    else:
        checked_counter += 1

    # ship_placement_checker(array):
    array_first_letter = ord(array[0][0])
    array_first_number = int(array[0][1])
    counter = 0

    # TODO: Andere Reihenfolge auch ermöglichen

    if array[0][0] == array[1][0]:
        for fields in array:
            if ord(fields[0]) == array_first_letter and int(fields[1]) in range(array_first_number - len(array),
                                                                                array_first_number + len(array)):
                counter += 1

    elif array[0][1] == array[1][1]:
        for fields in array:
            if int(fields[1]) == array_first_number and ord(fields[0]) in range(array_first_letter - len(array),
                                                                                array_first_letter + len(array)):
                counter += 1

    if counter == len(array):
        checked_counter += 1
    else:
        print("Ungültige Positionierung")

    # ship_overlap_checker(array):
    counter = 0
    for fields in array:
        if Field_Player[int(fields[1]) - 1][ord(fields[0]) - 65] == "~":
            counter += 1
    if counter == len(array):
        checked_counter += 1
    else:
        print("Schiffe dürfen nicht aufeinander liegen")

    # ship_double_checker(array):
    checked_fields = []
    success = True
    for fields in array:
        if fields in checked_fields:
            print("Felder doppelt angeben ist verboten")
            success = False
        else:
            checked_fields.append(fields)

    if success:
        checked_counter += 1

    if checked_counter == 4:
        return True
    else:
        return False

while True:
    
    Game_Mode = start()
    draw()

    place_ship_player()
    
    if Game_Mode != "0":
        place_ship_enemy_random()
        
    play_game()
    draw()

    if input("Noch eine Runde? (J/N) ->") == "J":
        
        Field_Player = [["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"] , ["~","~","~","~","~","~","~","~"]]
        Field_Enemy_Hidden = [["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"] , ["~", "~", "~", "~", "~", "~", "~", "~"]]

    else: break