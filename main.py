import network_creation as nc

def main():
    create_network_for_era()


def create_network_for_era():
    # pop
    pop1 = "scoreData/pop/rihanna-stay.xml"
    pop2 = "scoreData/pop/brunoMars-whenIWasYourMan.xml"
    pop3 = "scoreData/pop/billyJoel-pianoMan.xml"
    pop_list = [pop1, pop2, pop3]
    pop_g = nc.create_network(pop_list)
    nc.draw_network(pop_g, "pop")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

