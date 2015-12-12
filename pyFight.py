import time
import random


class Fight:
    def __init__(self):
        self.players = 10               # total number of players
        self.player_health = 100        # max init health
        self.max_power = 20             # max init power
        self.min_power = 5              # min init power
        self.tpr = 5                    # turns per round
        self._std_wait = 0.05              # standard wait for output to be somewhat readable
        self.min_attack = 1             # if 0 allow misses
        self.show_eors = False          # show end-of-round stats
        self.show_battle = True         # shows each turn in each round

        self.player_attr = ["id", "health", "power", "name"]
        self.name_list = ["Keane", "Vance", "Gil", "Ray", "Brady", "Steven", "Marsden", "Xenos", "Brett", "Alfonso",
                          "Benedict", "Oscar", "Demetrius", "Abel", "Holmes", "Jermaine", "Yardley", "Moses", "Ezra",
                          "Amir", "Marshall", "Henry", "Kane", "Neil", "Ulric", "Keaton", "Jamal", "Hamilton", "Keefe",
                          "Thomas", "Marshall", "Flynn", "Macaulay", "Wyatt", "Perry", "Carter", "Lev", "Coby",
                          "Nissim", "Keefe", "Burton", "Lee", "Garth", "Garrett", "Melvin", "Deacon", "Slade", "Felix",
                          "Aquila", "Quentin", "Brock", "Damon", "Hashim", "Callum", "Honorato", "Ivan", "Austin",
                          "Alan", "Louis", "Hu", "Nigel", "Jacob", "Gavin", "Philip", "Thomas", "Barrett", "Dillon",
                          "Caesar", "Giacomo", "Logan", "Dieter", "Amal", "Vincent", "Valentine", "Alvin", "Fulton",
                          "Cole", "Price", "William", "Harper", "Cruz", "Jasper", "Felix", "Odysseus", "Caesar",
                          "Raymond", "Ray", "Charles", "Brady", "Porter", "Forrest", "Wade", "Vernon", "Hayden", "Gage",
                          "Randall", "Stuart", "Walter", "Berk", "Quamar"]

        self.player_list = [["a"]*len(self.player_attr) for g in range(self.players)]

        print "%d players" % self.players
        id = 0
        for pl in self.player_list:
            numb = random.randrange(0, len(self.name_list))
            name = self.name_list[numb]
            self.name_list.pop(numb)

            # todo: update this to be dynamic with value header names

            pl[0] = id
            pl[1] = self.player_health
            pl[2] = random.randrange(self.min_power, self.max_power)
            pl[3] = name

            id += 1

        for p in range(self.players):
            print "%s as entered the fight" % self.player_list[p][3]

        print "\n*** setup complete ***\n"
        time.sleep(self._std_wait)

    def fight(self):
        turn = self.tpr
        while True:
            # pick two players
            if len(self.player_list) == 1:
                print "%s has survived %d rounds to win the fight with %d health remaining." % (self.player_list[0][3],
                                                                                               turn - 1,
                                                                                               self.player_list[0][1])
                print "Game over."
                break
            else:
                _this_round = random.sample(self.player_list, 2)
                random.shuffle(_this_round)

                print ">>> Round %d Starting\n" % turn

                time.sleep(self._std_wait)

                for t in range(self.tpr):
                    _attack_power = random.randrange(self.min_attack,_this_round[0][2])
                    if self.show_battle:
                        print ">> %d - %s(%d) attacks %s(%d)" % (t+1,
                                                                 _this_round[0][3],
                                                                 _this_round[0][1],
                                                                 _this_round[1][3],
                                                                 _this_round[1][1])
                        if _attack_power == 0:
                            print ">>     %s misses" % (_this_round[0][3])
                        else:
                            print ">>     %s receives %d damage" % (_this_round[1][3],_attack_power)
                    _this_round[1][1] -= _attack_power
                    # player dies
                    if _this_round[1][1] <= 0:
                        print "%s is dead, long live %s" % (_this_round[1][3],_this_round[1][3])
                        self.player_list.remove(_this_round[1])
                        break
                    # end of turn tasks
                    if len(_this_round) == 1:
                        break
                    else:
                        _this_round.reverse()
                    time.sleep(self._std_wait)

                # end of round tasks

                if self.show_eors:
                    print ">>> ********************"
                    for i in self.player_list:
                        print ">>> %s" % i
                    print ">>> ********************"
                print "\n>>> Round Complete.\n"
                turn += 1
                time.sleep(self._std_wait)

if __name__ == "__main__":
    Fight().fight()
