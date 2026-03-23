# Resultater fra Midveis STK1100 - 2026

Utgangspunktet for denne analysen er at på tbaneturen på vei hjem, var mange misfornøyde med midtveis i STK1100. Vi var av den oppfatning at den var vesetnlig vaskskligere enn andre midtveiseksamner, så jeg bestemte meg for å se på dataene, og se om dette stemmer. Jeg sammenligner resulatene fra midtveiseksamen i STK1100 fra 2026, MAT1100 fra 2026 og MAT1105 fra 2025.

### Om de ulike emnene

For å forkare utslagene i datasettene, er det viktig med innsikt i hvem som tar de ulike emnene. MAT1100 er grunnkurs i matematikk, for både fysikere og matematikere. Mye av stoffet i dette kurset er kjent for dem som studerer matematikk, som forklarer den høye andelen som fikk tilnærmet full pott. Dette ga en positivt skjev fordeling, med en vesentlig høyere forventingsverdi enn median. 

Derfor er det mer informativt å sammenligne resulatene med MAT1105 fra 2025, som var et kurs utelukkende for dem som studerer matematikk. Dette vil gi oss et inblikk i hvordan de samme studentene gjør det i to ulike emner.  


#### Behandle data
Det første vi gjør, er å legge resultatene i en fil, slik at vi kan behandle dataen. Deretter leser vi ut resulatene, som legges i en array **a** . Deretter plotter vi dette i et histogram, først et histogram som beskriver den nomenielle fordelingen av antall studenter per poengsum. Histogrammene for de ulike emnene er plottet nedenfor. 

## MAT1100
![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/1100.png)

I resulatene fra MAT1100 ser vi at det er en positiv skjev fordeling. Den høye søylen med full pott kan antas å være matematikkstudenetene, som har var gjennom store deler av pensumet til midtveis i høst. Forventet score på 69% er derfor lite informativ for hvordan det går med matematikkstudentene. Medianen er på 73%, så dette er en positivt skjev fordeling (grunnet de gode resulatne fra matematikkstudentene)
## STK1100
![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/nominell.png)

For STK1100 ser vi at poengscoren er nærmere normalfordelt. Her er det en forvendingsverdi på 61% korrekt, med en median på 60% korrekt. 
## MAT1105
![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/1105.png)

For MAT1105 ser vi at det er en postiv skjev fordeling, men nærmere en normalfordeling enn det MAT1100 er. 



### Median, varians og forveningsverdei
##### Forveningsverdi
Vi beregner den empiriske forveningsverdien ved å bruke utrykket for empirisk forveningsverdi, ved å summere over poengsummene gitt ved $x_i$ for både MAT1100 og STK1100. Da det var 15 oppgaver på MAT1100 og 20 på STK1100, gir målet om gjennomsnittlig prosentvis score mer mening som et mål. Begge regnes med formelen


$$
\mu_{gjennomsnitt} = \frac{1}{n} \sum_{i=1}^{n} x_{i} 
$$ 



Når vi gjør dette for verdiene i dataettet, får vi at **Forventingsverdeien er 69% riktig på MAT1100 og 61 % riktig på STK1100 og 72% rett på MAT1105** . Da fokuset er på endringen fra MAT1105 til STK1100, ser vi at forveningsverdien har falt med 10 prosentpoeng. 

##### Varians

Vi beregner variansen ved å bruke utrykket for empirisk varians for andelen riktige poeng ved de ulike midtveiseksamnene. 


$$
\sigma_{empirisk}^2 = \frac{1}{n^2} \sum_{i=1}^{n} (\frac{x_{i}}{n} -\mu_{forvenitning})^2
$$ 


**Dette gir en varians på 0.04 for STK1100, 0.06 for MAT1100 og 0.04 for MAT1105.** . Dette resulatet passer med forvenintngen om at todelingen av studentene i MAT1100, mellom fysikere og matematikere gir stor sprening i resulatene til midtveis.

##### Median

Når vi skal finne medainen, finner vi antall elementer i listen over resulater, og printer a[ $\frac{n}{2}$ ], som er den poengsummen der halvparten av studentene ligger over, mens halvparten av studentene ligger under. Median er det samme som 0.5-prosentilen. Utregningen fra scriptet viser at **For de ulike fagene MAT1105, MAT1100 og STK1100 er medianene henholsvis 76% rikig, 73% riktig og 60% riktig** . 

## Standarisere til prosentiler, og sammenligne

Ved å bruke percentiler sammenligner vi studentenes relative plassering i resultatfordelingen, i stedet for rå poeng. For eksempel betyr 50-percentilen at man ligger midt i fordelingen, mens 90-percentilen tilsvarer de beste 10 %.

Dette gjør fagene sammenlignbare fordi percentiler ikke påvirkes av hvor mange studenter som har tatt eksamen eller hvor mange poeng det er mulig å få (Da fagene hadde henholsvis 15,17 og 20 poeng som full score). En gitt percentil representerer samme prestasjonsnivå uavhengig av fag. Dermed kan man sammenligne resultater på en rettferdig måte, selv om eksamenene har ulik lengde. Plottet viser at for alle murlige percentiler, så ligger resulatene fra STK1100 vesetnlig lavere. 

![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/japp.png)

### Peace out
