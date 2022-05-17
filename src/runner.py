from src import network_creation as nc, melody_generator as mg
import random
import os.path


def main():
    G = create_network_for_genre("genre")
    melodies = iteration(G, 1)
    return melodies


def create_melodies(genre, iteration_num):
    G = create_network_for_genre(genre)
    return iteration(G, iteration_num)


def create_network_for_genre(genre):
    if genre == 'classical':
        clas1 = "./scoreData/classical/beethoven-pianoQuartetNo3.xml"
        clas2 = "./scoreData/classical/haydn-hobXVI35.xml"
        clas3 = "./scoreData/classical/mozart-k545-theme1.xml"
        clas_list = [clas1, clas2, clas3]
        clas_G = nc.create_network(clas_list)
        nc.save_network(clas_G, genre)
        return clas_G
    elif genre == 'romantic':
        rom1 = "./scoreData/romantic/brahms-op77.xml"
        rom2 = "./scoreData/romantic/chopin-op33no2.xml"
        rom3 = "./scoreData/romantic/tchaikovsky-op35.xml"
        rom_list = [rom1, rom2, rom3]
        rom_G = nc.create_network(rom_list)
        nc.save_network(rom_G, genre)
    elif genre == 'jazz':
        jazz1 = "./scoreData/jazz/ellington-inASentimentalMood.xml"
        jazz2 = "./scoreData/jazz/monk-straight,NoChaser.xml"
        jazz3 = "./scoreData/jazz/monk-wellYouNeedn't.xml"
        jazz4 = "./scoreData/jazz/porter-iLoveYou.xml"
        jazz_list = [jazz1, jazz2, jazz3, jazz4]
        jazz_G = nc.create_network(jazz_list)
        nc.save_network(jazz_G, genre)
        return jazz_G
    # pop
    pop1 = "./scoreData/pop/rihanna-stay.xml"
    pop2 = "./scoreData/pop/brunoMars-whenIWasYourMan.xml"
    pop3 = "./scoreData/pop/billyJoel-pianoMan.xml"
    pop_list = [pop1, pop2, pop3]
    pop_G = nc.create_network(pop_list)
    nc.save_network(pop_G, genre)
    return pop_G


def iteration(G, iteration_num):
    melodies = []
    melodies_path = []
    folder_path = "./media/iteration-" + str(iteration_num) + "/"
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    for i in range(5):
        length = random.randint(16, 24)
        melody = mg.generate_melody(G, length)
        melodies.append(melody)
        path = folder_path + str((i + 1)) + ".wav"
        mg.save_melody(melody, path)
        melodies_path.append(path)
    mg.save_labels(melodies, folder_path)
    return melodies_path


