$ RENPY_OPEN_FILE_ENCODING = "utf-8"

init python:
   def color_word(text, word, color):
      word_to_color = word
      color_tag = "{color=" + color + "}%s{/color}" % word_to_color
      return text.replace(word_to_color, color_tag)

   # Function to change a word color every time it appears
   # How to use: 
   # config.say_menu_text_filter = lambda text: color_word(text, word=your_word, color=your_color)

define ada = Character(name="Ada Lovelace", image="ada", color="#9175ff")

# Include disabled options in the menu options
define config.menu_include_disabled = True

label start:
   play music "audio/bubbles.mp3" fadein 5.0 loop 
   scene bkg passarela

   "Hey, hello? Acorda! Acorda Sérgio!"

   "Dormindo na passarela do Dinf? Bem, se levante preciso de você!"

   "Ah verdade, você não deve estar entendendo nada hahaha"

   "Bem, vamos resumir" 
   
   "Quem eu sou? Ah eu sou um espectro do Alan Turing!"

   "Eu preciso da sua ajuda, pois aconteceu um probleminha..."

   "Resumidamente houve uma ruptura no espaço tempo teletransportando figuras
   importantíssimas da computação para os dias de hoje."
   
   "Especificamente figuras femininas da computação que agora são estudantes do seu curso..."

   "OK eu sei que parece loucura (e é um pouco), mas você precisa acreditar, se
   você não me ajudar nessa, e rápido, as criações delas serão apagadas da
   história!"

   "E não precisa ser um gênio para saber que se isso ocorrer não só a
   computação estará perdida, mas o mundo entrará em colapso!"

   "O que você precisa fazer? Bem... eu tenho uma hipótese."
   
   "Acredito que se você as convencer e as ajudar a recriarem seus trabalhos o espaço-tempo pode
   enfim se normalizar e restaurar a linha do tempo."

   "ESPERA AÍ!!!" 
   
   "Antes, preciso ponderar algumas coisas..."
   
   "Primeiro: eu identifiquei três figuras com quem você precisa falar, sendo elas: "
   
   show ada neutral
   "Ada Lovelace"
   hide ada neutral

   show grace neutral
   "Grace Hopper"
   hide grace neutral

   show hedy neutral
   "E por último, Hedy Lammar."
   hide hedy neutral

   "Segundo: elas não sabem quem são/foram."
   
   "Essa ruptura tirou a memória delas, portanto não se lembram de seus feitos. Então é
   de suma importância que você as ajude sem falar diretamente sobre quem são ou o que criaram."
   
   "A ruptura é muito instável e um choque desses poderia pôr tudo a perder!!"

   label fase1:
      "Acho que estou vendo uma delas... Ah sim, você está certo essa é
      Ada Lovelace..."

      "Bem, antes que fale com ela vamos relembrar brevemente seu feito para a computação, Augusta Ada Lovelace criou o primeiro algoritmo da história."
      
      "A função do algoritmo era computar os números de Bernoulli!"

      "Muito uteis para a programação e matemática, usados para sintetizar somas usando-os em
      sequência ou série."
      
      "Seu trabalho foi dividido em notas, a principal foi a nota G, a qual continha um
      passo a passo de uma sequência de operações usando os números de
      Bernoulli."

      "Bem como um diagrama demonstrando o funcionamento dessa
      desse passo a passo, ou seja, o algoritmo."
      
      "Esse algoritmo funcionava como um loop (pois organizava operações em
      grupos que podiam ser repetidos), sendo esse o primeiro algoritmo de
      computador publicado no mundo!"

      "Além disso, Lovelace relatou que o funcionamento não se limitava apenas a
      esses números, mas a qualquer objeto que pudesse ser adaptado a notação do
      mecanismo."

      "Inclusive, previu várias ideias atuais da programação por
      computador!"
      
      "Como por exemplo que as máquinas poderiam um dia criar até
      mesmo música de qualquer grau de complexidade..."

      "Depois dessa simples apresentação, vá ver o que ela está fazendo e cumpra sua missão!"

      show ada oh at center with dissolve

      ada "Oh! Olá Sérgio! Como vai?"

      ada neutral "O que estou fazendo?"

      ada think "Bem estou tentando resolver um desafio... "

      ada happy "Ele consiste em imaginar que há 2 portas, uma correta e outra falsa"

      ada think "Na frente de cada porta há um guarda. Sabendo que um deles conta apenas
      mentiras e o outro apenas verdades"

      ada "Como eu poderia descobrir a entrada correta
      com apenas uma pergunta?"

      ada meh "Você poderia me ajudar?"

      menu resposta:
         "\"Sim, posso, eu te ajudo e em troca você me ajuda com um problema em organizar uma sequência de operações...\"":
            jump rota_a
         "\"Não, você está perdendo tempo com coisas sem importância!\"":
            jump rota_b

      label rota_a:
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

         hide ada

         "Muito bem! Confesso que me impressionou!"
         "você conseguiu fazer com que ela recriasse seu grande feito e, como minha hipótese
         previa, a linha do tempo envolvendo Lovelace foi restaurada..."
         "Não temos tempo a perder Sérgio!, vamos encontrar a próxima figura da computação!"
      
      label rota_b:
         pass

   return
