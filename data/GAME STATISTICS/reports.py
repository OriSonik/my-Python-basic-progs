import export
import printing

f = open('game_stat.txt', 'r')


# # "How many games are in the file?"
# def count_games(file_name):    
#     return int

# # "Is there a game from a given year?"
# def decide(file_name, year):
#     return bool

# # "Which is the latest game?"
# def get_latest(file_name):
#     return str('title')

# # "How many games are in the file by genre?"
# def count_by_genre(file_name, genre):
#     return int

# # "What is the line number of a given title?"
# def get_line_number_by_title(file_name, title):
#   a  return int
#   b  raise ValueError # exception if title not found

# # "Can you give me the alphabetically ordered list of the titles?"
# def sort_abc(file_name):
#     return list of titles
#     # don't use sort method nor sorted, min, max built-in f 
#     # implement own sorting algorithm

# # "Which genres occur in the data file?"
# def get_genres(file_name):
#     return list of genres [no duplicates]
#     # don't use sort method nor sorted, min, max built-in f 
#     # implement own sorting algorithm

# # "What is the release year of the top sold first-person shooter game?"
# def when_was_top_sold_fps(file_name):
#   a  return int
#   b  raise ValueError # exception if none found

# # reports contain the functions providing the answers, 
# # printing asks for user input and prints output to the terminal, 
# # export gets the required input parameters as command line arguments, then saves the results. 

# # The latter two modules call reports's core functions.

# # The reports module does not ask for user input and does not print anything.

# # The printing module asks for user input, first for the name of a data file, then it goes through all the questions, 
# #                                                  asks for the extra arguments, and prints the results to the screen.
# # The printing module does not exit on reports's exceptions but handles them and communicates them with the user.
# # The printing module does not implement the answers themselves but imports report (and does not import export).

# # The export module needs command line arguments in this form python3 export.py source_file_name target_file_name input_year input_genre input_title where the last 3 are arguments for questions #2, #4, and #5, respectively. The results are saved into a file target_file_name, the individual answers written into new lines.
# # The export module does not exit on reports's exceptions but handles them and sends informative text snippets to the output instead.
# # The export module does not implement the answers themselves but imports report (and does not import printing).
