from synthesizer import Writer, Synthesizer, Waveform
import random
import numpy as np


def generate_melody(G, length):
    nodes_w_weights = dict(G.nodes(data="inbound"))
    first_note = get_first_note(nodes_w_weights)
    melody_labels = [first_note]

    adj_view = dict(G.adj)
    note = first_note

    for i in range(length):
        melody_labels.append(note)
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


def save_melody(melody_labels, path):
    waves = []
    writer = Writer()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    for label in melody_labels:
        labels = label.split("/")
        note = [labels[0]][0]
        time = float(labels[1])
        if note[0] == 'R':
            waves.extend(synthesizer.generate_constant_wave(0, time))
        else:
            waves.extend(synthesizer.generate_constant_wave(note, time))
    writer.write_wave(path, np.array(waves))

def save_labels(melodies, folder_path):
    path = folder_path + "melodies.txt"
    with open(path, "w") as f:
        for melody in melodies:
            line = " "
            line = line.join(melody)
            f.write(line)
            f.write("\n")
