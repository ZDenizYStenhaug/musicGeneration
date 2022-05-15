from src import network_creation as nc, melody_generator as mg
import random
import os.path


def main():
    G = create_network_for_era()
    melodies = iteration(G, 1)
    return melodies


def create_network_for_era():
    # pop
    pop1 = "scoreData/pop/rihanna-stay.xml"
    pop2 = "scoreData/pop/brunoMars-whenIWasYourMan.xml"
    pop3 = "scoreData/pop/billyJoel-pianoMan.xml"
    pop_list = [pop1, pop2, pop3]
    pop_g = nc.create_network(pop_list)
    return pop_g


def iteration(G, iteration_num):
    melodies = []
    folder_path = "./media/iteration-" + str(iteration_num) + "/"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    for i in range(5):
        length = random.randint(16, 24)
        melody = mg.generate_melody(G, length)
        melodies.append(melody)
        path = folder_path + str((i + 1)) + ".wav"
        mg.save_melody(melody, path)
    mg.save_labels(melodies, folder_path)
    return melodies


main()
