def minion_game(string):
    player1,player2 = 0,0
    res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]            
    for word in list(set(res)):
        if word[0] in "AEOIU":
            player1 += string.count(word)
        else:
            player2 += string.count(word)
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)