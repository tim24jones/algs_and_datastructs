#messy thoughts on sudoku
class rowset
    def __init__(self,row,entry):
    letters='abcdefghij'
    set=[]
    for char in letters: #use letters as placeholders to create a 10 member list
        set=set+[sudoku_member(row,letters.find(char),entry[letters.find(char)])]
    self.set=set

class colset
    def __init__(self,column,entry):
    letters='abcdefghij'
    set=[]
    for char in letters: #use letters as placeholders to create a 10 member list
        set=set+[sudoku_member(letters.find(char),column,entry[letters.find(char)])]
    self.set=set

class sudoku_member #the heart of initial thinking, each number having an ordered triple, starting with a locatory ordered pair
    def __init__(self,row,column,entry):
    self.row=row
    self.column=column
    self.value=entry
    if row not in range(10):
        return invalid row
    if column not in range(10):
        return invalid column
class fill_entries
    def __init__(self,entries):
    if entry==blank:
        for range(10):
            set=[]+[None]
            entries=set
    elif len(entries)!=10:
        return 'Needs 10 list entries'
    self.entries=entries

class sudoku_board
    def __init__(self,entry):

    for i in range(10):
        sudoku_rowset(i,sudoku_entries())

    self.initial=(self,entry):
        
class sudoku_game
    def __init__(self,setup):
    self.setup=setup #make setup in str for immutability
    initial_entries=[] #convert to list to change values
    for n in range(0,90,10):
        initial_entries=initial_entries+list(self.setup[n:n+10]

