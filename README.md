# aktiesparekonto-nordnet
Nordnet Aktiesparekonto: find brugbare papirer

Hvis du har en Aktiesparekonto hos Nordnet, er du måske stødt på dette problem: 
- Mange af de viste værdipapirer er ikke på Skat's positiv liste
- Nordnet viser ikke dette til brugeren, og tilbyder ingen filtreringsmulighed

Eksempel:
- Fremsøg alle ETF'er (Børs & marked -> ETF'er - Børshandlede fonde). Der er ca. 1600
- Check Skats positivliste. Der er ca. 4400 værdipapirer
- Find overlappet mellem de to ovenstående lister. Der er kun ca. 550 værdipapirer

Med andre ord: du hanler i blinde, og 2 ud af 3 gange vil du formentlig forsøge købe et 
værdipapir, der ikke er på Skats positiv liste.

## Step 1: download poistivliste
Hent positivlisten fra Skat: https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa

## Step 2: download nordnet list
Log ind på Nordnet, og vælge de værdipapirer du er interesseret i. Eksempel:
- Børs & marked -> ETF'er - Børshandlede fonde
- Vælg ikonet som tilbyder funktionen 'Hent som CSV' og download listen.

## Step 3: Hent script
Brug Git til at hente dette script.

    git clone https://github.com/LarsWH/aktiesparekonto-nordnet.git

## Step 4: Processer
Nedenståend instruktioner antager at du har 'bash' installeret (f.eks. hvis du kører Linux)

Optional: opret variable til pege på de downloaded filer

    POSITIVLISTE="skats-positivliste.csv"
    NORDNET="/mnt/d/Users/lars/Downloads/etf\'er–børshandledefonde_5-17-2024_1628.csv"

Optional: opret variable til pege på resultat-file

    BRUGBAR="brugbar.csv"

Kør scriptet og print resultatet

    source ./skattematch.sh $POSITIVLISTE $NORDNET $BRUGBAR
    cat $BRUGBAR

## Step 4: Importer
Importer resultatfilen i regneark. Jeg bruger LibreOffice Calc