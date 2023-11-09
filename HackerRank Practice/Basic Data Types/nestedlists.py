if __name__ == '__main__':
    
    # Create empty lists
    students, scores, results = [], [], []

    # Enter n number of student records
    for _ in range(int(input())):
        # Input name as string and score as float
        name = input()
        score = float(input())
        # Append each individual name and score as sublist entry into nested list
        students.append([name, score])
        # Append score into list of all scores
        scores.append(score)

    # Create set of all scores to remove duplicate scores
    scores = sorted(set(scores))
    # Second lowest score will be in index one of sorted set
    secondlowest = scores[1]

    # For each student sublist entry in students list check if score matches second lowest score
    for i in range(len(students)):
        if students[i][1] == secondlowest:
            # If matches second lowest score append name to results list
            results.append(students[i][0])
    
    # Sort results list in ascending alphabetical order
    results.sort()

    # Print results
    for x in results:
        print(x)


