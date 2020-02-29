#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################

VOTES = 100000
MEDIAN = VOTES/2
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}

MENTIONS = [
    "Excellent",
    "Très bien",
    "Bien",
    "Assez Bien",
    "Passable",
    "Insuffisant",
    "A rejeter"
]


def create_votes():
    return [
        {
            "hermione": random.randint(0, 1),
            "balou": random.randint(2, 4),
            "chuck-norris": random.randint(4, 6),
            "elsa": random.randint(3, 4),
            "gandalf": random.randint(5, 6),
            "beyonce": random.randint(0, 2)
        } for _ in range(0, VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################

############### CREATE ARRAY #####################


def results_hash(votes):
    """ Count votes per candidate and per mention
    Returns a dict of candidate names containing vote arrays.
    """
    candidates_results = {
        candidate: [0]*len(MENTIONS)
        for candidate in CANDIDATES.keys()
    }
    for vote in votes:
        for candidate, mention in vote.items():
            candidates_results[candidate][mention] += 1
    return candidates_results


##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()
    results = results_hash(votes)
    print(results)


if __name__ == '__main__':
    main()
