if __name__ == '__main__':

    records = []

    for _ in range(int(input())):
        name, x, y, z= input().split()
        x, y, z = [float(x), float(y), float(z)]
        records.append([name, x, y, z])

    query_name = input()

    for i in range(len(records)):
        if records[i][0] == query_name:
            query = ((records[i][1] + records[i][2] + records[i][3]) / 3)
    
    print("%.2f" % query)
