from synthesizer import Writer, Synthesizer, Waveform
import random
import numpy as np


def generate_melody(G):
    """
    :param G: directed graph
    :return: List of String that represents melody labels
    """
    length = random.randint(16, 24)
    nodes_w_weights = dict(G.nodes(data="inbound"))
    first_note = get_first_note(nodes_w_weights)
    melody_labels = [first_note]

    adj_view = dict(G.adj)
    note = first_note

    for i in range(length):
        melody_labels.append(note)
        neighbours = adj_view[note]
        if len(neighbours) == 0:
            note = get_first_note(nodes_w_weights)
        else:
            note = get_next_note(adj_view[note])
    return melody_labels


def get_next_note(neighbours):
    nodes = []
    weights = []
    for key in neighbours:
        nodes.append(key)
        weights.append(neighbours[key]['weight'])
    return random.choices(nodes, weights=weights)[0]


def get_first_note(nodes_w_weights):
    nodes = list(nodes_w_weights.keys())
    node_weights = list(nodes_w_weights.values())
    return random.choices(nodes, weights=node_weights)[0]


def save_melody_as_wav(melody_labels, path):
    """
    :param melody_labels: list of strings
    :param path: the path to save the wav file
    """
    waves = []
    writer = Writer()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    for label in melody_labels:
        labels = label.split("-")
        note = [labels[0]][0]
        time = labels[1]
        if note[0] == 'R':
            waves.extend(synthesizer.generate_constant_wave(0, time))
        else:
            if '/' in labels[1]:
                operands = labels[1].split('/')
                time = float(operands[0]) / float(operands[1])
            print("time: " + str(time) + "  note: " + str(note))
            waves.extend(synthesizer.generate_constant_wave(note, time))
    writer.write_wave(path, np.array(waves))


def save_labels(melodies, folder_path):
    """
    :param melodies: list of lists of melody labels.
    :param folder_path: the path to folder to save the melodies.txt file.
    """
    path = folder_path + "melodies.txt"
    with open(path, "w") as f:
        for melody in melodies:
            line = " "
            line = line.join(melody)
            f.write(line)
            f.write("\n")
