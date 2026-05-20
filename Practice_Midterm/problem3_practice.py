# Problem 3: Movie Night Organizer (40 points)
# Skills tested: All of Builds 1–3 integrated (variables, conditionals, loops, data structures, string methods, named patterns)

# Instructions
# A group of friends is planning movie night and needs to organize votes. Write a program that:
# 1.	Ask for the name of the person hosting (a string)
# 2.	Use a while loop to let the user add movie votes one at a time. After each vote, ask "Add another vote? (yes/no)". Stop when the user types "no".
# 3.	For each vote, collect:
# •	Voter name (a string)
# •	Movie title (a string)
# •	Genre: "action", "comedy", "horror", or "drama" (a string)
# 4.	Clean each vote’s data before storing:
# •	Voter name should be converted to title case (e.g., "jane doe" → "Jane Doe")
# •	Movie title should be converted to title case
# •	Genre should be converted to lowercase and stripped of whitespace
# 5.	Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
# 6.	After voting closes, produce a report:
# •	Total number of votes
# •	Number of comedy votes and number of non-comedy votes (use an accumulator or counter)
# •	A numbered list of all votes showing voter, movie, and genre (use a for loop with the index)
# •	If more than half the votes are for comedy, print: "Looks like a comedy night!"
# Example output:
# --- Movie Night Report (hosted by Alex) ---
# Total votes: 4
# Comedy votes: 3
# Other votes: 1

# All Votes:
# 1. Jane Doe voted for The Hangover (comedy)
# 2. Bob Smith voted for Inception (action)
# 3. Carol Lee voted for Bridesmaids (comedy)
# 4. Dan Park voted for Superbad (comedy)

# Looks like a comedy night!

# Constraints
# •	Must use a while loop (not a for loop with a fixed count)
# •	Must use string methods to clean data (title case, lowercase, strip)
# •	Must use a list of dictionaries
# •	Must use an accumulator/counter for comedy vs. non-comedy counts
# •	Must use a conditional for the comedy night message
