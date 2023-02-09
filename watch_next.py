# A program that compares a description, synopsis, of The Planet Hulk movie to recommend one of ten other movies. 
# The recommendation will be reommended based on similarity. 
import spacy
nlp = spacy.load('en_core_web_md')

# The Planet Hulk synopsis is initialised as it is the central string that is to be compared against the others from the .txt.file
# It is also cast as nlp to ready for a spacy comparison
hulk_description = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# This function does the main work of pulling in the read items to return a dictionary of similarity scores
def synopsis_sort():

    # Then there was to create a dictionary so that the most and least similar synopsis can be displayed 
    # After the initial print above the dictionary, synopsis_similarity_dict is then make ready for additions then sorting.
    synopsis_similarity_dict = {}
    for i, x in enumerate(movies):
        synopsis_similarity_dict.update({x[0:2]: x.similarity(hulk_description)})


    return synopsis_similarity_dict

# This print_synopsis function is for some efficiency later on in the program. 
# The print_synopsis function takes in a variable that is already a dict item. 
def print_synopsis(synopsis_sorted):

    for i, x in enumerate(movies): 
        if f"{synopsis_sorted[0]}" == str(x[0:2]):
            print(x[3:])
    
    pass

# The text file movies.txt i read and made ready for reading as a list. 
with open('movies.txt', 'r') as movie_descriptions: 
    movie_descriptions = movie_descriptions.readlines()

    for i, x in enumerate(movie_descriptions):
        movie_descriptions_split = x.split
    
# Here the opened file, now a list, is worked through so that each list item is an nlp. 
movies = [nlp(descriptions) for descriptions in movie_descriptions]

print("\nThe list of movies and there similarities are: \n")

# I considered using statistical mean when I realised that some coparisons are made word by word
# I didn't need to use the statistics module because the outcome of the following for loop are individual floats. 
# The for loop produces a print out of each movie and the similarity. 
# I thought it useful to leave this for loop in as you will notice from the print out
synopsis_similarity = []
for i, x in enumerate(movies):
    synopsis_similarity.append(x.similarity(hulk_description))
    # synopsis_list = x
    print(f"{x[0:2]}: {x.similarity(hulk_description)}")

# Here the main function gets to work regarding presenting the synopsis dictionary by similarity score. 
synopsis_sort()

synopsis_similarity_dict = synopsis_sort()

# synopsis_similarity_dict is then sorted by items as highest and lowest similarity. _
# I have already prepared the dictionary so that the items are the scores. 
# I've tried to define these as a method / function even though won't save on efficiency however it doesn't return a dict.
synopsis_sim_high = dict(sorted(synopsis_similarity_dict.items(), key=lambda item: item[1], reverse=True))
synopsis_sim_low = dict(sorted(synopsis_similarity_dict.items(), key=lambda item: item[1]))

# These two variables are the variables that are to be used in the print_synopsis function. 
first_pair = list(synopsis_sim_high.items())[0]
last_pair = list(synopsis_sim_low.items())[0]

# From here on the print outs begin so that the user is informed about similarities, scores and so that they can read the synopsises. 
print(f'''\nConsidering that the user enjoyed the movie Planet Hulk and wants to watch another similar movie: \n

        The movie synopsis that the user is likely to watch next is {first_pair[0]}.
        {first_pair[0]} has the highest similarity of synopsis on a score of {first_pair[1]} from 0-1 of 10 movies.\n''')


print(f"The synopsis for {first_pair[0]} is: \n")

print_synopsis(first_pair)

print("-----------------------------------------------------------------------------------------------------------------\n")

print(f'''\nConsidering that the user enjoyed the movie Planet Hulk and wants to watch another similar movie: \n 
        The movie synopsis that the user is least likely to watch next is {last_pair[0]}.
        {last_pair[0]} has the lowest similarity of synopsis on a score of {last_pair[1]} from 0-1 of 10 movies\n''')

print(f"The synopsis for {last_pair[0]} is: \n")

print_synopsis(last_pair)

print("------------------------------------------------------------------------------------------------------------------\n")

print(f"The synopsis for Planet Hulk is: \n\n {hulk_description}\n")

#Code ends    