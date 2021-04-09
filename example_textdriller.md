```python
from gascoigne.textdriller import converter
```

to create an extractor, please note you are obliged to specify the url location of the tesseract in your local machine.  
For windows users, If you do not have tesseract, you can download it from here:  
https://github.com/UB-Mannheim/tesseract/wiki


```python
extractor = converter(language="it",tesseract_url="D:\\TESSERACT\\tesseract",treshold_words=20,treshold_language=0.95)
```

### usage example for a scanned pdf document


```python
url_pdf="https://movimento5stelle.s3-eu-west-1.amazonaws.com/spazzacorrotti/regionali/marche-2020/andrea-quattrini-cv.pdf"
```


```python
text = extractor.extract_text(url_pdf)
print(text)
```

    ANDREA QUATTRINI
    Nato a Roma il 02/04/1963
    Residente ad Ancona
    
    Diplomato nel 1982 presso |"Istituto Tecnico Comm.le B.Stracca di Ancona con 50/60.
    Laureato nel 1989 presso la Facolta di Economia e Commercio di Ancona con 100/110.
    
    Ho lavorato negli anni 1989-90 presso la Filiale di Ancona délla societé di revisione Deloitte &
    Touche.
    
    Assunto nel settembre 1990 dal Mediocredito delle Marche, poi Medidcredito Fondiario
    Centroitalia Spa, ho svolto mansioni di tesoreria, titoli ed estero presso il Servizio Finanza.
    
    In particolare, nell’ambito del settore estero, ho curato le trattative ed i perfezionamenti, con
    relativa contrattualistica in lingua inglese, delle operazioni di raccolta che il Mediocredito ha
    stipulato con Banche estere sulla piazza di Londra.
    
    Assunto nel 1998 dalla Cassa di Risparmio di Ascoli Piceno Spa presso la Filiale di Ancona con
    mansioni di addetto titoli. Successivamente ho ricoperto i seguenti ruoli:
    
    1999-2002: Vice Direttore della Filiale di Ancona.
    
    2002-2003: Vice Direttore della Filiale di Jesi.
    
    2003-2004: Direttore della Filiale di Castelfidardo.
    
    2004-2005: Direttore della Filiale di Rieti.
    
    2005-2006: Direttore della Filiale di Ancona.
    
    2006-2007: Gestore Imprese provincie di Ancona e Macerata.
    
    2007-2008: Direttore della Filiale di Porto Recanati.
    
    2008-2013: Direttore della Filiale di Ancona.
    
    Nel] 2013, a seguito della fusione della Cassa di Risparmio di Ascoli Piceno con Banca
    dell’Adriatico (Gruppo Intesa Sanpaolo Spa) e per effetto della riorganizzazione territoriale, la
    Filiale che dirigevo é stata chiusa. Contestualmente, a causa dei miei sempre maggiori impegni in
    politica, ho cambiato ruolo passando al Team Credito Proattivo di Direzione Regionale, come
    Specialista Crediti, mansione ricoperta fino al 2018.
    
    Dal 2019, vista la mia passata esperienza e conoscenza di varie lingue straniere, sono stato
    nominato referente del neo-costituito Team Estero Specialistico di Direzione Regionale, come
    Specialista Estero.
    
    Grado attualmente ricoperto: Quadro Direttivo di 3° livello
    
    In politica sono stato Consigliere comunale MSS e Capogruppo consiliare per due consiliature, dal
    2009 al 2013 e dal 2013 al 2018. Componente della Commissione sport, turismo e politiche
    giovanili durante dal 2009 al 2013 e della Commissione Urbanistica dal 2013 al 2018, oltre a
    partecipare attivamente a tutte le Commissioni come Capogruppo in entrambe le consiliature.
    Membro della Commissione di indagine sulle gravi irregolarita contabili della Fondazione Le Citta
    del Teatro — Teatro Stabile delle Marche durante la consiliatura 2009/2013.
    
    All’interno de! MSS ho coordinato nelle Marche le raccolte firme, le pratiche burocratiche e le
    campagne elettorali delle Politiche 2013, Europee 2014 e Politiche 2018, oltre che per i referendum
    No Euro e No alle modifiche costituzionali.
    
    9/1/2013 red Quattrini
    
    

### usage examples for images


```python
url_image="https://s3-eu-west-1.amazonaws.com/doc-pubblici/20190518220600-cp-certificato.PNG"
text = extractor.extract_text(url_image)
print(text)
```

     
    
    Alnome di:
    ‘cogreme
    some
    
    Date tras
    ope Nasa
    Seseo
    
    static
    rus
    
    Sistema Informativo del Casellario
    Certificato Penale del Casellario Giudiziale
    
    (ART, 25 D.P.A. 14/11/2002 N.313)
    
    CERTIFICATO NUMERO: 5545/2019/R
    
    FRANCESCHINI
    MARIA CRISTINA
    zarvor1969
    
    LUCCA (LU) = ITALIA
    F
    
    INTERESSATO
    AMMINISTRATIVO (ART. 25 D.P.A, 14/11/2002 N.318)
    
    Siattesta che nella Banca dati del Casellario giudiae risuita:
    
    NULLA
    
    [ESTRATTO DA CASELLARLO GIUOIZIALE- PROCURA DELLA REPUBBLICA PRESSO IL TRIBUNALE DI LUCCA
    
    WoeA,1an62018.199 ILresronsasite fa senvZ0 CEATIACATWO
    
    (spAogfriccl AURA)
    
    {pment ete ub see tafe tpt eine lag pte een
    alana (a. 400.8 28 come 2000, 45), aa pte! noua prod ne procederi dpa dale corms
    ‘suimnigzione (dls. 25 glo 1908, n 236. certo & vaio ge presenatn ale eur amma sari,
    
     
    
    
