# Resultater fra Midveis STK1100 - 2026

Utgangspunktet for denne analysen er at på tbaneturen på vei hjem, var mange misfornøyde med midtveis i STK1100. Vi var av den oppfatning at den var vesetnlig vaskskligere enn andre midtveiseksamner, så jeg bestemte meg for å se på dataene, og se om dette stemmer. Jeg sammenligner resulatene fra midtveiseksamen i STK1100 fra 2026, MAT1100 fra 2026 og MAT1105 fra 2025.

### Om de ulike emnene

Siden en stor andel av studentene i MAT1100 er fysikkstudenter, og kritikken i hovedsak retter seg mot vanskelighetsgraden i STK1100, er det mer hensiktsmessig å sammenligne prestasjonene til de samme studentene i MAT1105. Dette emnet ligner mer på STK1100, ettersom begge i hovedsak tas av studenter på bachelorprogrammet i matematikk. Jeg viser imidlertid et plott av skjevfordelingen i MAT1110, for å vise at fysikerenes kritikk at kurset er berettighet. 

Etter at STKFys ble opprettet som et eget kurs, består STK1100 nå i hovedsak kun av matematikkstudenter. Dette gjør sammenligningen mellom MAT1105 og STK1100 til en studie av hvordan de samme studentene gjør det i to ulike emner. Antagelsen er at de samme studentene bør levere omtrent like resulater, gitt at vansklighetsgraden holder seg stabil.


#### Behandle data
Det første vi gjør, er å legge resultatene i en fil, slik at vi kan behandle dataen. Deretter leser vi ut resulatene, som legges i en array **a** . Deretter plotter vi dette i et histogram, først et histogram som beskriver den nomenielle fordelingen av antall studenter per poengsum. Histogrammene for de ulike emnene er plottet nedenfor. 

## MAT1100
![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/fig2.png)

Resultatene fra MAT1100 viser en positivt skjev fordeling. Den høye søylen ved full uttelling kan trolig forklares med matematikkstudentene, som allerede hadde gjennomgått store deler av pensum før midtveis i høstsemesteret. Dermed blir gjennomsnittsscoren på **69 %** mindre representativ for hvordan resten av studentene presterer (altså de som ikke hadde MAT1105 forrigje semester)

Medianen ligger på **73 %**, noe som bekrefter at fordelingen er høyreskjev. Denne skjevheten skyldes i stor grad de sterke resultatene blant matematikkstudentene, som trekker gjennomsnittet opp. Som følge av dette fremstår kritikken fra fysikkstudentene – om at faget oppleves som svært krevende som beretiget.


![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/fig3.png)


For STK1100 er forveningsverdien på **61%** , mens medianen er på **60%** . 


## MAT1105
![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/fig1.png)

MAT1105 har en median på **76%** riktig, og en forvening på **72%** riktig, og er derfor positivt sjev. 

### Feilestimater for sammenligningen


- Mange studenter mener forventet score på MAT1105 er kunstig lav, da mange av oppgavene var regneoppgaver. Vi hadde ikke kalkulator, og da det var en flervalgsprøve, gjorde små regnefeil at man fikk 0 poeng på en oppgave. 
- På MAT1105 og MAT1110 var det 5 svaralternativer per oppgave, mens det var 4 på STK1100. Dette gjør at sansynligheten for rett svar dersom man gjetter er 5 prosentpoeng høyere per oppgave for STK1100. 
Disse momentene taler samlet for at forventingsverdeien i MAT1105 er lavere enn den burde vært, mens forveningen i STK1100 er høyere enn den burde vært. Dermed vil den reele differansen mellom kompetansen til studentene være enda høyre enn tallene viser. Da er spørsmålet, er det studentene eller faget som det er noe galt med? 


### Skjevfordelingen
Skjevfordeling beskriver forholdet mellom medianen og forventningsverdien (gjennomsnittet).

For MAT1105 er gjennomsnittet 72 %, mens medianen er 76 %. Dette innebærer en positiv skjevfordeling, der noen lavere resultater trekker gjennomsnittet ned, mens flertallet av studentene faktisk presterer over forventingsverdien på 72% korrekt. 

For STK1100 er gjennomsnittet 61 %, mens medianen er 60 %. Her ligger disse målene svært nær hverandre, noe som tyder på en tilnærmet symmetrisk fordeling om 0.5-prosentilen. Ved å lage q-q-plott kan vi se hvorhvidt vi kan anta at fordelingen kan tilnærmes med normalfordelingen (som en optimal fordelign skal gjøre)


### Median, varians og forveningsverdei
#### Forveningsverdi
Vi beregner den empiriske forveningsverdien ved å bruke utrykket for empirisk forveningsverdi, ved å summere over poengsummene gitt ved $x_i$ for både MAT1100 og STK1100. Da det var 15 oppgaver på MAT1100 og 20 på STK1100, gir målet om gjennomsnittlig prosentvis score mer mening som et mål. Begge regnes med formelen


$$
\mu_{gjennomsnitt} = \frac{1}{n} \sum_{i=1}^{n} x_{i} 
$$ 



Når vi gjør dette for verdiene i dataettet, får vi at **Forventingsverdeien er 69% riktig på MAT1100 og 61 % riktig på STK1100 og 72% rett på MAT1105** . Da fokuset er på endringen fra MAT1105 til STK1100, ser vi at forveningsverdien har falt med 10 prosentpoeng. 

#### Varians

Vi beregner variansen ved å bruke utrykket for empirisk varians for andelen riktige poeng ved de ulike midtveiseksamnene. 


$$
\sigma_{empirisk}^2 = \frac{1}{n^2} \sum_{i=1}^{n} (\frac{x_{i}}{n} -\mu_{forvenitning})^2
$$ 


**Dette gir en varians på 0.04 for STK1100, 0.06 for MAT1100 og 0.04 for MAT1105.** . Dette resulatet passer med antagelsen om at todelingen av studentene i MAT1100 (fysikere og matematiker) gir stor varians i resulatene fra midtveis.  

#### Median

Når vi skal finne medainen, finner vi antall elementer i listen over resulater, og printer a[ $\frac{n}{2}$ ], som er den poengsummen der halvparten av studentene ligger over, mens halvparten av studentene ligger under. Median er det samme som 0.5-prosentilen. Utregningen fra scriptet viser at **For de ulike fagene MAT1105, MAT1100 og STK1100 er medianene henholsvis 76% rikig, 73% riktig og 60% riktig** . 

## Standarisere til prosentiler, og sammenligne

Ved å bruke percentiler sammenligner vi studentenes relative plassering i resultatfordelingen, i stedet for rå poeng. For eksempel betyr 50-percentilen at man ligger midt i fordelingen, mens 90-percentilen tilsvarer de beste 10 %.

Vi ser at kurven for MAT1105 stort sett ligger over STK1100, noe som betyr at studentene i MAT1105 oppnår høyere andel av maks poeng på alle prosentiler av studentmassen (med unntak i ytterpunktene)

Forskjellen er størst rundt midten av fordelingen. En typisk student (rundt medianen) gjør det altså vesentlig bedre i MAT1105 enn i STK1100. Det er snakk om 10 prosentpoeng i forskjell, noe som er en betraktlig forskjell i nivå. 

Helt på toppen er forskjellen mindre, noe som viser at de beste studentene gjør det bra i begge fag. Totalt sett tyder figuren på at STK1100 er mer krevende, særlig for de som ikke er blant de aller sterkeste.

![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/fig4.png)


### Peace out
