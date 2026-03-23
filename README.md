# Resultater fra Midveis STK1100 - 2026

Resultatene fra Midtveiseksamen i STK1100 for 2026 har kommet, så jeg syntes det er gøy å se litt på tallene, og hva det kan si om hvordan det går i emnet for den jevne student. 

#### Behandle data
Det første vi gjør, er å legge resultatene i en fil, slik at vi kan behandle dataen. Deretter leser vi ut resulatene, som legges i en array **a** . Deretter plotter vi dette i et histogram, først et histogram som beskriver den nomenielle fordelingen av antall studenter per poengsum, og deretter en sansynlighetsfordeling for de ulike poengsummene, gitt som figur 1 og figur 2. 

![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/nominell.png)

![ja](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/sansynlighet.png)



### Median, varians og gjennomsnitt
##### Gjennomsnitt
Vi beregner den empiriske forveningsverdien ved å bruke utrykket for empirisk forveningsverdi, ved å summere over poengsummene gitt ved $x_i$:


$$
\mu_{empirisk} = \frac{1}{n} \sum_{i=1}^{n} x_{i} 
$$ 




Når vi gjør dette for verdiene i dataettet, får vi at **Forventingsverdeien er 12.24 poeng** . Forventet antall poeng for en tilfeldig valgt student er altså litt over halvparten riktige svar.

##### Varians

Vi beregner variansen ved å bruke utrykket for empirisk varians for poengsummene $x_i$


$$
\sigma_{empirisk}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_{i} -\mu_{empirisk})^2
$$ 


**Dette gir en varians på 15.9** , som forteller oss at spredningen i resulatentene fra midtveis er veldig stor. 

##### Median

Når vi skal finne medainen, finner vi antall elementer i listen over resulater, og printer a[ $\frac{n}{2}$ ], som er den poengsummen der halvparten av studentene ligger over, mens halvparten av studentene ligger under. Median er det samme som 0.5-prosentilen. Utregningen fra scriptet viser at **Medianen ligger på 12 poeng** . 

### Normalfordeling

Vi lager et q-q-plott for å se om poengene fra midtveis kan tilnærmes med en normalfordeling. Vi finner prosnetilene til den sorterte listen **a** , ved formelen 


$$
p_i = \frac{i-0.5}{n} $$


Dette gir følgene q-q-plot:

Vi ser at punktene ligger tilnærmet langs en rett linje for verdiene i midten, noe som tyder på at poengsummene rundt forventningsverdien kan antas å være tilnærmet normalfordelte. Vi har imidlertid beregnet et relativt høyt variansnivå, $\sigma^2 = 15,9$, som innebærer at den tilhørende normalfordelingen vil ha stor spredning. Dette betyr at verdiene er ganske varierte, og at avvikene fra forventningsverdien på 12.24 poeng kan være store.



