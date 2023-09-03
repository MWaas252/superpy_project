#**Hierbij een begeleidend verslag waarin drie elementen van de script-implementatie worden belicht, evenals de reden waarom ze zijn gekozen:**_\

##**Command-Line Argumenten Verwerking met argparse:**_\  
De script maakt gebruik van de argparse-bibliotheek
om opdrachtregelargumenten te definieren en te verwerken. Dit stelt gebruikers in staat om invoer 
en instructies te verstrekken bij het uitvoeren van het script vanaf de opdrachtregel. 
De gedefinieerde subcommando's, acties en bijbehorende argumenten verbeteren de bruikbaarheid en modulariteit van het script. 
Door het script te structureren met subcommando's en acties kunnen gebruikers op een intuitieve manier 
met de tool interacteren op basis van hun behoeften, waardoor het script gebruiksvriendelijker wordt. 
Deze ontwerpkeuze vereenvoudigt het proces om de functionaliteit uit te breiden 
door in de toekomst nieuwe subcommando's en acties toe te voegen zonder de kernlogica te wijzigen.

##**Verwerking van Datum en Tijd met datetime en date:**_\  
Het script behandelt bewerkingen met betrekking tot 
datum en tijd door gebruik te maken van de klassen datetime en date uit de datetime-module. Deze klassen 
worden gebruikt om zowel alleen datuminformatie als datum-tijd informatie te beheren, 
waardoor het script in staat is om tijd simulaties uit te voeren en nauwkeurige datumvergelijkingen te maken. 
Het vermogen van het aantal dagen tussen data te berekenen en vervolgens de tijd met die dagen te simuleren, 
toont de flexibiliteit in het omgaan met tijdsgebonden scenario's. Dit is essentieel voor taken zoals het 
controleren van de voorraadstatus voor specifieke datums, evenals het bijhouden van vervaldatums van producten.

##**Gemoduleerde Actiefuncties:**_\  
Het script maakt gebruik van gemoduleerde functies om verschillende acties 
te behandelen, zoals het ophalen van productdetails, tellen van producten en controleren van de status 
van verkochte producten. Deze benadering verbetert de leesbaarheid, onderhoudbaarheid en herbruikbaarheid 
van de code. Elke actie is ingesloten in een aparte functie, waardoor ontwikkelaars zich kunnen richten op 
specifieke functionaliteiten zonder het hoofdscript te overweldigen. Deze ontwerpaanpak bevordert het principe 
van enkelvoudige verantwoordelijkheid (Single Responsibility Principle, SRP) en maakt het gemakkelijker
om problemen op te lossen, uit te breiden en de codebasis bij te werken. Daarnaast biedt deze modulaire 
structuur ruimte voor toekomstige uitbreiding van nieuwe actiefunctionaliteiten.

Ter conclusie, het script toont een ontwerp door gebruik te maken van opdrachtregelargumenten verwerking, 
verwerking van datum en tijd, en een benadering met gemoduleerde functies. 
Deze elementen dragen samen bij aan hulpmiddel dat voldoet aan de vereisten voor het bijhouden van de voorraad, 
terwijl de codekwaliteit en het gebruiksgemak worden gehandhaafd.


##See below voor stock CLI##  

Products in stock info - products : python main.py action products
Products count info - count: python main.py action count
Product details info - details: python main.py action details
Product sold info: python main.py action sold --product "product_name" -- date 2023-08-25

##Advance-time mbt stock##  

Advance-time voor simulatie- of testdoeleinden om de effecten van het verstrijken van de 
tijd op de inventaris en andere gegevens te onderzoeken zonder te wachten op de werkelijke tijd
Advance-time 2 day - python main.py advance-time 2

