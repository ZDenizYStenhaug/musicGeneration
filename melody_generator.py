from time import sleep

from synthesizer import Player, Synthesizer, Waveform
import random

# TODO: walk the graph function. Must return a list of labels of notes to play.
def generate_melody(G, length):
    nodes_w_weights = dict(G.nodes(data="inbound"))
    first_note = get_first_note(nodes_w_weights)

    melody = [first_note]

    # edges_with_weights = G.edges.data("weight")
    adj_view = dict(G.adj)
    note = first_note
    for i in range(16):
        melody.append(note)
        note = get_next_note(adj_view[note])
    print(melody)
    play_melody(melody)


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


def play_melody(melody):
    player = Player()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    player.open_stream()

    for label in melody:
        print(label)
        labels = label.split("/")
        note = [labels[0]]
        time = float(labels[1])
        if note[0] == 'R':
            sleep(time)
        else:
            player.play_wave(synthesizer.generate_chord(note, time))
