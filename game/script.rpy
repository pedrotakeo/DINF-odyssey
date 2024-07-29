# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ada Lovelace")


# The game starts here.

label start:
    play music "audio/bubbles.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bkg passarela

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ada meh at right
    
    e ""
    
    show ada oh at center
    with move

    # These display lines of dialogue.

    e "Oh! Ola Sergio! Como vai?"
    
    show ada sad
    
    e "ooga booga booga wawa lorem ipsum dolor sit amet wa wa
       wa wa w aw a wa w a wa w  wa wa w aw a wa w a wa w wa wa w aw a wa w a wa w"
     
    show ada neutral
    
    e "ooga booga booga wawa lorem ipsum dolor sit amet wa wa
       wa wa w aw a wa w a wa w  wa wa w aw a wa w a wa w wa wa w aw a wa w a wa w"
    
    show ada think
    
    e "smt mano tlg kkkkkk ooga"

    # This ends the game.

    return
