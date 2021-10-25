from  chessboard.chess_board import ChessBoard

def test_queens_on_same_row():
    #rang
    chess=ChessBoard()
    chess.add_red(1,5)
    chess.add_blue(4,6)
    expected=False
    #Act
    actual=chess.is_under_attack()
    #Assert
    assert actual==expected
