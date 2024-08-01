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
   show ada sad at center with ease

   ada "Ah, entendi... Bem acho que vou indo para a aula... Até mais {color=#FF80AE}Sérgio{/color}."
   
   "{b}*Ada vai embora visivelmente triste, aparentemente você perdeu a chance de convencer ela...*{/b}"

   hide ada sad with dissolve

   show alan pain with dissolve

   alan "É..." 

   alan rbf "Agora estamos numa enrrascada"

   alan scream "Sem Ada não conseguiremos restaurar a o espaço-tempo! Talvez esteja tudo perdido..."

   alan neutral "Bem, vamos atras das outras, talvez com elas consigamos
   concertar a linha do tempo..."

   hide alan with dissolve

   scene bkg bibdark with dissolve
   stop music fadeout 3.0

   "*Você sente o ar pesado a sua volta, a agitação das pessoas não esconde que tem
   algo errado acontecendo*"

   show alan scream with dissolve
   
   play music "audio/pokemon.mp3" fadein 1.5 loop

   alan "Mal... pelo que consigo ver falhamos na nossa missão, os programas e os próprios computadores não funcionam mais..."

   alan neutral "Isso afetou as demais áreas do mundo, a bolsa de valores do dia pra noite parou de funcionar."

   alan pain "Os sistemas de segurança de todo tipo não fazem mais nada!"

   alan scream "Os sistemas do mundo todo pararam!!!"

   alan neutral "É Sérgio, a ruptura se consolidou e os problemas agora são visíveis... Esse é o começo de uma nova era no mundo."
   
   alan rbf "Porém..."
   
   alan scream "Diferente das outras, não representa avanços, mas sim retrocessos..."

   alan pain "{b}*Alan Turing chateado acena para você e some num passo de mágica.*{/b}"

   hide alan pain with dissolve
   
   "{b}*O mundo após o caos que se alastrou pelo globo...*{/b}"
   
   "{b}*Recomeça.*{/b}"

   stop music fadeout 5.0
   
   "{b}*Alguns especulam que demorarão séculos para se alcançar o progresso que havia antes.*{/b}"
   
   "{b}*Outros dizem até milênios...*{/b}"

   play music "audio/papers.mp3" fadein 5.0 loop

   scene you lose1 with dissolve

   $ renpy.pause()

   stop music fadeout 5.0
return
