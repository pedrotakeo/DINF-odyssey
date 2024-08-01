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

label rota_a:
   scene bkg bib
   show ada happy at center with dissolve
   ada happy "Viva!! Bem vamos começar então..."

   "{b}*vocês concluem o desafio que Ada enfrentava usando os
   conhecimentos adquiridos nas aulas de ICC*{/b}"

   ada happy "Muito obrigado!!"

   ada think "Mas agora deixe-me ver seu problema..."

   ada happy "Ah sim... usando numeros de Bernoulli... Acho q tive uma ideia de como fazer..."

   "{b}*Ada Lovelace começa a escrever como se algo dentro dela soubesse
   exatamente o que fazer*{/b}"

   "{b}*Logo ela termina e mostra o que parece ser exatamente
   o primeiro algoritmo da história, assim como foi escrito no passado...*{/b}"
      
   "{b}*Dessa forma, Lovelace desaparece em um piscar de olhos*{/b}"
   hide ada with dissolve

   show alan happy

   alan happy "Muito bem! Confesso que me impressionou!"
   alan happyn "você conseguiu fazer com que ela recriasse seu grande feito e, como minha hipótese
   previa, a linha do tempo envolvendo Lovelace foi restaurada..."
   alan scream "Não temos tempo a perder Sérgio!, vamos encontrar a próxima figura da computação!"
   hide alan with dissolve
   play music "audio/suki.mp3" fadein 5.0 loop

   scene win with dissolve

   $ renpy.pause()

   stop music fadeout 5.0
return
