import argparse

letterVar = [
    ['!', '1', '?'],  # ! at index 33
    ['"', '\''],  # "
    ['#', '3'],  # #
    ['$', '4'],  # $
    ['%', '5'],  # %
    ['&', '7'],  # &
    ['\'', '"'],  # '
    ['(', '9'],  # (
    [')', '0'],  # )
    ['*', '8'],  # *
    ['+', '='],  # +
    [',', '<', '.', ':', ';'],  # ,
    ['-', '_', '~', '='],  # -
    ['.', '>', ':', ';'],  # .
    ['/', '\\', '?', '|'],  # /
    ['0', 'O', 'o', '()', '{}', '[]', ')'],  # 0
    ['1', 'l', 'L', 'i', 'I', '|', '!', '?', "/", '\\'],  # 1
    ['2', 'R', 'r', 'Z', 'z', 'S', 's', '@'],  # 2
    ['3', 'E', 'e', '#'],  # 3
    ['4', 'A', 'a', 'H', 'h', '$'],  # 4
    ['5', 'S', 's', '2', '%'],  # 5
    ['6', 'b', 'B', 'G', 'g', '^'],  # 6
    ['7', 'T', 't', 'L', 'l', '&'],  # 7
    ['8', 'B', 'b', '*'],  # 8
    ['9', 'g', 'G', 'q', 'Q', '('],  # 9
    [':', ';', '.', ','],  # :
    [';', ':', '.', ','],  # ;
    ['<', '>', ','],  # <
    ['=', '-', '_', '~'],  # =
    ['>', '<', '.'],  # >
    ['?', '/', '!'],  # ?
    ['@', '2', 'at', 'AT'],  # @
    ['A', 'a', '4', '$', '/-\\', '/_\\', '@', '2', '/\\'],  # A
    ['B', 'b', '8', '*', '|3', '13', '|}', '|]', '|)', '|:', '|;', '|8', '18', '6', '|B'],  # B
    ['C', 'c', '<', '{', '[', '('],  # C
    ['D', 'd', '|)', '|]', '|}'],  # D
    ['E', 'e', '3'],  # E
    ['F', 'f', '|=', 'ph', 'PH', '|#', '|"'],  # F
    ['G', 'g', '[-', '[+', '6', '|-', '|+'],  # G
    ['H', 'h', '4', '|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],  # H
    ['I', 'i', '1', '|', 'l', 'L'],  # I
    ['J', 'j', '_|', '_/', '_7', '_)', '_]', '_}'],  # J
    ['K', 'k', '|<', '1<', 'i<', 'I<', 'l<', 'L<'],  # K
    ['L', 'l', '|_', '|', '1', 'i', 'I'],  # L
    ['M', 'm', '44', '|\\/|', '^^', '/\\/\\', '/X\\', '/x\\', '[\\/]', '[]\\/[]', '][\\\\//][', '//.', '.\\\\', 'N\\',
     '|v|', '|V|', '/V\\', '/v\\', '[V]', '[v]', '[]V[]', '[]v[]', '][\\V//]['],  # M
    ['N', 'n', '|\\|', '/V', '/v', '/\\/', '][\\\\]['],  # N
    ['O', 'o', '0', '()', '[]', '{}'],  # O
    ['P', 'p', '|o', '|O', '|0', '|>', '|*', '|°', '|D', '/o', '/O', '/0'],  # P
    ['Q', 'q', 'O_', 'o_', '0_', '9', '(,)', '[,]', '{,}'],  # Q
    ['R', 'r', '|2', '12', 'i2', 'I2', 'l2', 'L2', '.-', '|^'],  # R
    ['S', 's', '5', '2', '$', '§'],  # S
    ['T', 't', '7', '+', '7`', '\'|\''],  # T
    ['U', 'u', 'V', 'v', '|_|', '\\_\\', '/_/', '\\_/', '(_)', '[_]', '{_}'],  # U
    ['V', 'v', 'U', 'u', '\\/'],  # V
    ['W', 'w', 'VV', 'vv', 'UU', 'uu', '(/\\)', '\\^/', '|/\\|', '\\X/', '\\x/', '\\\\\'', '\'//'],  # W
    ['X', 'x', '%', '*', '><', '}{', ')(', ']['],  # X
    ['Y', 'y', '`/', '¥'],  # Y
    ['Z', 'z', '2', '7_', '>_', '5', 'S', 's'],  # Z
    ['[', ']', '{', '('],  # [
    ['\\', '/', '|'],  # \
    [']', '}', '[', ')'],  # ]
    ['^', '6', '/\\'],  # ^
    ['_', '-', '=', '~'],  # _
    ['`', ',', '\''],  # `
    ['a', 'A', '4', '$', '/-\\', '/_\\', '@', '2', '/\\'],  # a
    ['b', 'B', '8', '*', '|3', '13', '|}', '|]', '|)', '|:', '|;', '|8', '18', '6', '|B'],  # b
    ['c', 'C', '<', '{', '[', '('],  # c
    ['d', 'D', '|)', '|]', '|}'],  # d
    ['e', 'E', '3'],  # e
    ['f', 'F', '|=', 'ph', 'PH', '|#', '|"'],  # f
    ['g', 'G', '[-', '[+', '6', '|-', '|+'],  # g
    ['h', 'H', '4', '|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],  # h
    ['i', 'I', '1', '|', 'l', 'L'],  # i
    ['j', 'J', '_|', '_/', '_7', '_)', '_]', '_}'],  # j
    ['k', 'K', '|<', '1<', 'i<', 'I<', 'l<', 'L<'],  # k
    ['l', 'L', '|_', '|', '1', 'i', 'I'],  # l
    ['m', 'M', '44', '|\\/|', '^^', '/\\/\\', '/X\\', '/x\\', '[\\/]', '[]\\/[]', '][\\\\//][', '//.', '.\\\\', 'N\\',
     '|v|', '|V|', '/V\\', '/v\\', '[V]', '[v]', '[]V[]', '[]v[]', '][\\V//]['],  # m
    ['n', 'N', '|\\|', '/V', '/v', '/\\/', '][\\\\]['],  # n
    ['o', 'O', '0', '()', '[]', '{}'],  # o
    ['p', 'P', '|o', '|O', '|0', '|>', '|*', '|°', '|D', '/o', '/O', '/0'],  # p
    ['q', 'Q', 'O_', 'o_', '0_', '9', '(,)', '[,]', '{,}'],  # q
    ['r', 'R', '|2', '12', 'i2', 'I2', 'l2', 'L2', '.-', '|^'],  # r
    ['s', 'S', '5', '2', '$', '§'],  # s
    ['t', 'T', '7', '+', '7`', '\'|\''],  # t
    ['u', 'U', 'V', 'v', '|_|', '\\_\\', '/_/', '\\_/', '(_)', '[_]', '{_}'],  # u
    ['v', 'V', 'U', 'u', '\\/'],  # v
    ['w', 'W', 'VV', 'vv', 'UU', 'uu', '(/\\)', '\\^/', '|/\\|', '\\X/', '\\x/', '\\\\\'', '\'//'],  # w
    ['x', 'X', '%', '*', '><', '}{', ')(', ']['],  # x
    ['y', 'Y', '`/', '¥'],  # y
    ['z', 'Z', '2', '7_', '>_', '5', 'S', 's'],  # z
    ['{', '}', '[', '('],  # {
    ['|', '\\', '/', '[', ']'],  # |
    ['}', '{', ']', ')'],  # }
    ['~', '-', '_', '=', '\'']  # ~
]
simplettervar = [
    ['!', '1'],  # ! at index 33
    ['"'],  # "
    ['#', '3'],  # #
    ['$', '4'],  # $
    ['%', '5'],  # %
    ['&', '7'],  # &
    ['\''],  # '
    ['(', '9'],  # (
    [')', '0'],  # )
    ['*', '8'],  # *
    ['+', '='],  # +
    [','],  # ,
    ['-'],  # -
    ['.'],  # .
    ['/'],  # /
    ['0', 'O', '()'],  # 0
    ['1', 'l', 'i', '!'],  # 1
    ['2', 'R', 'r', '@'],  # 2
    ['3', 'E', '#'],  # 3
    ['4', 'A', '$'],  # 4
    ['5', 'S', '%'],  # 5
    ['6', 'b', '^'],  # 6
    ['7', 'T', '&'],  # 7
    ['8', 'B', '*'],  # 8
    ['9', 'g', 'q'],  # 9
    [':'],  # :
    [';'],  # ;
    ['<'],  # <
    ['='],  # =
    ['>'],  # >
    ['?'],  # ?
    ['@', '2'],  # @
    ['A', 'a', '4'],  # A
    ['B', 'b', '8'],  # B
    ['C', 'c', '<'],  # C
    ['D', 'd', '|)'],  # D
    ['E', 'e', '3'],  # E
    ['F', 'f', '|='],  # F
    ['G', 'g', '[-'],  # G
    ['H', 'h', '4', '|-|'],  # H
    ['I', 'i', '1',  'l'],  # I
    ['J', 'j', '_|'],  # J
    ['K', 'k', '|<'],  # K
    ['L', 'l', '1', 'i'],  # L
    ['M', 'm', '44', '|\/|', '/\/\\'],  # M
    ['N', 'n', '|\|'],  # N
    ['O', 'o', '0', '()'],  # O
    ['P', 'p', '|o'],  # P
    ['Q', 'q', 'O_'],  # Q
    ['R', 'r', '12'],  # R
    ['S', 's', '5', '$'],  # S
    ['T', 't', '7', '+'],  # T
    ['U', 'u', 'V', 'v', '|_|'],  # U
    ['V', 'v', 'U', 'u', '\/'],  # V
    ['W', 'w', 'VV', 'vv'],  # W
    ['X', 'x', '%', '*', '><'],  # X
    ['Y', 'y'],  # Y
    ['Z', 'z', '2', '5', 'S', 's'],  # Z
    ['['],  # [
    ['\\'],  # \
    [']'],  # ]
    ['^'],  # ^
    ['_'],  # _
    ['`'],  # `
    ['a', 'A', '4', '@'],  # a
    ['b', 'B', '8', '|3'],  # b
    ['c', 'C', '<'],  # c
    ['d', 'D', '|)'],  # d
    ['e', 'E', '3'],  # e
    ['f', 'F', '|='],  # f
    ['g', 'G', '[-'],  # g
    ['h', 'H', '4', '|-|'],  # h
    ['i', 'I', '1', 'l'],  # i
    ['j', 'J', '_|'],  # j
    ['k', 'K', '|<'],  # k
    ['l', 'L', '1', 'i'],  # l
    ['m', 'M', '44', '|\/|', '^^', '/\/\\'],  # m
    ['n', 'N', '|\|'],  # n
    ['o', 'O', '0', '()'],  # o
    ['p', 'P', '|o'],  # p
    ['q', 'Q', 'O_'],  # q
    ['r', 'R', '12'],  # r
    ['s', 'S', '5', '$'],  # s
    ['t', 'T', '7', '+'],  # t
    ['u', 'U', 'V', 'v', '|_|'],  # u
    ['v', 'V', 'U', 'u', '\/'],  # v
    ['w', 'W', 'VV', 'vv'],  # w
    ['x', 'X', '%', '*', '><'],  # x
    ['y', 'Y'],  # y
    ['z', 'Z', '2', '7_'],  # z
    ['{'],  # {
    ['|'],  # |
    ['}'],  # }
    ['~']  # ~
]
passwordList = []
keywordList = []

parser = argparse.ArgumentParser(description="Keywords to Hash Cracking Wordlists!")
parser.add_argument('--version', action='version', version='0.2')
parser.add_argument('-m', metavar='Mode', type=int, help='0 for simple swap mode, or 1 for complicated swap mode. 0 is '
                    'set by default')
parser.add_argument('-lp', metavar='Lead Padding', type=int, help='Max lead padding length, 0 for no padding')
parser.add_argument('-tp', metavar='Tail Padding', type=int, help='Max lead padding length, 0 for no padding')
parser.add_argument('-lt', metavar='Lead Type', type=int, help='0 for numeric, 1 for alpha, 2 for full. 2 by default')
parser.add_argument('-tt', metavar='Tail Type', type=int, help='0 for numeric, 1 for alpha, 2 for full. 2 by default')

results = parser.parse_args()
memelements = 10000000
curkey = None
cyclelist = [None]
cyclelistint = [None]
cycleint = [None]
currentcycle = [None]
workinglist = [None]
editfile = None
templist = [None] * memelements
tempint = 0
filepath = None
run = True;


def cycle(tocycle, l, f):
    global run
    if run:
        rewrite(f)
        run = False
    if l == 1:
        letterlist = letterVar
    elif l == 0:
        letterlist = simplettervar
    global curkey
    global cyclelist
    global cyclelistint
    global cycleint
    global currentcycle
    global workinglist
    global filepath
    filepath = f
    curkey = tocycle
    cyclelist = list(tocycle)  # list of original chars
    cyclelistint = [None] * len(tocycle)  # list of original char integer values
    cycleint = [None] * len(tocycle)  # list of char transformations
    currentcycle = [0] * len(tocycle)  # list of current char transformation
    workinglist = [None] * len(tocycle)  # list of working chars
    for index in range(0, len(tocycle)):
        cycleint[index] = len(letterlist[ord(cyclelist[index])-33])
        cyclelistint[index] = ord(cyclelist[index])-33
    for index in range(0, cycleint[0]):
        workinglist[0] = letterlist[ord(cyclelist[0])-33][index]
        if len(tocycle) > 0:
            nextletter(1, letterlist)
        else:
            tolist(''.join(workinglist))
    tolist(''.join(workinglist), 1)


def nextletter(i, ls):
    ni = i + 1
    for index in range(0, cycleint[i]):
        workinglist[i] = ls[ord(cyclelist[i])-33][index]
        if len(curkey) > i+1:
            nextletter(ni, ls)
        else:
            tolist(''.join(workinglist))


def tolist(p, l=0):
    # passwordList.append(p)
    global templist
    global tempint
    templist[tempint] = p
    if tempint == len(templist)-1 or l == 1:
        tempint = 0
        writefile(templist, l)
        templist = [None] * memelements
    else:
        tempint += 1


def writefile(p, l):
    out = open(filepath, 'a', encoding='utf-8')
    if l == 0:
        for index in range(0, len(p)):
            out.write(p[index] + '\n')
    else:
        for index in range(0, len(p)):
            if p[index] is not None:
                out.write(p[index] + '\n')
            else:
                break
    out.close()


def rewrite(f):
    out = open(f, 'w', encoding='utf-8')
    out.close()

# def createfile(f):
#    out = open(f, 'w')
#    out.close()


# def appendfile(p, f):
#    out = open(f, 'a')
#    for index in range(0, len(p)):
#        out.write(p[index] + '\n')
#    out.close()


cycle('password', 0, 'foo.txt')
# print(passwordList)
# writefile(passwordList, 'foo.txt')
print('list is ' + str(len(passwordList)) + ' passwords long')
