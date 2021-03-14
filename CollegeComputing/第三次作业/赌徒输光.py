import random
def coin_normal(players, rounds):
    ########## Begin ##########
    i= 0
    a = 0
    while i <= players-1:
        ii = 0
        d = 10
        while ii <= rounds-1 and d > 0:
            d = d-1
            p = random.random()
            if p >= 0.5:
                d = d+2
            elif p < 0.5:
                d = d
            ii = ii+1
        if d > 10:
            a = a+1
        i = i+1
    return a/players
    ########### End ###########
def coin_battle(persons, rounds):
    ########## Begin ##########
    i= 0
    a = 0
    while i <= persons-1:
        ii = 0
        d1 = 10 #赌徒
        d2 = 10 #庄家
        while ii <= rounds-1 and d1 > 0 and d2 > 0:
            d1 = d1-1
            d2 = d2-1
            p = random.random()
            if p >= 0.5:
                d1 = d1+2
            elif p < 0.5:
                d2 = d2+1
            ii = ii+1
        if d1 > 10:
            a = a+1
        i = i+1
    return a/persons
    ########### End ###########
def coin_commission(persons, rounds, cms):
    ########## Begin ##########
    i= 0
    a = 0
    while i <= persons-1:
        ii = 0
        d1 = 10 #赌徒
        d2 = 10 #庄家
        while ii <= rounds-1 and d1 > 0 and d2 > 0:
            d1 = d1-1
            d2 = d2-1
            p = random.random()
            if p >= 0.5:
                d1 = d1+2
                d2 = d2+cms*1
                d1 = d1-cms*1
            elif p < 0.5:
                d2 = d2+1
            ii = ii+1
        if d1 > 10:
            a = a+1
        i = i+1
    return a/persons
    ########### End ###########
def atest_coin_game(persons, rounds, cms):
    random.seed(0)
    print('赌徒人数:%d\t赌博轮数:%d\t抽点比例:%g' % (persons, rounds, cms))
    print('抛硬币游戏(庄家赌本无限制)的赌徒胜率:%g' % coin_normal(persons, rounds))
    print('抛硬币游戏(对赌)的赌徒胜率:%g' % coin_battle(persons, rounds))
    print('抛硬币游戏(庄家抽点)的赌徒胜率:%g' % coin_commission(persons, rounds, cms))
atest_coin_game(1000, 1000,0.02)