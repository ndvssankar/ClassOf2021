import sys
def read_input():
    return list(map(int, sys.stdin.readline().split()))

def load_test_case():
    m, n = read_input()
    if not m:
        return False
    teams = read_input()
    tables = read_input()
    return teams, tables

def seat_arrangement(tables, teams):
    if not tables:
        return None
    teams_tables = [list() for _ in teams]
    
    tables = sorted([(seats,table) for table, seats in enumerate(tables)], reverse=True)
    print (tables)
    return None

while True:
    teams, tables = load_test_case()
    if teams is None:
        break
    res = seat_arrangement(tables, teams)
    if not res:
        print (0)
    else:
        print (1)
        for i in res:
            print (" ".join(map(str, sorted(res))))

