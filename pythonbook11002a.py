<<<<<<< HEAD
def hangman ( word ) :
    wrong = 0 
    stages = [ '' , 
               '__________      ' ,
               '|               ' , 
               '|       |       ' , 
               '|       O       ' , 
               '|      /|\      ' , 
               '|      / \      ' , 
               '|               ' , ]
    rletters = list(word)
    board= ["_"] * len(word)
    win = False
    print ( "ハングマンへようこそ！" )     
#   for i in range(0,8) :
#       print ( stages[i] ) 

    while wrong < len(stages) - 1 :
        print ( "\n" )
        msg = "単語のうち、１文字を予想してね。"
        char = input(msg)
        if char in rletters :
            print ( "ヒットしました。" ) 
            cind = rletters.index(char)
            board[cind] = char 
            rletters[cind] = '$'
        else :
            print ( "ぶっぶー、はずれ。" ) 
            wrong += 1 
        print  ( " ".join( board ) )
        e = wrong + 1
        print ( "\n".join(stages[0:e]) )
        if "_" not in board :
            print ( "あなたの勝ち！おめでとうございます。正解は、" , end = '' )
            print ( "".join(board) + "です。")
            win = True 
            break 
    if not win : 
        print ( "\n".join( stages[0:wrong+1] ) ) 
        print ( "あなたは負けました！正解は{}でした。".format(word) )

=======
def hangman ( word ) :
    wrong = 0 
    stages = [ '' , 
               '__________      ' ,
               '|               ' , 
               '|       |       ' , 
               '|       O       ' , 
               '|      /|\      ' , 
               '|      / \      ' , 
               '|               ' , ]
    rletters = list(word)
    board= ["_"] * len(word)
    win = False
    print ( "ハングマンへようこそ！" )     
#   for i in range(0,8) :
#       print ( stages[i] ) 

    while wrong < len(stages) - 1 :
        print ( "\n" )
        msg = "単語のうち、１文字を予想してね。"
        char = input(msg)
        if char in rletters :
            print ( "ヒットしました。" ) 
            cind = rletters.index(char)
            board[cind] = char 
            rletters[cind] = '$'
        else :
            print ( "ぶっぶー、はずれ。" ) 
            wrong += 1 
        print  ( " ".join( board ) )
        e = wrong + 1
        print ( "\n".join(stages[0:e]) )
        if "_" not in board :
            print ( "あなたの勝ち！おめでとうございます。正解は、" , end = '' )
            print ( "".join(board) + "です。")
            win = True 
            break 
    if not win : 
        print ( "\n".join( stages[0:wrong+1] ) ) 
        print ( "あなたは負けました！正解は{}でした。".format(word) )

>>>>>>> 12e0810da05ca930cb7ff9bd0a2a28f406791e3c
            