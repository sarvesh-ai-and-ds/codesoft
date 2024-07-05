import random

movies = {"comedy": ["Hera Pheri (2000)", "Munna Bhai M.B.B.S. (2003)", "Andaz Apna Apna (1994)", "3 Idiots (2009)",
                     "Phir Hera Pheri (2006)", "Garam Masala (2005)", "Coolie No. 1 (1995)", "Dhamaal (2007)",
                     "Golmaal Fun Unlimited (2006)", "OMG: Oh My God! (2012)", "Hungama (2003)", "Heyy Babyy (2007)",
                     "Chachi 420 (1997)", "Welcome Back (2015)", "It's Entertainment (2014)", "Golmaal Again (2017)",
                     "Dil Chahta Hai (2001)", "Delhi Belly (2011)", "Pyaar Ka Punchnama (2011)", "Jolly LLB (2013)",
                     "Chachi 420 (1997)", "Bheja Fry (2007)", "Dulhe Raja (1998)", "Mr. & Mrs. Khiladi (1997)",
                     "Partner (2007)", "Bhool Bhulaiyaa (2007)", "Mujhse Shaadi Karogi (2004)", "No Entry (2005)",
                     " Dhol (2007)", "Masti (2004)", "Housefull (2010)", "Ready (2011)", "Malamaal Weekly (2006)",
                     "Kyaa Super Kool Hain Hum (2012)", "Chup Chup Ke (2006)", "Bhagam Bhag (2006)"],
          "action": ["Terminator 2: Judgment Day (1991)", "Die Hard (1988)", "Aliens (1986)",
                     "Mad Max:Fury Road (2015)", "Indiana Jones and the Raiders of the Lost Ark (1981)",
                     "Mission: Impossible - Fallout (2018)", "The Last Boy Scout (1991)", "Inception (2010)",
                     "The Matrix (1999)", "The Dark Knight (2008)", "Tenet (2020)", "The Rock (1996)",
                     "Gladiator (2000)", "Elite Squad 2: The Enemy Within (2010)", "Predator (1987)", "Skyfall (2012)",
                     "RoboCop (1987)", "Casino Royale (2006)", "The Boondock Saints (1999)", "The Fugitive (1993)",
                     "Ford v Ferrari (2019)", "Pirates of the Caribbean: The Curse of the Black Pearl (2003)",
                     "The Northman (2022)", "Top Gun: Maverick (2022)", "Sonic the Hedgehog 2 (2022)", "The Unbearable Weight of Massive Talent (2022)",
                     "Avatar: The Way of Water (2022)", "K.G.F: Chapter 2 (2022)", "The Gentlemen (2019)", "Moonfall (2022)"],
          "romantic": ["The Notebook (2004)", "Notting Hill (1999)", "Gone with the Wind (1939)", "Titanic (1997)",
                       "Casablanca (1942)", "The Bridges of Madison County (1995)", "Moulin Rouge (2001)",
                       "When Harry Met Sally... (1989)", "Scent of a Woman (1992)", "Legends of the Fall (1994)",
                       "Wedding Crashers (2005)", "Becoming Jane (2007)", "Remember Me (I) (2010)",
                       "Hum Apake Hain Kon (1994)", "Vivah (2006)", "Thi Sadhya Kay Karte (2017)",
                       "Hum Dil De Chuke Sanam (1999)", "Sanam Teri Kasam (2016)", "Sanam Re (2016)",
                       "Hate Story 4 (2018)", "The French Dispatch (2021)", "Downton Abbey (2019)", "Pitch Perfect (2012)",
                       "Call Me by Your Name (2017)", "Pride & Prejudice (2005)", "Twilight (I) (2008)", "After (I) (2019)",
                       "Marry Me (2022)", "The In Between (2022)", "Swiss Army Man (2016)", "Clueless (1995)"],
          "horror": ["Alien (1979)", "The Shining (1980)", "The Thing (1982)", "Rosemary's Baby (1968)",
                     "The Silence of the Lambs (1991)", "Let the Right One In (2008)", "Shaun of the Dead (2004)",
                     "Scream (1996)", "A Quiet Place (2018)", "The Return of the Living Dead (1985)",
                     "The Autopsy of Jane Doe (2016)", "The Evil Dead (1981)", "The Haunting (1963)", "REC (2007)",
                     "Young Frankenstein (1974)", "Saw (2004)", "Coraline (2009)", "Dawn of the Dead (1978)",
                     "Poltergeist (1982)", "Psycho (1960)", "Firestarter (2022)", "Fresh (2022)", "American Psycho (2000)",
                     "The Witch (2015)", "Tusk (I) (2014)", "The Hunt (II) (2020)", "Piranha 3D (2010)", "Invaders from Mars (1986"],
          "animated": ["Toy Story (1995)", "Up (2009)", "Finding Nemo (2003)", "Spirited Away (2001)", "WALL·E (2008)",
                        "The Incredibles (2004)", "Ratatouille (2007)", "The Iron Giant (1999)", "The Lion King (1994)",
                        "My Neighbor Totoro (1988)", "Monsters, Inc. (2001)", "Beauty and the Beast (1991)",
                        "How to Train Your Dragon (2010)", "Princess Mononoke (1997)", "Fantastic Mr. Fox (2009)",
                        "Waltz with Bashir (2008)", "Inside Out (I) (2015)", "Howl's Moving Castle (2004)",
                        "Zootopia (2016)", "The Bad Guys (2022)", "Turning Red (2022)", "Chip 'n' Dale: Rescue Rangers (2022)", "Spider-Man: Into the Spider-Verse (2018)",
                       " Cars (2006)", "Moana (I) (2016)", "Beauty and the Beast (1991)", "Spirited Away (2001)", "Luca (2021)", "Raya and the Last Dragon (2021)"],
          "crime": ["Once Upon a Time in America (1984)", "L.A. Confidential (1997)", "Chinatown (1974)",
                    "Double Indemnity (1944)", "The Godfather: Part II (1974)", "The Killing (1956)",
                    "To Kill a Mockingbird (1962)", "Witness for the Prosecution (1957)", "M (1931)",
                    "City of God (2002)", "Vertigo (1958)", "In Bruges (2008)", "The Green Mile (1999)",
                    "Léon: The Professional (1994)", "The Silence of the Lambs (1991)", "The Maltese Falcon (1941)",
                    "The Untouchables (1987)", "Goodfellas (1990)", "Heat (1995)", "A Clockwork Orange (1971)", "The Batman (2022)", "Death on the Nile (2022)", "The Godfather (1972)", "K.G.F: Chapter 2 (2022)",
                    "The Outfit (2022)", "Gangubai Kathiawadi (2022)", "London Fields (2018)", "Wrath of Man (2021)"],
          "science fiction": ["2001: A Space Odyssey (1968)", "Solaris (1972)", "The Prestige (2006)", "Alien (1979)",
                              "Blade Runner (1982)", "Stalker (1979)", "The Matrix (1999)", "Metropolis (1927)",
                              "Terminator 2: Judgment Day (1991)", "Inception (2010)", "Planet of the Apes (1968)",
                              "Star Wars (1977)", "Back to the Future (1985)", "A Clockwork Orange (1971)",
                              "12 Monkeys (1995)", "Jurassic Park (1993)", "Mad Max: Fury Road (2015)",
                              "District 9 (2009)", "The Martian (2015)", "Dune (1984)", "Jurassic World Dominion (2022)", "Moonfall (2022)",
                              "Venom: Let There Be Carnage (2021)", "Firestarter (2022)", "Don't Look Up (2021)", "Men (2022)", "The Matrix Resurrections (2021)",
                              "War of the Worlds (2005)", "Corrective Measures (2022)", "Invaders from Mars (1986)", "Crimes of the Future (2022)"]}

