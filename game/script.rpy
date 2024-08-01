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

label start:
   queue music [ "audio/unsweetened_mint.mp3", "audio/bubbles.mp3" ]

   scene bkg passarela

   "Hey, hello? Acorda! Acorda Sérgio!"

   show alan neutral with dissolve

   "Dormindo na passarela do Dinf? Bem, se levante preciso de você!"

   show alan happy 
 
   "Ah verdade, você não deve estar entendendo nada hahaha"

   show alan neutral 

   "Bem, vamos resumir" 
   
   alan happyn "Quem eu sou? Ah eu sou um espectro do Alan Turing!"

   alan pain "Eu preciso da sua ajuda, pois aconteceu um probleminha..."

   alan rbf "Resumidamente houve uma ruptura no espaço tempo teletransportando figuras
   importantíssimas da computação para os dias de hoje."
   
   alan rbf "Especificamente figuras femininas da computação que agora são estudantes do seu curso..."

   alan scream "OK eu sei que parece loucura (e é um pouco), mas você precisa acreditar, se
   você não me ajudar nessa, e rápido, as criações delas serão apagadas da
   história!"

   alan scream"E não precisa ser um gênio para saber que se isso ocorrer não só a
   computação estará perdida, mas o mundo entrará em colapso!"

   alan neutral "O que você precisa fazer? Bem... eu tenho uma hipótese."
   
   alan happy"Acredito que se você as convencer e as ajudar a recriarem seus trabalhos o espaço-tempo pode
   enfim se normalizar e restaurar a linha do tempo."

   alan scream "ESPERA AÍ!!!" 
   
   alan rbf "Antes, preciso ponderar algumas coisas..."
   
   alan neutral "Primeiro: eu identifiquei três figuras com quem você precisa falar, sendo elas: "
   show alan neutral at right with move
   
   show ada neutral at center with dissolve
   alan neutral "Ada Lovelace"
   hide ada neutral with dissolve

   show grace neutral at center with dissolve
   alan neutral "Grace Hopper"
   hide grace neutral with dissolve

   show hedy neutral at center with dissolve
   alan neutral "E por último, Hedy Lammar."
   hide hedy neutral with dissolve
   show alan neutral at center with move

   alan pain "Segundo: elas não sabem quem são/foram."
   
   alan scream "Essa ruptura tirou a memória delas, portanto não se lembram de seus feitos. Então é
   de suma importância que você as ajude sem falar diretamente sobre quem são ou o que criaram."
   
   alan rbf "A ruptura é muito instável e um choque desses poderia pôr tudo a perder!!"



   label fase1:
      alan neutral"Acho que estou vendo uma delas... Ah sim, você está certo essa é
      Ada Lovelace..."

      scene bkg bib with dissolve
      show alan happy with dissolve
      alan happy "Bem, antes que fale com ela vamos relembrar brevemente seu feito para a computação, Augusta Ada Lovelace criou o primeiro algoritmo da história."
      
      alan happyn "A função do algoritmo era computar os números de Bernoulli!"

      alan happyn "Muito uteis para a programação e matemática, usados para sintetizar somas usando-os em
      sequência ou série."
      
      alan neutral "Seu trabalho foi dividido em notas, a principal foi a nota G, a qual continha um
      passo a passo de uma sequência de operações usando os números de
      Bernoulli."

      alan neutral"Bem como um diagrama demonstrando o funcionamento dessa
      desse passo a passo, ou seja, o algoritmo."
      
      alan happy "Esse algoritmo funcionava como um loop (pois organizava operações em
      grupos que podiam ser repetidos), sendo esse o primeiro algoritmo de
      computador publicado no mundo!"

      alan happyn "Além disso, Lovelace relatou que o funcionamento não se limitava apenas a
      esses números, mas a qualquer objeto que pudesse ser adaptado a notação do
      mecanismo."

      alan scream"Inclusive, previu várias ideias atuais da programação por
      computador!"
      
      alan happy "Como por exemplo que as máquinas poderiam um dia criar até
      mesmo música de qualquer grau de complexidade..."

      alan happyn "Depois dessa simples apresentação, vá ver o que ela está fazendo e cumpra sua missão!"
      hide alan with dissolve

      show ada oh at center with dissolve

      ada "Oh! Olá {color=#FF80AE}Sérgio{/color}! Como vai?"

      ada neutral "O que estou fazendo?"

      ada think "Bem estou tentando resolver um desafio... "

      ada happy "Ele consiste em imaginar que há 2 portas, uma correta e outra falsa"

      ada think "Na frente de cada porta há um guarda. Sabendo que um deles conta apenas
      mentiras e o outro apenas verdades"

      ada "Como eu poderia descobrir a entrada correta
      com apenas uma pergunta?"

      ada oh "Você poderia me ajudar?"

      menu resposta:
         "\"Sim, posso, eu te ajudo e em troca você me ajuda com um problema em organizar uma sequência de operações...\"":
            jump rota_a
         "\"Não, você está perdendo tempo com coisas sem importância!\"":
            jump rota_b
