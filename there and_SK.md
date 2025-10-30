## Prompt 1: Popis pozície AI Prompt Engineer
**Dátum**: 28. október 2025  
**Model**: Gemini  
**Úloha**: Vygenerovať LinkedIn popis

### Prompt:
Ty si kariérny poradca. Napíš krátky, 3-vetový popis pracovnej pozície "AI Prompt Engineer" pre LinkedIn profil. Použi profesionálny, ale prístupný jazyk. Zameriavaj sa na zručnosti ako prompt design, práca s LLM a GCP.

### Výstup
Navrhujem, testujem a optimalizujem prompt design s cieľom maximalizovať výkon a presnosť veľkých jazykových modelov (LLM) pre kritické podnikové aplikácie. Prekladám komplexné obchodné požiadavky do efektívnych vstupov a stratégií pre LLM, čím zabezpečujem relevantné a vysoko kvalitné výstupy. Mám skúsenosti s nasadením a riadením týchto riešení, často využívajúc platformy ako Google Cloud Platform (GCP) pre škálovateľnú a robustnú integráciu AI.

## Prompt 2: Chain-of-Thought – Riešenie logickej úlohy
**Dátum**: 28. október 2025  
**Model**: Gemini, ChatGPT  
**Úloha**: Vyriešiť logický problém krok za krokom

### Prompt:
Máš 3 boxy:  
- Jeden označený "jablko"  
- Jeden označený "pomaranč"  
- Jeden označený "jablko a pomaranč"  

Všetky označenia sú NESPRÁVNE.  
Ak si vyberieš box označený "jablko", akú máš šancu dostať jablko?  
Vysvetli krok za krokom.

#### Gemini:
Toto je klasická logická hádanka. Vzhľadom na to, že **všetky označenia sú NESPRÁVNE**, tvoja šanca, že si z boxu označeného "jablko" vyberieš práve jablko, je **0 % (nulová šanca)**.

### Vysvetlenie krok za krokom

Základom hádanky je fakt, že **žiaden box neobsahuje to, čo je na ňom napísané**.

#### 1. Analýza boxu s nesprávnym označením "jablko a pomaranč"

* V boxe s označením "**jablko a pomaranč**" **nesmú** byť jablko a pomaranč (pretože je označenie nesprávne).
* Preto tento box musí obsahovať buď **iba jablko**, alebo **iba pomaranč**.

#### 2. Kľúčový krok: Výber z boxu "jablko a pomaranč"

* Keďže musíš zistiť obsah všetkých troch boxov len jedným ťahom, **musíš si vybrať z boxu označeného "jablko a pomaranč"**.
* **Prípad A:** Ak si z tohto boxu vytiahneš **jablko**, vieš, že:
    * Box s označením "**jablko a pomaranč**" obsahuje **jablká**.
    * Box s označením "**pomaranč**" nemôže obsahovať pomaranče (nesprávne označenie) a už ani jablká (tie sú v boxe A+P), takže obsahuje **jablko a pomaranč**.
    * Tým pádom box s označením "**jablko**" musí obsahovať **pomaranče**.
* **Prípad B:** Ak si z tohto boxu vytiahneš **pomaranč**, vieš, že:
    * Box s označením "**jablko a pomaranč**" obsahuje **pomaranče**.
    * Box s označením "**jablko**" nemôže obsahovať jablká (nesprávne označenie) a už ani pomaranče (tie sú v boxe A+P), takže obsahuje **jablko a pomaranč**.
    * Tým pádom box s označením "**pomaranč**" musí obsahovať **jablká**.

#### 3. Odpoveď na tvoju otázku

Tvoja otázka však bola: "Ak si vyberieš box označený '**jablko**', akú máš šancu dostať jablko?"

* Box označený "**jablko**" musí mať **nesprávny obsah**.
* Preto **nemôže** obsahovať iba jablká.
* Môže obsahovať **iba pomaranče** alebo **jablko a pomaranč**.
* V oboch prípadoch (ak je v ňom iba pomaranč, alebo mix) však výberom z tohto boxu vopred vieš, že **box neobsahuje iba jablká**.

Preto, ak si vyberieš box označený "**jablko**", máš **0 % šancu**, že sa jedná o box s čistými jablkami. Tvoje šance na **vybratie** jablka z tohto boxu sú buď $100 \%$ (ak je v ňom jablko a pomaranč) alebo $0 \%$ (ak je v ňom iba pomaranč), **ale box sám o sebe nie je to, čo je na ňom napísané.**

