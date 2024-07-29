init python:
   def color_word(text, word, color):
      word_to_color = word
      color_tag = "{color=" + color + "}%s{/color}" % word_to_color
      return text.replace(word_to_color, color_tag)

   # Function to change a word color every time it appears
   # How to use: 
   # config.say_menu_text_filter = lambda text: color_word(text, word=your_word, color=your_color)

   config.say_menu_text_filter = lambda text: color_word(text, word="Sergio", color="#FF80AE")

define ada = Character(name="Ada Lovelace", image="ada", color="#FF80AE")

# Include disabled options in the menu options
define config.menu_include_disabled = True

label start:
   play music "audio/bubbles.mp3"

   scene bkg passarela

   show ada meh at right with dissolve
   pause 1
   ada oh ""
   show ada oh at center with move 
   ada "Oh!"
   ada happy "How are you today my dear Sergio~"
   menu talking_with_sergio:
      
      "\"Doing good\"":
         ada sad "Yeah, me too"
         $ love = False

      "\"I literally love you\"":
         ada oh "Sergio..."
         $ love = True
      
   menu marriage:
      "Propose" if love:
         "Please marry me Ada"
      "Dump her":
         "Fuck off"
         
   return
