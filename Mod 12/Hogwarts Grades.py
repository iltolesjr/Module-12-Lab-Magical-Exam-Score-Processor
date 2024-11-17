# Hogwarts_grades.py
# Ira Toles
# November 13th 2024

def read_scores ():
    scores = []
    with open ('scores.txt', 'r') as file:  # Specify the file name and mode
        for line in file:
            name, score = line.strip ().split (',')
            scores.append ((name, int (score)))
    return scores


def calculate_average (scores):
    total = sum (score for _, score in scores)
    return total / len (scores)


def write_report (scores, average):
    with open ('report.txt', 'w') as file:
        file.write ("Transfiguration O.W.L. Results\n")
        file.write ("=============================\n\n")
        for name, score in scores:
            file.write (f"{name}: {score}\n")
        file.write (f"\nClass Average: {average:.2f}")


# Main process
if __name__ == "__main__":
    scores = read_scores ()
    average = calculate_average (scores)
    write_report (scores, average)
    print ("Magical report generated in 'report.txt'!")