**Zhrnutie:** Ak to berieme striktne logicky, box s nesprávnym označením "jablko" **nikdy** neobsahuje len jablká, takže šanca, že **je to box s jablkami**, je 0%.


#### ChatGPT:
Dobrý puzzle — pozrime sa na to krok za krokom. Najprv poviem, aké predpoklady robím, pretože bez nich sa pravdepodobnosť nedá spočítať presne:

**Predpoklady (štandardné pre takýto problém):**

1. Keď povieme „vyberieš box a vezmeš jeden kus ovocia“, myslíme náhodný ťah jedného kusu z toho boxu.
2. „Miešaný“ box obsahuje aspoň jedno jablko aj aspoň jeden pomaranč; pre jednoduchosť predpokladáme, že pri ťahu z miešaného boxu je šanca na jablko = 1/2 (rovnomerné zastúpenie).
3. Nevieme nič viac — všetky usporiadania, ktoré spĺňajú podmienku „všetky označenia sú nesprávne“, považujeme za rovnako možné.

Teraz logika:

1. Označíme boxy podľa toho, čo na nich stojí:

   * (L_A) = box označený „jablko“
   * (L_O) = box označený „pomaranč“
   * (L_{A+O}) = box označený „jablko a pomaranč“

   A obsah každého boxu môže byť buď (A) (len jablká), (O) (len pomaranče) alebo (M) (miešané).

2. Keďže všetky označenia sú nesprávne:

   * (L_A \neq A)
   * (L_O \neq O)
   * (L_{A+O} \neq M)

3. Preto box (L_{A+O}) (označený „jablko a pomaranč“) **nemôže** byť miešaný — musí byť **A** alebo **O**.

4. Zoberieme dva možné prípady:

   **Prípad 1:** (L_{A+O} = A).
   Potom zostávajú pre (L_A) a (L_O) obsah (O) a (M). Keďže (L_O) nesmie byť (O) (označenie by bolo správne), musí byť (L_O = M) a teda (L_A = O).
   => v tomto prípade box označený „jablko“ obsahuje **len pomaranče** (šanca na jablko = 0).

   **Prípad 2:** (L_{A+O} = O).
   Symetricky zostanú pre (L_A) a (L_O) obsah (A) a (M). Keďže (L_A) nesmie byť (A), musí byť (L_A = M) a (L_O = A).
   => v tomto prípade box označený „jablko“ je **miešaný** (šanca na jablko pri jednom náhodnom ťahu = (1/2) podľa nášho predpokladu).

5. Preto z dostupnej informácie sú **presne dva** možné scénare — v jednom je (L_A) iba pomaranče (pravdepodobnosť jablka = 0), v druhom je (L_A) miešaný (pravdepodobnosť jablka = 1/2). Ak považujeme oba scenáre za rovnako pravdepodobné (keďže nemáme inú informáciu), celková pravdepodobnosť dostať jablko pri jednom náhodnom ťahu z boxu (L_A) je
   [
   \frac{1}{2}\cdot 0 + \frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4} = 25%.
   ]

### Zhrnutie

* Ak nešpecifikujeme inak, a ak miešaný box dáva pri ťahu jablko s pravdepodobnosťou (1/2), potom šanca dostať jablko z boxu označeného „jablko“ je **25 %**.
* Poznámka: ak by miešaný box mal inú zložku (napr. nerovnaký počet plodov), alebo ak by sme mali informáciu, že jeden z dvoch možných scenárov je pravdepodobnejší, výsledok by sa zmenil. Ak chcete, môžem prepočítať výsledok pri inej predpokladanej pomere v miešanom boxe.


###Bonus
Grok vymyslel tento prompt - vedel, že odpoveď je 0%. Keď som mu povedal výsledky ostatných tak mal brain-fart a povedal, že obaja sa mýlia a odpoveď je 100%. Potom som ho opravil.

## Prompt 3: Few-Shot – Citát v štýle Elona Muska
**Dátum**: 28. október 2025  
**Model**: Gemini  
**Úloha**: Vygenerovať citát podľa príkladov

### Prompt:
Príklad 1:
Vstup: "Ako zlepšiť produktivitu?"
Výstup: "Pracuj ako keby si mal 24 hodín na záchranu sveta."

Príklad 2:
Vstup: "Čo je úspech?"
Výstup: "Úspech je keď sa ti podarí to, čo iní považujú za nemožné."

Vstup: "Ako prekonať strach?"
Výstup: "Strach prekonáš nie sedením a premýšľaním, ale tak, že vyjdeš von a začneš konať." (Parafráza Dalea Carnegieho)