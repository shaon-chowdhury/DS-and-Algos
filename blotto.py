import random
import operator
import numpy as np
import heapq
import gc

'''
Save only a set number of elements in a dictionary. Pop out items from the heap
which have the smallest total score (or in case of a tie, lowest number of wins)
'''
class OnlyKDict(object):

    def __init__(self, max_dict_size, key = lambda x: x):

        self.data = []
        self.dictionary = {}
        self.key = key
        self.max_dict_size = max_dict_size

    def push(self, item):

        heapq.heappush(self.data, (self.key(item),item))
        self.dictionary[item[0]] = item[1]
        if len(self.data) > self.max_dict_size:
            item = self.pop()
            self.dictionary.pop(item[0], None)

    def pop(self):

        return heapq.heappop(self.data)[1]

    def merge(self, only_k_dict):

        for key, value in only_k_dict.dictionary.iteritems():
            self.__setitem__(key, value)

        return self

    def __getitem__(self, key):

        return self.dictionary[key]

    def __setitem__(self, key, value):

        if self.dictionary.has_key(key):
            self.dictionary[key][0] += value[0]
            self.dictionary[key][1] += value[1]
            self.dictionary[key][2] += value[2]
        else:
            self.push((key, value))

'''
Obtain random arrays which add to a given total
Input:
- n (int): length of output arrays
- total (int): the specified total the random arrays sum to
- weighted (boolean) (default: True): generate unweighted/weighted arrays
Output:
Two arrays (list) representing strategies
'''
def constrained_sum_sample_nonneg(n, total, weighted=True):

    if weighted is True:
        array = np.arange(1, n + 1)*1.0
    else:
        array = np.ones(n)*1.0
    samp = np.random.multinomial(total, array/np.sum(array), size=2)
    return samp[0,:], samp[1,:]

'''
Score each strategy head-to-head for the Blotto game
Input:
- strategy 1, 2 (list): Two strategies (arrays) that are scored
Output:
- strategy1ScoreDiff, strategy2ScoreDiff (int): Head-to-head (int) scores for both
strategies
'''
def blottoGameScoring(strategy1, strategy2):

    p1score = p2score = 0
    n = len(strategy1)
    assert len(strategy1) == len(strategy2)

    for i in range(n):
        if strategy1[i] > 2*strategy2[i]:
            p1score += i + 1
        elif strategy2[i] > 2*strategy1[i]:
            p2score += i + 1

    strategy1ScoreDiff = p1score - p2score
    strategy2ScoreDiff = p2score - p1score

    return strategy1ScoreDiff, strategy2ScoreDiff

'''
Run simulations for the Blotto game by randomly generating strategies, scoring
these head-to-head and appending into a defined data structure (and pruning
strategies as required)
Input:
- totalSoldiers (int): Total number of soldiers each player can assign
- totalCastles (int): Total number of castles a player has to assign soldiers to
- numGames (int): Number of blotto games to run
- keepTopSets (int): Number of (top) strategies to keep in memory
- strategySetSource (OnlyKDict) (default: None): Read in previous blotto game
run results
- weighted (boolean) (default: True): To weight/unweight random array generation
Output:
- The total set of strategies saved in memory, their scores, number of games won
and number of games the strategy was played
'''
def blottoGameRun(totalSoldiers, totalCastles, numGames, keepTopSets, strategySetSource=None, weighted=True):

    if strategySetSource is not None:
        keepTopSets = int(np.sqrt(keepTopSets))
        numGames = 10**8

    strategySet = OnlyKDict(keepTopSets, lambda x:x[0][1] if x[0][1]==x[0][0] else x[0][0])

    if strategySetSource is not None:
        topKSets = dict(sorted(strategySetSource.dictionary.items(), key=operator.itemgetter(1), reverse=True)[:keepTopSets])
        for key, value in topKSets.items():
            strategySet.__setitem__(key, value)

    gameNum = 0
    strategy1, strategy2 = (), ()

    random_indices = None
    if strategySetSource is not None:
        try:
            random_indices = np.array(len(strategySet.dictionary)*np.random.random_sample((numGames, 2)), dtype=int)
        except MemoryError:
            print 'Memory Error'

    while gameNum < numGames:

        p1winner, p2winner, strategyGamesPlayed = 0, 0, 1

        if strategySetSource is None:
            strategy1, strategy2 = constrained_sum_sample_nonneg(totalCastles, totalSoldiers, weighted)
        else:
            if random_indices is not None:
                rand_index_1, rand_index_2 = random_indices[gameNum, 0], random_indices[gameNum, 1]
            else:
                random_indices = np.array(len(strategySet.dictionary)*np.random.random_sample((1, 2)), dtype=int)
                rand_index_1, rand_index_2 = random_indices[0][0], random_indices[0][1]

            for index, key_value_tuple in enumerate(strategySet.dictionary):

                if index == rand_index_1:
                   strategy1 = key_value_tuple
                if index == rand_index_2:
                   strategy2 = key_value_tuple

            random_indices = None

        strategy1ScoreDiff, strategy2ScoreDiff = blottoGameScoring(strategy1, strategy2)

        if (type(strategy1) or type(strategy2)) is not tuple:
            strategy1 = tuple(strategy1.tolist())
            strategy2 = tuple(strategy2.tolist())

        if strategy1ScoreDiff > 0:
            p1winner = 1
        if strategy2ScoreDiff > 0:
            p2winner = 1

        if strategy1 != strategy2:
            strategySet.__setitem__(strategy1, [strategy1ScoreDiff, p1winner, strategyGamesPlayed])
            strategySet.__setitem__(strategy2, [strategy2ScoreDiff, p2winner, strategyGamesPlayed])

        gameNum += 1

        if gameNum % (2*10**8) == 0:

            gc.collect()

    if strategySetSource is None:
        return strategySet
    else:
        return sorted(strategySet.dictionary.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == "__main__":

    totalSoldiers = 100
    totalCastles = 10
    numGames = 10**9
    keepTopSets = 2*10**7

    gameRunResults = blottoGameRun(totalSoldiers, totalCastles, numGames, keepTopSets)
    matchResults = blottoGameRun(totalSoldiers, totalCastles, numGames, keepTopSets, gameRunResults)
    sortedResults = sorted(matchResults.items(), key=operator.itemgetter(1), reverse=True)
    print matchResults[:20]
