from tests.flow.flo import Flo

def test_for_cheating():
   Flo.test('tests/flow/cheat_and_fix.txt')

def test_for_zilch():
    Flo.test('tests/flow/zilch.txt')

def test_living_on_edge():
    Flo.test('tests/flow/living_on_the_edge.txt')

def test_hot_dices():
    Flo.test('tests/flow/hot_dice.txt')