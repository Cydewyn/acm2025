# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define full_character_name = "Gene Harker"

define av_narrator = Character(None)
define nvl_narrator = nvl_narrator
define player = Character(full_character_name)

define full_player_name = ""
define pronoun1 = "he"
define pronoun2 = "him"
define pronoun3 = "his"
define pronoun_conjugation = 1

define light_levels = ["broad_daylight","cloudy_daylight","overcast","dark","night"]
default light = light_levels[0]


# The game starts here.

label start:

    av_narrator "Choose your name"
    
    menu:

        "Eugene 'Gene' Harker (he/him)":

            $ full_player_name = "Eugene"
            $ player_name = "Gene"
            $ full_character_name = "Eugene Harker"
            $ pronoun1 = "he"
            $ pronoun2 = "him"
            $ pronoun3 = "his"
            $ pronoun_conjugation = 1

        "Jeanette 'Jean' Harker (she/her)":

            $ full_player_name = "Jeanette"
            $ player_name = "Jean"
            $ full_character_name = "Jeanette Harker"
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "hers"
            $ pronoun_conjugation = 1

        "Jean Harker (she/her)":

            $ full_player_name = "Jean"
            $ player_name = "Jean"
            $ full_character_name = "Jene Harker"
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "hers"
            $ pronoun_conjugation = 1

        "Gene Harker (they/them)":

            $ full_player_name = "Gene"
            $ player_name = "Gene"
            $ full_character_name = "Gene Harker"
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "theirs"
            $ pronoun_conjugation = 2

        "Jean Harker (they/them)":

            $ full_player_name = "Gene"
            $ player_name = "Gene"
            $ full_character_name = "Gene Harker"
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "theirs"
            $ pronoun_conjugation = 2

    #[a black screen, pulsating]

    window show

    nvl clear

    nvl_narrator "You feel as though you are awaking from a nightmare now quickly fading from memory."
    nvl_narrator "You must have been sleeping awhile. {w} Your body is heavy. "
    nvl_narrator "Yet your mind is not rested. {w} The nightmare must have kept it awake during your slumber. "
    nvl_narrator "You push your eyes open, expecting to see the cloth of a pillowcase beneath you…"

    #[flicker vision]

    nvl_narrator "Instead, you are greeted by pastel-colored sand underneath your knees."
    
    nvl clear

    nvl_narrator "You blink your eyes once more, hoping to see a soft bed. "
    #[flicker vision]

    nvl_narrator "The sight does not fade." 
    nvl_narrator "You force yourself awake." 
    nvl_narrator "Your mind begins to think: how did you get here? {w} Why are you here? {w} Where is here?"
    nvl_narrator "You strain your mind to remember.{w}.{w}.{w} Nothing."
    nvl_narrator "The blood rushing through your veins begins to flood your head as your heartbeat quickens." 
    
    nvl clear 

    nvl_narrator "You try to remember anything. {w} Anything at all." 
    nvl_narrator "Only vague shapes and colors emerge from the corners of your mind." 
    nvl_narrator "You blink your eyes again." 

    #[flicker vision]

    nvl_narrator "Nothing. {w} Nothing except…"
    nvl_narrator "Your name. [player_name] Harker." 
    nvl_narrator "You are [player_name] Harker. {w} That’s all you can remember." 
    
    nvl clear 

    window hide 

    scene black

    av_narrator "Having nothing else to do, you push yourself to your feet."

    $ light = light_levels[2]

    show beach_draft
    #[show Harker image]

    av_narrator "You stand on a pastel-colored beach."
    av_narrator "To your right, a shadowy forest looms with its drooping branches and tendrils reaching out for you."
    av_narrator "To your left, the waves of an endless ocean brush over the shore."
    av_narrator "The sky is overcast. {w} Far out in the sea, waves are rising. {w} A storm is coming." 
    av_narrator "You are alone, with only the rustling of trees, the whistling of the wind, and the rumbling of the waves to keep you company." 

    player "Where am I?"

    av_narrator "You cannot recall seeing this landscape before, although it feels familiar." 
    av_narrator "The wind picks up and thunder rumbles in the distance."
    av_narrator "You feel an ominous presence looming over you." 
    av_narrator "You cannot tarry here."


    return