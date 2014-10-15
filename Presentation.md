theme: sudodoki/reveal-cleaver-theme
title: CodeWeekEU - Datenvisualisierung für Journalisten
author:
  name: Paul Balzer
  twitter: balzer82
  url: http://codefor.de/dresden
output: Presentation-CodeWeek-DataVis-Journalists.html
controls: true

--

![](http://blog.slub-dresden.de/uploads/RTEmagicC_codeweek-slider.png.png)

# Datenvisualisierung für Journalisten
## und Blogger und weil es fetzt!

~ Paul Balzer ~

--

## Warum visualisieren?

![](http://mechlab-engineering.de/wordpress/wp-content/uploads/2014/10/visuelle-kommunikation-ausschnitt-595x484.jpg)

The Power of Visual Communication Infographic via [Wyzowl](https://www.wyzowl.com/blog/power-visual-communication-infographic/)

--

## Warum visualisieren?

![Infographic by- GO Gulf Web Design Dubai Company](http://www.go-gulf.ae/wp-content/uploads/2014/07/what-people-share-social-networks.jpg)

--

## Was ist Datenjournalismus?

Datenjournalismus (englisch data driven journalism, DDJ) ist eine Form des Online-Journalismus.

Gemäß der Open-Data-Idee bedeutet Datenjournalismus nicht nur die Recherche in Datenbanken, sondern die Sammlung, Aufbereitung, Analyse und Publikation öffentlich zugänglicher Informationen sowie ihre Verarbeitung in klassischen journalistischen Darstellungsformen.

[Quelle: Wikipedia](http://de.wikipedia.org/wiki/Datenjournalismus)

--

## Datenjournalismus-Portale

* [Data Store](http://www.theguardian.com/data) und [Datablog](http://www.guardian.co.uk/news/datablog) von The Guardian
* [Data Desk](http://projects.latimes.com/index/) von The Los Angeles Times
* [Data Blog](http://blog.zeit.de/open-data/) bei Die Zeit
* [Datadrivenjournalism.net](http://datadrivenjournalism.net/). Website zur Konferenz Data Driven Journalism
* [Data Journalism Handbook](http://datajournalismhandbook.org/1.0/en/) der Open Knowledge Foundation
* [Datenjournalismus und Visualisierung mit Open Source Software](http://www.mandalka.name/visualisierung)
* ...



--

# Roadmap heute

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

Es gibt [unendlich viele Tools](http://www.mandalka.name/visualisierung/), die eingesetzt werden können. Wir beschränken uns auf eine gaaaanz kleine Auswahl!

* Python 2.7 mit Zusatzpaketen:
* Pandas (zum Datenhandling)
* Matplotlib (zur Darstellung)
* requests (zur Kommunikation mit APIs)
* mpld3 (für interaktive Onlinegrafiken)


mehr Auswahl:
* http://selection.datavisualization.ch/
* http://www.mandalka.name/visualisierung/

--

## Welche Tools brauche ich?

Wir machen keine 1 Click Solution! :(

[1 Click] <========================|==> [Individuell]


Python Distribution Conda:
`http://continuum.io/downloads`

und den Paketmanager PIP:
`http://pip.readthedocs.org/en/latest/installing.html`

--

### Wie bekomme ich das auf meinem PC/Mac zum laufen?

![](http://www.troll.me/images/victory-baby/you-can-do-it-just-try.jpg)

--

# Daten, was ist das?

`11110001001000000`

Unter Daten versteht man im Allgemeinen: Angaben, Werte oder formulierbare Befunde, die durch Messung, Beobachtung u. a. gewonnen wurden.


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

Im Alltag oft Probleme mit `,` oder `.` (Komma, Dezimalpunkt, Tausendertrennzeichen) Problematik!

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

Bei komplexen Strukturen für den Menschen eher schwer zu lesen. Für den PC easy.

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

Bei komplexen Strukturen für den Menschen eher schwer zu lesen. Für den PC easy.

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

### Beispiel: OpenStreetMaps.org

Frage an die [Overpass API](http://overpass-turbo.eu/s/5rh):
```
<osm-script output="json" timeout="25">
  <query type="way">
    <has-kv k="leisure" v="park"/>
    <bbox-query e="13.7618887424469" n="51.074113200087204" s="51.06796492266171" w="13.752104043960571"/>
  </query>
  <print mode="body"/>
  <recurse type="down"/>
  <print mode="skeleton" order="quadtile"/>
</osm-script>
```

Antwort der API:
```
{
  "version": 0.6,
  "generator": "Overpass API",
  "osm3s": {
    "timestamp_osm_base": "2014-10-13T12:04:02Z",
    "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL."
  },
  "elements": [

{
  "type": "way",
  "id": 4383454,
  "nodes": [
    26750561,
    2972329680,
    369112324,
    3013620425,
	...
	  ],
  "tags": {
    "alt_name": "Alaunpark",
    "leisure": "park",
    "name": "Alaunplatz",
    "wheelchair": "yes",
    "wikipedia": "de:Alaunplatz"
  }
},
```

oder als [GeoJSON](https://gist.github.com/anonymous/28244576babfd484e63f)

--

![Matrix](http://i.huffpost.com/gen/799955/thumbs/o-THE-MATRIX-AND-HINDUISM-facebook.jpg)

-- 

## Woher bekomme ich Daten?

![Daten](http://i.imgur.com/pMHcemY.jpg)

* Wikipedia
* OpenStreetMaps
* APIs ([API Verzeichnis](http://www.programmableweb.com/apis/directory))
* Scrapen
* ...

http://blog.visual.ly/data-sources/

--

![Matrix](http://mechlab-engineering.de/wordpress/wp-content/uploads/2014/10/Headerimage-700x441.jpg)

--

# Fangen wir an!

![Meme](http://i1.kym-cdn.com/photos/images/newsfeed/000/415/209/3b4.png)

--

"Wir sehen im Thema Datenjournalismus einen ganz wichtigen Baustein in den Darstellungsformen, die uns zur Verfügung stehen – keine Mode-Erscheinung.
Diese Skills werden wir durch immer wieder neue Projekte ausbauen und anwenden."

Sascha Venohr, Entwicklungsredakteur bei Zeit Online, über die Datenjournalismus-Strategie seiner Redaktion. [Quelle](http://www.mediummagazin.de/magazin-plus/thema-datenjournalismus-das-beispiel-zeit-online/)

--

## Weiter

[Programmier Crashkurs für Journalisten](http://www.digitalerwandel.de/2012/07/16/programmier-crashkurs-fuer-journalisten/) - Digitaler Wandel

[Visualisierungshilfen für den Datenjournalismus](http://edoc.sub.uni-hamburg.de/haw/volltexte/2014/2416/pdf/bachelorarbeit_alexander_salenko.pdf) - Bachelorarbeit von Alexander Salenko