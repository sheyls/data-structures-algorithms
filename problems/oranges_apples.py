def countApplesAndOranges1(s, t, a, b, apples, oranges):
    a_on_house = 0
    for apple in apples:
        if s <= a + apple <= t:
            a_on_house += 1
    
    o_on_house = 0
    for orange in oranges:
        if s <= b + orange <= t:
            o_on_house += 1

    print(a_on_house)
    print(o_on_house)


def countApplesAndOranges2(s, t, a, b, apples, oranges):
    a_on_house = sum(1 for i in apples if s <= a + i <= t)
    o_on_house = sum(1 for i in oranges if s <= b + i <= t)
    
    print(a_on_house)
    print(o_on_house)

# O(n + m) time complexity where n and m are the lengths of apples and oranges lists respectively
# O(1) space complexity