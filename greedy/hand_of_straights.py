from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sort by increasing then
        # Loop: Grab the first 'groupSize' elements that are consecutive

        if (groupSize == 1): return True

        hand.sort(key = lambda x: x)
        hand_list = list()
        hand_len = len(hand)

        # While there are more cards left
        while hand_len > 0:
            # Pop first element
            search = 0
            curr = hand.pop(0)
            hand_len -= 1
            # Pop off next groupSize - 1 elements
            for i in range(groupSize - 1):
                while(hand_len > 0 and search < hand_len and hand[search] != curr + 1):
                    search+=1
                if search == hand_len: return False
                curr = hand.pop(search)
                hand_len -= 1
                if hand_len == 0: return True
        return False