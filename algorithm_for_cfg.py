
#Serdar Sertgöz



#grammar rules in chomsky normal form
grammar_rules =   {     "S" : {"AB","aB","Ab","ab"},
                        "A" : {"BB","bB","Bb","bb"},
                        "B" : {"AB","aB","Ab","ab"}
    
}          
#input
string = ["a","a","b","b","b"]


def algorithm(rules, inp):

    length = len(inp)

    # table on which we run the algorithm
    table = [[set() for _ in range(length+1)] for i in range(length+1)]
    for i in range(length):
        table[i][i].add(inp[i])

    for s in range(length):
        for i in range(length - s+1):
            for k in range(i,i+s):
                for j in rules.keys():
                    for first in table[i][k]:
                        for second in  table[k+1][i+s]:
                            #print(type(first))
                            if first + second in rules[j]:
                                table[i][i+s].add(j)
    #seeTable(table)
    if "S" in table[0][length-1]:
        return True
    return False

def seeTable(table):
    for i in range(len(table)-1):
        print(table[i][:-1])


def show_result(isTrue):
    if isTrue:
        print("The input belongs to this context free grammar!")
    else:
        print("The input does not belong to this context free grammar!")


if __name__ == '__main__':
    show_result(algorithm(grammar_rules, string))
