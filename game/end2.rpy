$ RENPY_OPEN_FILE_ENCODING = "utf-8"

init python:
   def color_word(text, word, color):
      word_to_color = word
      color_tag = "{color=" + color + "}%s{/color}" % word_to_color
      return text.replace(word_to_color, color_tag)

   # Function to change a word color every time it appears
   # How to use: 
   # config.say_menu_text_filter = lambda text: color_word(text, word=your_word, color=your_color)

define ada = Character(name="Ada Lovelace", image="ada", color="#FF80AE")
define alan = Character(name="Alan Turing", image="alan", color="#8FD6B5")

# Include disabled options in the menu options
define config.menu_include_disabled = True

label rota_b:
    
    scene bkg bibdark with dissolve
    stop music
    show ada sad at center with dissolve
    ada sad "Oh..."
    show ada sad at right with move
    ada sad "ok..."
    play music "audio/papers.mp3" fadein 5.0 loop
    hide ada with dissolve
    scene you lose1 with dissolve
    $ renpy.pause()
    stop music fadeout 5.0
return

