'''Hogwarts_grades.py
 Ira Toles
 November 13th 2024


import os


# Function to create the scores.txt file
def create_scores_file ():
    scores_data = """Harry Potter, 78
Hermione Granger, 98
Ron Weasley, 72
Draco Malfoy, 85"""
    with open ('scores.txt', 'w') as file:
        file.write (scores_data)
    print ("scores.txt file created successfully.")


# Function to run the hogwarts_grades.py script
def run_hogwarts_grades_script ():
    os.system ('python hogwarts_grades.py')


# Main function
if __name__ == "__main__":
    create_scores_file ()
    run_hogwarts_grades_script ()