'''
A group of friends is planning movie night and needs to organize votes. 
Write a program that:
'''
# 1.	Ask for the name of the person hosting (a string)
host = input("Host name: ")

# 5.	Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
votes = []

# 2.	Use a while loop to let the user add movie votes one at a time. 
# After each vote, ask "Add another vote? (yes/no)". Stop when the user 
# types "no".
add_more = "yes"
while add_more == "yes":
    # 3.	For each vote, collect:
    # •	Voter name (a string)
    voter_name = input("Voter: ").title()
    # •	Movie title (a string)
    movie_title = input("Movie: ").title()
    # •	Genre: "action", "comedy", "horror", or "drama" (a string)
    genre = input("Genre: ").lower().strip()
    # 4.	Clean each vote’s data before storing:
    # •	Voter name should be converted to title case (e.g., "jane doe" → "Jane Doe")
    # •	Movie title should be converted to title case
    # •	Genre should be converted to lowercase and stripped of whitespace

    # 5.	Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
    vote_dict = { "Voter": voter_name, "Movie": movie_title, "Genre": genre}
    votes.append(vote_dict)
    add_more = input("Add another vote? (yes/no) ").lower() 

# 6.	After voting closes, produce a report:
# •	Total number of votes
# •	Number of comedy votes and number of non-comedy votes (use an accumulator or counter)
# ex: --- Movie Night Report (hosted by Alex) ---
# Total votes: 4
# Comedy votes: 3
# Other votes: 1
print(f"--- Movie Night Report (hosted by {host}) ---")
total_votes = len(votes)
comedy_votes = 0 
for vote in votes: 
    if vote["Genre"] == "comedy": 
        comedy_votes += 1 
non_comedy_votes = total_votes - comedy_votes
print(f"Total votes: {total_votes}")
print(f"Comedy votes: {comedy_votes}")
print(f"Other votes: {non_comedy_votes}")

# •	A numbered list of all votes showing voter, movie, and genre (use a for loop with the index)
# All Votes:
# 1. Jane Doe voted for The Hangover (comedy)
# 2. Bob Smith voted for Inception (action)
# 3. Carol Lee voted for Bridesmaids (comedy)
# 4. Dan Park voted for Superbad (comedy)
for i in range(len(votes)):
    print(f"{i+1}. {votes[i]["Voter"]} voted for {votes[i]["Movie"]} ({votes[i]["Genre"]})")
# •	If more than half the votes are for comedy, print: "Looks like a comedy night!"
if (comedy_votes / total_votes) > 0.5:
    print(f"Looks like  comedy night!")
# Looks like a comedy night!


