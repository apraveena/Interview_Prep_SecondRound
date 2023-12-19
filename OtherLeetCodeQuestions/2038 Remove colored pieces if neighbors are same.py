#JPMC JP Morgan Chase question
#Look at Solution1 for efficient answer
#Game winner

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        colors = list(colors)
        alice_turn = True
        while True:
            item_deleted = False
            if alice_turn:
                piece_to_remove = "A"
            else:
                piece_to_remove = "B"

            for i in range(1, len(colors) - 1):

                curr = colors[i]
                prev = colors[i - 1]
                nxt = colors[i + 1]

                if curr != piece_to_remove:
                    continue

                if curr == prev == nxt:
                    item_deleted = True
                    del colors[i - 1]
                    break

            if not item_deleted:
                return not alice_turn

            alice_turn = not alice_turn

class Solution1:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a > b
sln = Solution()
print(sln.winnerOfGame('AAABABB') == True) #Alice wins
print(sln.winnerOfGame('AAA') == True) #Alice wins
print(sln.winnerOfGame('BBB') == False) #Alice loses Bob wins
print(sln.winnerOfGame('ABBBBBBBAAA') == False) #Alice loses Bob wins
print(sln.winnerOfGame('AA') == False) #Alice loses Bob wins

