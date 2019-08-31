#! python3

def printTable(table):

    columns = columnsWidth(table)

    for i in range(len(table[0])):
        line =''
        for j in range(len(table)):
            line += table[j][i].rjust(columns[j])
        print(line)

def columnsWidth(table):

    result = []
    for i in range(len(table)):
        result.append(0)
        for word in table[i]:
            if len(word) > result[i]: result[i] = len(word)
        result[i] += 1

    return result


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
