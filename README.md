# aktiesparekonto-nordnet
Nordnet Aktiesparekonto: find brugbare papirer vha. enten 'bash' eller 'Python' scripts

## Intro
Hvis du har en Aktiesparekonto hos Nordnet, er du måske stødt på dette problem: 
- Mange af de viste værdipapirer er ikke på Skat's positiv liste
- Nordnet viser ikke dette til brugeren, og tilbyder ingen filtreringsmulighed

Eksempel:
- Fremsøg alle ETF'er (Børs & marked -> ETF'er - Børshandlede fonde). Der er ca. 1600
- Check Skats positivliste. Der er ca. 4400 værdipapirer
- Find overlappet mellem de to ovenstående lister. Der er kun ca. 550 værdipapirer

Med andre ord: du handler i blinde, og 2 ud af 3 gange du forøger at købe, risikerer du 
at værdipapiret ikke er på Skats positiv liste.

## Step 1: Download poistivliste og konverter
Hent 'ABIS listen' fra Skat: https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa

Konverter listen til CSV vha din regnearks applikation (jeg bruger LibreOffice Calc)

## Step 2: Download nordnet list
Log ind på Nordnet, og vælge de værdipapirer du er interesseret i. Eksempel:
- Børs & marked -> ETF'er - Børshandlede fonde
- Vælg ikonet som tilbyder funktionen 'Hent som CSV' og download listen.

## Step 3: Hent scripts
Brug Git til at hente disse scripts.

    git clone https://github.com/LarsWH/aktiesparekonto-nordnet.git

## Step 4: Forbered
Nedenståend instruktioner antager at du har 'bash' installeret (f.eks. hvis du kører Linux)

Optional: opret variable til pege på de downloaded filer

    POSITIVLISTE="/mnt/d/Users/lars/Downloads/abis-listen-29042024.csv"
    NORDNET="/mnt/d/Users/lars/Downloads/etf\'er–børshandledefonde_5-17-2024_1628.csv"

Optional: opret variable til pege på resultat-file

    BRUGBAR="brugbar.csv"

## Step 5a: Kør som 'bash' script
Kør scriptet og print resultatet

    source ./skattematch.sh $POSITIVLISTE $NORDNET $BRUGBAR

## Step 5b: Kør som 'Python' script
Alternativt (hvis du ikke kører 'bash') - kør som Python script:

    python3 skattematch.py $POSITIVLISTE $NORDNET $BRUGBAR

## Step 4: Importer
Se resultatet som tekst

    cat $BRUGBAR

Importer resultatfilen i regneark (f.eks. LibreOffice Calc). Nu kan du se de værdipapirer der er egnede til Aktisparekonto.
