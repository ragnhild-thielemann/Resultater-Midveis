# Resultater fra Midveis STK1100 - 2026

Resultatene fra Midtveiseksamen i STK1100 for 2026 har kommet, så jeg syntes det er gøy å se litt på tallene, og hva det kan si om hvordan det går i emnet for den jevne student. 

#### Behandle data
Det første vi gjør, er å legge resultatene i en fil, slik at vi kan behandle dataen. Deretter leser vi ut resulatene, som legges i en array **a** . Deretter plotter vi dette i et histogram, først et histogram som beskriver den nomenielle fordelingen av antall studenter per poengsum, og deretter en sansynlighetsfordeling for de ulike poengsummene, gitt som figur 1 og figur 2. 

![Modelering](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/forventing.png)

![ja](https://github.com/ragnhild-thielemann/Resultater-Midveis/blob/main/images/nominell.png)



#### Median, varians og gjennomsnitt
##### Gjennomsnitt
Vi beregner den empiriske forveningsverdien ved å bruke utrykket for forveningsverdi:


$$
\mu_{empirisk} = \frac{1}{n} \sum_{i=1}^{n} x_{i} 

$$ 


Altså ved å summere de ulike verdiene for poengsummen ved midtveis, gitt som $x_{i}$ 

Når vi gjør dette for verdiene i listen, får vi at **Forventingsverdeien er 12.24 poeng**

##### Varians

Vi beregner variansen ved å bruke utrykket for varians

$$
\sigma_{empirisk}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_{i} -\mu_{empirisk})^2
$$ 

**Dette gir en varians på 15.9** , som forteller oss at spredningen i resulatentene er veldig stor. 

##### Median

Når vi skal finne medainen, finner vi antall elementer i listen over resulater, og printer a[$\frac{n}{2}$], som er den poengsummen der halvparten av studentene ligger over, mens halvparten av studentene ligger under. 



