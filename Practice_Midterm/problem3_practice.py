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
host = input("What is the name of the host? ").capitalize()
vote = input("Did you want to add a votes? yes or no ").lower()
votes = []
add_more = "yes"
while add_more == "yes": 
    voter_name = input("What is your name? ").title()
    movie_title = input("What is the name of the movie? ").title()
    genre = input("What is the genre? (action, comedy, horror, or drama) ").lower().strip()
 # 5. Store each vote as a dictionary in a list with keys: "voter", "movie", "genre"
    votes.append({
 "voter name": voter_name, "movie title": movie_title, "genre": genre
    })
    add_more = input("Add another vote? yes or no ")

# 6.	After voting closes, produce a report:
total_votes = len(votes)
comedy_votes = 0 
for vote in votes: 
    if vote["genre"] == "comedy":
        comedy_votes+=1 
non_comedy_vote = total_votes - comedy_votes
print(f"--- Movie Night Report (hosted by {host}) ---\n"
      f"Total votes: {total_votes}\n"
      f"Comedy votes: {comedy_votes}\n"
      f"Other votes: {non_comedy_vote}\n")
print("All votes:")
count = 1 
for vote in votes: 
    print(f"{count}. {vote['voter name']} voted for {vote['movie title']} ({vote['genre']})\n")
    count+=1 
if comedy_votes / total_votes > 0.5:
    print("Looks like a comedy night!")




# •	A numbered list of all votes showing voter, movie, and genre (use a for loop with the index)
# •	If more than half the votes are for comedy, print: "Looks like a comedy night!"


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
