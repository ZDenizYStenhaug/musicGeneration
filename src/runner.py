from src import network_creation as nc, melody_generator as mg
from synthesizer import Writer, Synthesizer, Waveform
import numpy as np


def main():
    G = create_network_for_era()
    melody = mg.generate_melody(G, 16)
    return melody


def create_network_for_era():
    # pop
    pop1 = "scoreData/pop/rihanna-stay.xml"
    pop2 = "scoreData/pop/brunoMars-whenIWasYourMan.xml"
    pop3 = "scoreData/pop/billyJoel-pianoMan.xml"
    pop_list = [pop1, pop2, pop3]
    pop_g = nc.create_network(pop_list)
    # nc.draw_network(pop_g, "pop")
    return pop_g


main()
