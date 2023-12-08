f = open("inp", "r")

values = {
    '2' : 0,
    '3' : 1,
    '4' : 2,
    '5' : 3,
    '6' : 4,
    '7' : 5,
    '8' : 6,
    '9' : 7,
    'T' : 8,
    'J' : -1,
    'Q' : 10,
    'K' : 12,
    'A' : 13
}
def get_hand_type(hand):
    d = {}
    j = 0
    for card in hand:
        if card == 'J':
            j = j + 1
            continue
        if card in d:
            d[card] = d[card]+1
        else:
            d[card] = 1
    l = len(d)
    if j == 5:
        l = 1
        m = 0
    else:
        m = d[max(d, key=d.get)]
    m = m + j

    if l >= 4:
        return 5 - l
    if l == 3 and m == 2:
        return 2
    if m == 3:
        return 6 - l
    if l == 1:
        return 6
    return 5

def compare(hand1, hand2):
    i = 0
    while i < 5 and hand1[i] == hand2[i]:
        i = i + 1
    return values[hand1[i]] > values[hand2[i]]

def sort_same_type_hands(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            hand1 = arr[j]["hand"]
            hand2 = arr[j+1]["hand"]
            if compare(hand1, hand2):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped== False:
            break
    return arr

hands = [[], [], [], [],[], [], []]
for line in f:
    hand, bid = line.split()
    ind = get_hand_type(hand)
    hands[ind].append({'hand' : hand, 'bid' : bid})
hands = list(map(lambda x: sort_same_type_hands( x), hands))
flat_list = []
b = 1
sum = 0
for type in hands:
    for hand in type:
        sum = sum + int(hand["bid"]) * b
        b = b+1


print(sum)