print(" ***              WELCOME TO MOVIE RECOMMENDATION SYSTEM               ***")


def rec_mov_list(choice):
    movie_list = movies[choice.lower()]
    result = random.sample(movie_list, 10)
    return result


def mov_list(abc):
    req_list = []
    for i in range(len(rec_mov_list(abc))):
        req_list.append(rec_mov_list(abc)[i])
    return req_list


is_on = True

while is_on:
    print("1.Comdey\n"
          "2.Action\n"
          "3.Romantic\n"
          "4.Horror\n"
          "5.Animated\n"
          "6.Crime\n"
          "7.Science Fiction\n"
          "8.Exit")

    user_input = input("\n Enter Your Genra Choice  : ")
    print("\n")
    if user_input == "1":
        user_input = "comedy"
        print("   ####      Your Recommendations are       ####\n")
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You for using  -_-_-_-_-_")

    elif user_input =="2":
        user_input = "action"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")

    elif user_input == "3":
        user_input = "romantic"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")

    elif user_input == "4":
        user_input = "horror"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")

    elif user_input =="5":
        user_input = "animated"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")

    elif user_input == "6":
        user_input = "crime"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")

    elif user_input == "7":
        user_input = "science fiction"
        for j in range(10):
            print(f"{j + 1}.{rec_mov_list(user_input)[j]}")
        stii_con = input("\n Do you want to Continue(yes/no) : ")
        if stii_con == "yes":
            is_on = True
        else:
            is_on = False
            print("\n _-_-_-_-_-  Thank You  -_-_-_-_-_")
            
    else:
        is_on = False
        print("\n _-_-_-_-_-  Thanks for using Movie Recommendation System  -_-_-_-_-_")
