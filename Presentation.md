theme: sudodoki/reveal-cleaver-theme
title: CodeWeekEU - Datenvisualisierung für Journalisten
author:
  name: Paul Balzer
  twitter: balzer82
  url: http://codefor.de/dresden
  output: Presentation.html
controls: true

--

![](http://blog.slub-dresden.de/uploads/RTEmagicC_codeweek-slider.png.png)

# Datenvisualisierung für Journalisten
## und Blogger und für dich!

~ Paul Balzer ~

--

## Warum visualisieren?

![](http://mechlab-engineering.de/wordpress/wp-content/uploads/2014/10/visuelle-kommunikation-ausschnitt-595x484.jpg)

The Power of Visual Communication Infographic via [Wyzowl](https://www.wyzowl.com/blog/power-visual-communication-infographic/)

--


## Roadmap heute

* Welche Tools brauche ich?
* Wie bekomme ich das auf meinem PC/Mac zum laufen?
* Daten, was ist das? Exkurs zu XLS, CSV, JSON
* Was sind APIs, wie kommunizieren Rechner?
* Woher bekomme ich Daten?
* Wie bereite ich Daten auf?
* Diagramme erstellen
* Export in Printqualität
* Export für Onlineangebote


--

## Welche Tools brauche ich?

![Why?](http://www.timelinecoverbanner.com/cliparts/wp-content/digital-scrapbooking/neutral-whyyyyy.png)

Es gibt [unendlich viele Tools](http://selection.datavisualization.ch/), die eingesetzt werden können. Wir beschränken uns auf eine gaaaanz kleine Auswahl!


* Python 2.7 mit Zusatzpaketen:
* Pandas (zum Datenhandling)
* Matplotlib (zur Darstellung)
* requests (zur Kommunikation mit APIs)
* mpld3 (für interaktive Onlinegrafiken)


Mehr: http://selection.datavisualization.ch/

--

## Welche Tools brauche ich?

Wir machen keine 1 Click Solution! :(

[1 Click] <========================|==> [Individuell]


Python Distribution Conda:
`http://continuum.io/downloads`

und den Paketmanager PIP:
`http://pip.readthedocs.org/en/latest/installing.html`

--

## Wie bekomme ich das auf meinem PC/Mac zum laufen?

![](http://www.troll.me/images/victory-baby/you-can-do-it-just-try.jpg)

--

## Daten, was ist das?

`11110001001000000`

Unter Daten versteht man im Allgemeinen Angaben, Werte oder formulierbare Befunde, die durch Messung, Beobachtung u. a. gewonnen wurden.


Typische Formate:

* CSV (Comma Seperated Value Datei)
* JSON (JavaScript Object Notation Datei)
* XML (Extensible Markup Language Datei)

alles Textdateien!


--

### Beispiel: CSV (auch Excel)

```
Herausgeber,Nummer,Deckung,Waehrung,Name,Vorname,maennlich,Hobby,Alter,Kind,Partner
Xema,1234-5678-9012-3456,2e+6,EURO,Mustermann,Max,true,Reiten,42,0,0
```

--

### Beispiel: JSON

```
{
  "Herausgeber": "Xema",
  "Nummer": "1234-5678-9012-3456",
  "Deckung": 2e+6,
  "Waehrung": "EURO",
  "Inhaber": {
    "Name": "Mustermann",
    "Vorname": "Max",
    "maennlich": true,
    "Hobbys": [ "Reiten", "Golfen", "Lesen" ],
    "Alter": 42,
    "Kinder": [],
    "Partner": null
  }
}
```

--

### Beispiel: XML

```
<Kreditkarte
  Herausgeber="Xema"
  Nummer="1234-5678-9012-3456"
  Deckung="2e+6"
  Waehrung="EURO">
  <Inhaber
    Name="Mustermann"
    Vorname="Max"
    maennlich="true"
    Alter="42"
    Partner="null">
    <Hobbys>
      <Hobby>Reiten</Hobby>
      <Hobby>Golfen</Hobby>
      <Hobby>Lesen</Hobby>
    </Hobbys>
    <Kinder />
  </Inhaber>
</Kreditkarte>
```

--

## Was sind APIs, wie kommunizieren Rechner?

API (englisch application programming interface, wortwörtlich ‚Anwendungs­programmier­schnittstelle‘)

* Frontend: Google Maps mit Routenplanung
* API dazu: [Google Distance Matrix API](https://developers.google.com/maps/documentation/distancematrix/?hl=de)

--

### Beispiel: Google Distance Matrix API

Frage an die API:
```
http://maps.googleapis.com/maps/api/distancematrix/json?origins=Prager+Str+Dresden&destinations=Kamenzer+Str+Dresden&mode=bicycling&language=de-DE&sensor=false
```

Antwort der API:
```
{
   "destination_addresses" : [ "Kamenzer Straße, 01099 Dresden, Deutschland" ],
   "origin_addresses" : [ "Prager Straße, 01067 Dresden, Deutschland" ],
   "rows" : [
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "3,8 km",
                  "value" : 3778
               },
               "duration" : {
                  "text" : "14 Minuten",
                  "value" : 855
               },
               "status" : "OK"
            }
         ]
      }
   ],
   "status" : "OK"
}
```

--

![Matrix](http://i.huffpost.com/gen/799955/thumbs/o-THE-MATRIX-AND-HINDUISM-facebook.jpg)

-- 

## Woher bekomme ich Daten?

![Daten](http://i.imgur.com/pMHcemY.jpg)

* Wikipedia
* OpenStreetMaps
* APIs
* ...

http://blog.visual.ly/data-sources/

--

![Matrix](http://mechlab-engineering.de/wordpress/wp-content/uploads/2014/10/Headerimage-700x441.jpg)

--

# Fangen wir an!

![Meme](http://i1.kym-cdn.com/photos/images/newsfeed/000/415/209/3b4.png)