from src import melody_generator as mg
import random
import os.path
from src.GraphGen import Graph


def create_melodies(genre, iteration_num, ratings=[]):
    """
    :param genre: the genre of the melody to be produced. Can be 'Classical', 'Romantic', 'Jazz', 'Pop'.
    :param iteration_num: the number of the iteration
    :param ratings: a list of 5 ints
    :return:
    """
    original_G = Graph(genre=genre)
    original_G.get_full_score_for_genre()
    original_G.generate()

    if iteration_num == 1:
        return iteration(original_G.G, iteration_num)
    else:
        new_G = create_graph_for_iteration(iteration_num, ratings, original_G)
        melodies_path = iteration(new_G.G, iteration_num)
        return melodies_path


def create_graph_for_iteration(iteration_num, ratings, original_G):
    # chose the melodies from previous generation
    previous_melodies_path = "./media/iteration-" + str(iteration_num - 1) + "/melodies.txt"
    previous_melodies = read_melodies_from_file(previous_melodies_path)
    chosen_melodies = []
    ratings = list(map(float, ratings))
    for i in range(4):
        selected_melody = random.choices(previous_melodies, weights=ratings)[0]
        index = previous_melodies.index(selected_melody)
        ratings.pop(index)
        previous_melodies.pop(index)
        chosen_melodies.append(selected_melody)
    # add a new melody from the original graph
    chosen_melodies.append(mg.generate_melody(original_G.G))
    # create a new network from these melodies
    all_melodies = []
    for m in chosen_melodies:
        all_melodies += m
    newG = Graph(all_notes=all_melodies)
    newG.generate()
    return newG


def read_melodies_from_file(path):
    with open(path) as f:
        melodies = []
        for line in f:
            line = line[:-1]
            melodies.append(line.split(" "))
    return melodies


def iteration(G, iteration_num):
    melodies = []
    melodies_path = []
    folder_path = "./media/iteration-" + str(iteration_num) + "/"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    for i in range(5):
        melody = mg.generate_melody(G)
        melodies.append(melody)
        path = folder_path + str((i + 1)) + ".wav"
        mg.save_melody_as_wav(melody, path)
        melodies_path.append(path)
    mg.save_labels(melodies, folder_path)
    return melodies_path
