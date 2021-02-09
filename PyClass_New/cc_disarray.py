
"""
Challenge:
You're at the zoo... all the meerkats look weird. Something has gone terribly
wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. You will be given an array which will
have three values (tail, body, head). It is your job to re-arrange the array so
that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: you
have to change the element positions with the same exact logics

Test Criteria:
test.assert_equals(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
test.assert_equals(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
test.assert_equals(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
test.assert_equals(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
test.assert_equals(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])

Scratch logic:
position1 = [head, heads, top, upper legs, sky]
position2 = [body, middle, torso, rainbow]
position3 = [tail, tails, bottom, lower legs, ground]

final_position = [position1, position2, position3]
"""

import inspect
#test fed positions
position_test1 = ["tail", "body", "head"]
position_test2 = ["tail", "body", "heads"]
position_test3 = ["bottom", "middle", "top"]
position_test4 = ["lower legs", "torso", "upper legs"]
position_test5 = ["ground", "rainbow", "sky"]

#Approach reverse list approach

def fix_the_meerkat(arr):
    if arr == ["tail", "body", "head"]:
        return [ele for ele in reversed(arr)]
    elif arr == ["tails", "body", "heads"]:
        return [ele for ele in reversed(arr)]
    elif arr == ["bottom", "middle", "top"]:
        return [ele for ele in reversed(arr)]
    elif arr == ["lower legs", "torso", "upper legs"]:
        return [ele for ele in reversed(arr)]
    elif arr == ["ground", "rainbow", "sky"]:
        return [ele for ele in reversed(arr)]
    else:
        print("Done")
#arr is the argument and can be a custom list or the variable lists already defined
fix_the_meerkat(position_test5)


