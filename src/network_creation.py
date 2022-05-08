import networkx as nx
import music21 as m21
import matplotlib.pyplot as plt


def create_network(fn_list):
    score = get_full_score(fn_list)
    G = nx.DiGraph()

    nodeSet = []
    edgeSet = []
    prev = None
    for note in score:
        note_label = get_note_label(note)
        if note_label not in nodeSet:
            G.add_node(note_label, inbound=1)
            nodeSet.append(note_label)
        elif note_label in nodeSet:
            G.nodes[note_label]['inbound'] += 1
        if prev is not None:
            if (prev, note_label) in edgeSet:
                G[prev][note_label]['weight'] += 1
            else:
                G.add_edge(prev, note_label, weight=1)
                edgeSet.append((prev, note_label))
        prev = note_label
    return G


def xml_to_list(xml):
    xml_data = m21.converter.parse(xml)
    score = []
    for part in xml_data.parts:
        for note in part.recurse().notesAndRests:
            if note.isRest:
                duration = note.quarterLength
                score.append([-1, duration])
            else:
                duration = note.quarterLength
                pitch = note.nameWithOctave
                score.append([pitch, duration])
    return score


def get_full_score(fn_list):
    score = []
    for fn in fn_list:
        score += xml_to_list(fn)
    return score


def get_note_label(note):
    """input is in the form of [<name of note with octave>, <duration>]
       returns the label that will be used in the network representation."""
    if note[0] == -1:
        note_label = "R/" + str(note[1])
    else:
        note_label = note[0] + "/" + str(note[1])
    return note_label


def draw_network(G, name):
    nx.write_gexf(G, "gephiFiles/" + name + ".gexf")
    nx.draw(G, with_labels=True)
    plt.show()
