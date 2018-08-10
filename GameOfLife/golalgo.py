# An der Loesung dieser Aufgabe waren folgende Personen beteiligt:
# Chernysh Kateryna
# Dudyka Maria-Theresia
import random

def simple_gol(ant_array):
    # Ersetzen Sie bitte die foldenden Zeilen durch Ihre Loesung von Aufgabenteil a)
    # ant_array[0][0] = [0, 0, 0]  # Pixel links oben schwarz
    # ant_array[0][1] = [0, 0, 255]  # Pixel rechts daneben blau
    # ant_array[1][0] = [255, 0, 0]  # Pixel darunter rot
    new_ant_array = []
    for i in range(len(ant_array)):
        new_cell = []
        for j in range(len(ant_array[i])):
            neighbors = ant_neighbors_count(ant_array, i, j)
            if (neighbors == 2) and ant_array[i][j] == [0, 0, 0] or neighbors == 3:
                new_cell.append([0, 0, 0])
            else:
                new_cell.append([255, 255, 255])
        new_ant_array.append(new_cell)
    return new_ant_array


def ant_neighbors_count(ant_array, x, y):
    count = 0
    ant_cell = [255, 255, 255]

    for i in range(3):
        for j in range(3):
            if ((x - i + 1 >= 0 and y - j + 1 >= 0) and (
                    x - i + 1 < len(ant_array) and y - j + 1 < len(
                    ant_array[0]))) and ant_array[x-i+1][y-j+1] != ant_cell: # check if the cell is black
                if not ((x - i + 1) == x and (y - j + 1) == y):  # check if the cell is the actual ant
                        count = count + 1  # count the neighbours
    return count




def multicolor_ants(ant_array):
    # Ersetzen Sie bitte die foldenden Zeilen durch Ihre Loesung von Aufgabenteil b)
    # ant_array[0][0] = [0, 0, 0]  # Pixel links oben schwarz
    new_ant_array = []
    white = [255,255,255]
    for i in range(len(ant_array)):
        new_cell = []
        for j in range(len(ant_array[i])):
            neighbors = ant_neighbors_count(ant_array, i, j)
            if (neighbors == 2 or neighbors == 3) and ant_array[i][j] == white:  #finding ants  1,2,3,4 = stay 2 or 3 = new
                new_cell.append(random.choice([(255, 0, 0),
                  (0, 255, 255),
                  (0, 0, 255)]))
            elif(neighbors > 4 or neighbors < 1):
                new_cell.append(white)
            else:
                new_cell.append(ant_array[i][j])
        new_ant_array.append(new_cell)
    return new_ant_array

