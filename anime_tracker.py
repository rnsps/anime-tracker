# Create an empty list to store anime
anime_list = []

def get_valid_rating():
     while True:
       
            # word error loop
             try:
                 rating =  float(input("enter rating: "))
                

             except ValueError:
                 print("Please enter a number (0-10)")
                 continue
    
            # number error loop
             if 0 <= rating <= 10:
                return rating
                
             else:
                 print("Please enter a number (0-10)")
                 continue

def get_valid_status():
    while True:
             status = input("Status - Watching, Completed, Dropped, Plan To Watch: ").strip().title()
    
        
            # Organised all valid statuses into a list
             valid_statuses =  [
                        "Watching",
                        "Completed",
                        "Dropped",
                        "Plan To Watch",
                        "On Hold"
                    ]
    
             if status in valid_statuses:
                 return status
    
             else:
                 print("Invalid status. Try again.")
                 continue

def get_valid_count(status):

    total_episodes = int(input("Total episodes: "))



    
    if status == "Plan To Watch":
         return 0 


    else:
         
        while True:
            try:
                episode_count = int(input("Episode progress: "))
                
            except ValueError:
                 print("Enter a numerical number for the episode count")
                 continue

            if 0 > episode_count or episode_count > total_episodes:
                print("Invalid count")
                continue
        
            else:
                return episode_count



              

# let the user keep adding anime until they choose to stop
while True:
    # Ask the user for an anime title
    title = input("search anime: ").strip().title()
    # Ask the user for a rating
    rating = get_valid_rating()
    # Ask the user for status
    status = get_valid_status()
    # Ask the user for episode count
    episode_count = get_valid_count(status)

         
    # Add into one dictionary 
    anime = {
        "title": title,
        "rating": rating,
        "status": status,
        "total episodes": total_episodes,
        "episode count": episode_count}
    

    #add dictionary to list
    anime_list.append(anime)

    # ask for anime
    # add anime
    choice = input("Want to add another anime? ").strip().lower()
     
        
    if choice == "no":
        break

# make list printable
for anime in anime_list:
    print(anime["title"], anime["rating"], anime["status"])
