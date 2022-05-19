import networkx as nx
import music21 as m21
import os.path


class Graph:
    def __init__(self, genre="", all_notes=[], G=nx.DiGraph()):
        self.genre = genre
        self.all_notes = all_notes
        self.G = G
        self.path = "./gexfFiles/" + self.genre + ".gexf"

    def save_graph(self):
        nx.write_gexf(self.G, self.path)

    def read_existing_graph(self):
        self.G = nx.read_gexf(self.path)

    def is_graph_created(self):
        return os.path.exists(self.path)

    def get_full_score_for_genre(self):
        self.all_notes = score_for_genre(self.genre)

    def generate(self):
        self.G = nx.DiGraph()

        nodeSet = []
        edgeSet = []
        prev = None
        for note in self.all_notes:
            if self.genre == "":
                note_label = note
            else:
                note_label = get_note_label(note)
            if note_label not in nodeSet:
                self.G.add_node(note_label, inbound=1)
                nodeSet.append(note_label)
            elif note_label in nodeSet:
                self.G.nodes[note_label]['inbound'] += 1
            if prev is not None:
                if (prev, note_label) in edgeSet:
                    self.G[prev][note_label]['weight'] += 1
                else:
                    self.G.add_edge(prev, note_label, weight=1)
                    edgeSet.append((prev, note_label))
            prev = note_label


def score_for_genre(genre):
    """
    :param genre: String. Must be "classical", "romantic", "jazz", "pop"
    :return: list of Strings of notes in the selected pieces from the genre specified.
    """
    if genre == 'classical':
        clas1 = "./scoreData/classical/beethoven-pianoQuartetNo3.xml"
        clas2 = "./scoreData/classical/haydn-hobXVI35.xml"
        clas3 = "./scoreData/classical/mozart-k545-theme1.xml"
        return get_full_score_from_xml([clas1, clas2, clas3])
    elif genre == 'romantic':
        rom1 = "./scoreData/romantic/brahms-op77.xml"
        rom2 = "./scoreData/romantic/chopin-op33no2.xml"
        rom3 = "./scoreData/romantic/tchaikovsky-op35.xml"
        return get_full_score_from_xml([rom1, rom2, rom3])
    elif genre == 'jazz':
        jazz1 = "./scoreData/jazz/ellington-inASentimentalMood.xml"
        jazz2 = "./scoreData/jazz/monk-straight,NoChaser.xml"
        jazz3 = "./scoreData/jazz/monk-wellYouNeedn't.xml"
        jazz4 = "./scoreData/jazz/porter-iLoveYou.xml"
        return get_full_score_from_xml([jazz1, jazz2, jazz3, jazz4])
    # pop
    pop1 = "./scoreData/pop/rihanna-stay.xml"
    pop2 = "./scoreData/pop/brunoMars-whenIWasYourMan.xml"
    pop3 = "./scoreData/pop/billyJoel-pianoMan.xml"
    return get_full_score_from_xml([pop1, pop2, pop3])


def get_full_score_from_xml(fn_list):
    """
    :param fn_list: list of paths of the xml files containing information about the selected pieces.
    :return: list of lists ([<name of note with octave>, <duration>]) of notes in the selected pieces from the genre specified.
    """
    score = []
    for fn in fn_list:
        score += xml_to_list(fn)
    return score


def xml_to_list(xml):
    """
    :param xml: the path to an xml file. Specifically, a musicxml file.
    :return: the list of lists ([<name of note with octave>, <duration>]) of the notes of the piece in the xml file.
    """
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


def get_note_label(note):
    """
    :param note: list [<name of note with octave>, <duration>]
    :return: String "<name of note with octave>-<duration>"
    """
    if note[0] == -1:
        note_label = "R-" + str(note[1])
    else:
        if '-' in note[0]:
            note[0] = note[0].replace('-', '')
        note_label = note[0] + "-" + str(note[1])
    return note_label
