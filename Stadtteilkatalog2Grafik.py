# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ![CodeWeek Logo](http://blog.slub-dresden.de/uploads/RTEmagicC_codeweek-slider.png.png)

# <headingcell level=1>

# Zusammenhänge aus Zahlen finden.
# 
# Beispiel: Dresden Stadtteilkatalog

# <markdowncell>

# [Dresden Stadtteilkatalog](http://www.dresden.de/de/02/06/stadtteilkatalog.php)

# <markdowncell>

# Zuerst ein paar Python Pakete importieren, die wir zum Bearbeiten der Daten benötigen

# <codecell>

import pandas as pd
import seaborn as sns
sns.set_style("whitegrid")

# <headingcell level=2>

# Wohnungsleerstand

# <markdowncell>

# Wohnungsleerstand von http://www.dresden.de/de/02/06/auskunft/medien/DD_STadtteilkatalog.htm

# <codecell>

daten='''Codes	Names	2005	2006	2007	2008	2009	2010	2011	
01	Innere Altstadt	15,35	22,58	18,77	16,84	15,92	15,38	14,69	
02	Pirnaische Vorstadt	13,96	15,32	8,18	7,98	7,55	5,91	5,06	
03	Seevorstadt-Ost	18,44	19,47	12,90	4,41	3,78	3,49	3,34	
04	Wilsdruffer Vorstadt/Seevorstadt-West	8,31	7,81	6,22	6,21	6,71	5,97	6,06	
05	Friedrichstadt	26,69	24,34	21,17	18,75	17,33	16,00	13,40	
06	Johannstadt-Nord	12,07	10,71	9,85	9,52	8,23	10,76	10,77	
07	Johannstadt-Süd	5,77	5,11	5,45	4,75	5,45	5,76	5,03	
11	Äußere Neustadt (Antonstadt)	13,70	12,19	10,84	10,13	8,73	8,33	7,61	
12	Radeberger Vorstadt 	16,35	14,50	12,32	11,84	10,88	11,77	10,12	
13	Innere Neustadt	17,77	16,80	15,32	14,65	13,91	10,58	9,22	
14	Leipziger Vorstadt 	18,77	17,04	15,01	13,90	12,12	9,35	8,67	
15	Albertstadt 	32,23	30,61	30,00	30,62	31,63	23,84	18,15	
21	Pieschen-Süd	23,10	20,89	18,65	15,92	12,95	11,81	10,68	
22	Mickten	19,04	17,67	14,99	12,56	12,16	11,95	10,88	
23	Kaditz	18,12	13,10	12,46	11,12	9,41	9,90	9,31	
24	Trachau	12,29	10,37	9,76	8,79	8,78	8,40	7,80	
25	Pieschen-Nord/Trachenberge	19,33	17,70	15,18	14,07	12,04	10,75	9,20	
31	Klotzsche	13,43	11,60	10,28	9,57	9,33	9,05	8,03	
32	Hellerau/Wilschdorf	14,66	9,63	8,10	7,73	7,87	7,78	6,89	
35	Weixdorf	16,00	7,36	5,97	5,45	5,16	5,84	5,40	
36	Langebrück/Schönborn	16,47	9,97	9,07	8,20	8,04	9,11	7,71	
41	Loschwitz/Wachwitz	22,19	17,74	14,29	13,17	13,20	15,03	13,51	
42	Bühlau/Weißer Hirsch	19,37	15,10	13,14	12,78	11,81	12,64	11,17	
43	Hosterwitz/Pillnitz	20,48	15,85	11,78	11,65	11,91	12,43	10,79	
45	Weißig	14,53	10,89	9,82	10,04	9,15	9,40	8,56	
46	Gönnsdorf/Pappritz	14,42	7,96	6,44	6,04	5,31	6,25	5,86	
47	Schönfeld/Schullwitz	17,54	9,92	8,22	8,05	8,03	9,13	8,66	
51	Blasewitz	17,21	14,77	12,68	12,54	12,10	12,25	10,50	
52	Striesen-Ost	11,01	11,09	9,43	9,22	8,35	8,32	7,43	
53	Striesen-Süd	9,84	8,81	6,59	5,90	4,66	4,31	3,83	
54	Striesen-West	8,96	8,78	7,86	7,20	5,88	5,79	5,63	
55	Tolkewitz/Seidnitz-Nord	19,80	17,32	16,41	16,29	19,00	19,14	16,69	
56	Seidnitz/Dobritz	10,91	11,01	9,64	7,31	6,17	6,17	5,66	
57	Gruna	12,89	10,48	7,82	7,46	5,98	5,80	5,38	
61	Leuben	15,65	11,99	11,12	10,46	8,78	8,48	7,27	
62	Laubegast	13,10	10,76	9,44	9,01	8,21	8,26	6,51	
63	Kleinzschachwitz	15,16	11,89	10,99	10,36	9,65	8,68	8,07	
64	Großzschachwitz	17,23	16,24	14,46	13,32	11,34	10,94	9,41	
71	Prohlis-Nord	19,57	16,76	13,71	12,95	12,99	10,54	10,46	
72	Prohlis-Süd	17,82	15,62	11,99	12,64	11,63	8,92	6,30	
73	Niedersedlitz	25,49	28,19	25,75	23,17	21,64	23,06	7,41	
74	Lockwitz	18,36	13,72	12,06	11,48	11,22	11,64	9,79	
75	Leubnitz-Neuostra	13,58	10,98	8,58	8,15	7,52	6,74	6,03	
76	Strehlen	19,83	19,87	14,41	15,80	19,41	15,24	6,95	
77	Reick	20,76	15,22	12,07	8,41	7,88	6,15	5,98	
81	Südvorstadt-West	8,88	7,78	5,84	5,40	5,63	5,59	4,67	
82	Südvorstadt-Ost	11,46	8,86	5,45	7,02	6,44	6,69	5,55	
83	Räcknitz/Zschertnitz	12,61	12,33	9,36	5,32	5,05	4,76	4,02	
84	Kleinpestitz/Mockritz	9,92	9,18	8,30	7,83	7,36	7,53	6,75	
85	Coschütz/Gittersee	17,91	15,55	12,68	11,67	12,06	12,25	11,39	
86	Plauen	12,64	11,78	10,59	9,19	8,23	7,93	6,82	
90	Cossebaude/Mobschatz/Oberwartha	20,16	15,62	13,37	12,29	12,01	11,98	11,30	
91	Cotta	21,60	21,02	18,30	16,46	14,88	13,67	11,34	
92	Löbtau-Nord	23,18	20,91	19,63	18,38	16,70	15,92	14,89	
93	Löbtau-Süd	18,16	16,49	15,34	13,94	11,52	10,06	8,46	
94	Naußlitz	20,93	17,52	16,23	15,63	14,66	14,94	14,59	
95	Gorbitz-Süd	16,46	9,29	7,57	8,39	7,17	7,44	7,00	
96	Gorbitz-Ost	14,65	12,64	10,90	9,12	9,71	8,89	8,13	
97	Gorbitz-Nord/Neu-Omsewitz	14,77	15,03	17,96	14,74	8,85	8,29	7,29	
98	Briesnitz	21,25	17,47	15,63	14,27	13,41	13,75	12,53	
99	Altfranken/Gompitz	11,99	8,00	6,98	6,94	6,07	6,57	6,64	'''

# <markdowncell>

# Die nachfolgende Funktion wandelt das rohe Textformat (siehe oberhalb) in ein Array und Dictionary, welches wir nutzen können um einen Datenframe in [Python Pandas](http://pandas.pydata.org/) anzulegen

# <codecell>

def text2dataframe(text):
    data={}
    for i,row in enumerate(text.split('\n')):
        d = row.split('\t')
        #print i, d
        if i==0:
            years = pd.to_datetime(d[2:9])
        else:
            try:
                data[d[1]] = [leerstand.replace(',','.') for leerstand in d[2:9]]
            except:
                pass
            
    return years, data

# <codecell>

# Rohdaten in Array und Dictionary wandeln
years, data = text2dataframe(daten)

# <markdowncell>

# DatenFrame erzeugen
# 
# * Daten = Zahlen
# * Index = Jahre

# <codecell>

df = pd.DataFrame(data=data, index=years)
df = df.convert_objects(convert_numeric=True) # Text in Zahlen umwandeln

# <headingcell level=4>

# Diagramme erzeugen

# <codecell>

%matplotlib inline
import matplotlib.pylab as plt

# <markdowncell>

# Schauen wir uns doch mal an, wie der DatenFrame aussieht

# <codecell>

df

# <markdowncell>

# Ein paar statistische Aussagen mit `.describe()`

# <codecell>

df.describe()

# <headingcell level=3>

# Wohnungsleerstand Varianz

# <markdowncell>

# Die Varianz ist ein Streuungsmaß, welches die Verteilung von Werten um den Mittelwert kennzeichnet. Sie ist das Quadrat der Standardabweichung.

# <codecell>

leerstandsvarianz = df.std()**2.0 # Varianz aus Standardabweichung berechnen

leerstandsvarianz.sort(inplace=True) # sortieren
leerstandsvarianz.plot(kind='barh', figsize=(7,12)) # Darstellung

plt.title('Wohnungsleerstand-Varianz zw. 2008 - 2011') # Titel
plt.tight_layout() # ordentlich formatieren
plt.savefig('Varianz-Wohnungsleerstand-Dresden.png', dpi=150) # abspeichern

# <markdowncell>

# Schauen wir uns mal ein paar Stadtteile mit hoher und niedriger Varianz an

# <codecell>

df[['Niedersedlitz','Seevorstadt-Ost','Johannstadt-Süd']].plot(kind='area', stacked=False, figsize=(6,3))
plt.ylabel('[%]')
plt.title('Wohnungsleerstand in Dresden')
plt.savefig('Wohnungsleerstand.png', dpi=150)

# <codecell>


# <headingcell level=2>

# PKW Bestand

# <markdowncell>

# Wir möchten eine Story zu PKW und Urbanisierung schreiben. Wir benötigen ein paar Informationen dazu.

# <codecell>

from IPython.display import HTML
HTML('<iframe src=http://www.spiegel.de/auto/aktuell/liste-der-staedte-mit-der-groessten-autodichte-a-845878.html width=1000 height=650></iframe>')

# <markdowncell>

# OK. Die haben eine Studie. Wir holen uns die Daten selbst.
# 
# Quelle: http://www.dresden.de/de/02/06/auskunft/medien/DD_STadtteilkatalog-Dateien/sheet007.htm

# <codecell>

pkw='''Codes	Names	2005	2006	2007	2008	2009	2010	2011	2005	2006	2007	2008	2009	2010	2011	2003	2004	2005	2006	2007	2008	2009	2010	2003	2004	2005	2006	2007	2008	2009	2010	2003	2004	2005	2006	2007	2008	2009	2010	2005	2006	2007	2008	2009	2010	2011	2005	2006	2007	2008	2009	2010	2011	
01	Innere Altstadt	482	473	398	393	404	426	438	21,3	21,8	13,9	12,7	43,0	42,0	48	236,0	262,0	254,0	284,0	286,0	277,0	289,0	285,0	88,0	97,0	94,0	97,0	101,7	94,0	94,0	96,0	32,0	46,0	47,0	48,0	55,0	52,0	57,0	56,0	0,0	0,0	0,0	0,0	0,0	0,0	0,0	 	 	 	 	 	 	
02	Pirnaische Vorstadt	419	419	363	367	367	363	356	11,2	11,2	10,5	10,6	9,0	9,0	9	26,0	28,0	32,0	31,0	31,0	28,0	29,0	26,0	3,0	3,0	4,0	4,0	3,7	3,0	4,0	3,0	1,0	2,0	2,0	2,0	2,1	2,0	2,0	2,0	293,9	375,9	323,8	269,9	197,0	180,0	191,0	14,0	14,8	18,3	19,0	19,8	20,0	20	
03	Seevorstadt-Ost	520	538	480	448	450	448	431	13,3	18,0	19,0	18,0	19,0	23,0	20	51,0	54,0	57,0	57,0	56,0	56,0	63,0	67,0	10,0	11,0	11,0	11,0	11,2	11,0	14,0	15,0	5,0	7,0	7,0	7,0	6,5	6,0	7,0	8,0	81,6	84,5	178,3	170,8	148,0	166,0	169,0	18,1	18,9	19,0	19,0	20,1	19,8	20,9048	
04	Wilsdruffer Vorstadt/Seevorstadt-West	516	512	452	455	459	457	453	17,8	20,5	16,4	16,4	22,0	22,0	21	68,0	72,0	75,0	74,0	77,0	76,0	75,0	78,0	5,0	5,0	6,0	6,0	5,7	7,0	5,0	5,0	2,0	4,0	4,0	4,0	4,0	4,0	4,0	3,0	147,7	136,8	143,4	211,9	112,0	155,0	139,0	18,9	19,3	21,4	20,1	21,6	22,1	17,6667	
05	Friedrichstadt	447	454	381	381	365	376	378	62,6	55,7	60,7	58,9	58,0	64,0	59	82,0	89,0	86,0	84,0	85,0	87,0	84,0	85,0	5,0	5,0	5,0	5,0	5,2	6,0	5,0	4,0	2,0	6,0	5,0	5,0	5,6	6,0	5,0	5,0	99,2	103,1	100,0	99,3	82,0	76,0	72,0	17,7	18,7	18,0	19,0	18,5	18,0	18,3333	
06	Johannstadt-Nord	621	617	549	548	545	538	534	20,2	23,1	27,2	27,1	31,0	32,0	33	37,0	39,0	39,0	40,0	41,0	42,0	42,0	40,0	4,0	4,0	4,0	4,0	3,8	4,0	4,0	4,0	1,0	2,0	2,0	2,0	1,8	2,0	2,0	2,0	82,5	84,6	75,7	80,8	71,0	79,0	79,0	16,6	16,1	15,9	16,3	17,3	19,3	19,8462	
07	Johannstadt-Süd	619	624	571	567	567	566	559	19,6	18,7	21,3	21,2	24,0	26,0	25	18,0	18,0	19,0	20,0	21,0	21,0	20,0	21,0	2,0	3,0	3,0	3,0	3,3	3,0	3,0	3,0	0,0	0,0	0,0	0,0	0,3	0,0	0,0	0,0	248,6	232,0	236,6	216,8	207,0	219,0	213,0	19,3	19,4	17,9	18,6	17,6	17,7	18,75	
11	Äußere Neustadt (Antonstadt)	321	325	295	295	310	316	315	13,7	13,4	13,7	13,5	14,0	14,0	15	73,0	76,0	79,0	75,0	73,0	75,0	72,0	71,0	14,0	15,0	15,0	14,0	12,3	12,0	12,0	11,0	7,0	11,0	11,0	10,0	9,5	10,0	10,0	10,0	51,8	50,1	49,1	45,9	38,0	41,0	60,0	17,4	18,2	19,0	19,9	21,1	23,0	23,5769	
12	Radeberger Vorstadt 	732	751	654	649	671	682	689	24,3	27,6	28,4	28,0	34,0	36,0	36	57,0	65,0	70,0	75,0	76,0	78,0	79,0	77,0	2,0	3,0	3,0	3,0	4,1	4,0	4,0	4,0	1,0	2,0	3,0	3,0	2,8	3,0	3,0	3,0	85,0	84,7	77,8	70,9	47,0	73,0	68,0	22,3	24,6	25,1	23,7	23,2	23,4	23,8846	
13	Innere Neustadt	543	541	484	481	484	478	487	65,9	62,4	64,5	63,2	68,0	65,0	67	114,0	121,0	123,0	121,0	121,0	125,0	129,0	123,0	17,0	17,0	19,0	19,0	19,0	20,0	18,0	17,0	6,0	8,0	9,0	9,0	6,3	7,0	8,0	8,0	197,2	180,6	176,6	179,6	156,0	165,0	161,0	21,9	22,7	22,9	22,0	22,3	22,6	22,8462	
14	Leipziger Vorstadt 	422	422	383	390	389	391	387	4,3	4,1	4,0	3,8	2,0	2,0	2	34,0	37,0	38,0	38,0	39,0	38,0	38,0	39,0	4,0	4,0	4,0	4,0	4,0	4,0	4,0	3,0	2,0	3,0	4,0	3,0	3,3	3,0	3,0	3,0	50,9	50,6	45,8	39,6	44,0	53,0	50,0	20,2	20,6	21,7	22,8	23,8	24,3	24,0769	
15	Albertstadt 	770	758	701	717	702	739	727	0,0	0,0	0,0	0,0	0,0	0,0	0	122,0	122,0	116,0	115,0	117,0	131,0	135,0	121,0	5,0	5,0	5,0	5,0	6,0	7,0	7,0	7,0	3,0	6,0	7,0	6,0	5,5	6,0	6,0	5,0	88,8	89,7	97,8	85,3	110,0	53,0	49,0	 	 	 	 	 	 	
21	Pieschen-Süd	476	486	425	427	436	449	453	43,3	43,3	42,2	40,6	36,0	39,0	39	46,0	48,0	48,0	49,0	48,0	48,0	46,0	45,0	7,0	8,0	8,0	8,0	6,6	7,0	7,0	7,0	3,0	4,0	4,0	3,0	3,2	3,0	2,0	3,0	54,3	59,9	73,4	74,8	58,0	68,0	71,0	19,4	20,4	21,3	20,8	22,1	21,8	22,2	
22	Mickten	693	688	629	623	625	639	637	8,4	10,9	14,1	13,7	12,0	14,0	11	39,0	40,0	42,0	42,0	42,0	42,0	42,0	43,0	4,0	4,0	4,0	4,0	4,0	4,0	5,0	4,0	2,0	3,0	3,0	3,0	2,8	3,0	3,0	2,0	60,6	61,9	64,6	57,6	56,0	55,0	53,0	20,5	19,1	19,9	19,9	19,9	21,9	22,9167	
23	Kaditz	807	807	736	733	749	762	762	4,0	3,8	3,8	3,7	4,0	4,0	4	45,0	49,0	52,0	49,0	50,0	53,0	55,0	56,0	6,0	7,0	7,0	7,0	7,0	7,0	11,0	11,0	2,0	3,0	3,0	3,0	3,6	4,0	4,0	4,0	43,8	43,9	40,8	37,5	30,0	68,0	69,0	20,1	21,0	20,9	22,1	21,1	19,0	19,5556	
24	Trachau	798	794	744	738	746	754	754	15,2	17,0	19,0	18,9	15,0	19,0	18	30,0	33,0	33,0	32,0	32,0	33,0	32,0	32,0	3,0	3,0	3,0	3,0	3,0	3,0	2,0	3,0	0,0	1,0	2,0	2,0	1,4	1,0	1,0	1,0	63,5	60,3	67,9	66,1	59,0	58,0	55,0	26,1	24,4	23,0	22,8	21,7	21,8	22,5833	
25	Pieschen-Nord/Trachenberge	639	646	586	587	591	592	600	6,5	8,2	8,0	7,9	8,0	8,0	7	41,0	46,0	48,0	48,0	50,0	51,0	50,0	51,0	4,0	4,0	5,0	5,0	4,5	5,0	5,0	5,0	2,0	3,0	3,0	3,0	3,1	3,0	3,0	3,0	89,9	92,2	92,6	89,7	82,0	86,0	81,0	21,4	20,9	20,8	21,1	21,6	21,5	22,2778	
31	Klotzsche	876	877	812	815	814	824	828	14,1	14,2	14,1	14,1	16,0	18,0	17	30,0	33,0	35,0	38,0	40,0	40,0	40,0	40,0	3,0	3,0	4,0	4,0	4,1	4,0	4,0	3,0	1,0	2,0	2,0	2,0	2,0	2,0	2,0	2,0	91,6	100,4	103,7	99,1	91,0	99,0	101,0	20,6	20,7	21,9	22,0	19,9	21,4	21,55	
32	Hellerau/Wilschdorf	1178	1194	1098	1109	1132	1132	1139	4,8	4,8	4,8	4,8	6,0	6,0	8	49,0	53,0	56,0	59,0	59,0	59,0	58,0	57,0	4,0	4,0	6,0	6,0	4,6	4,0	5,0	5,0	1,0	3,0	3,0	3,0	2,6	2,0	3,0	3,0	60,2	64,5	67,3	63,7	57,0	79,0	78,0	20,5	22,8	25,3	23,5	23,7	24,2	23,5714	
35	Weixdorf	1213	1262	1155	1158	1152	1169	1176	6,7	6,7	6,8	6,7	8,0	8,0	7	41,0	43,0	45,0	44,0	46,0	47,0	46,0	48,0	5,0	6,0	6,0	6,0	6,1	6,0	7,0	7,0	2,0	4,0	4,0	4,0	3,0	3,0	2,0	2,0	86,2	80,9	79,2	78,7	66,0	67,0	72,0	22,3	23,4	24,6	24,5	22,9	23,3	21,8	
36	Langebrück/Schönborn	1229	1239	1152	1147	1142	1139	1146	7,1	7,1	4,8	4,8	2,0	2,0	5	32,0	34,0	41,0	44,0	44,0	41,0	41,0	42,0	3,0	4,0	3,0	3,0	3,4	3,0	3,0	3,0	0,0	1,0	1,0	1,0	1,2	1,0	1,0	1,0	68,6	66,8	65,7	67,1	53,0	64,0	62,0	18,6	20,0	21,1	22,1	22,4	21,6	22	
41	Loschwitz/Wachwitz	1030	1059	928	932	952	966	976	7,8	7,8	7,6	7,4	13,0	11,0	13	62,0	65,0	67,0	70,0	74,0	78,0	76,0	76,0	5,0	5,0	5,0	5,0	6,7	7,0	7,0	7,0	2,0	3,0	4,0	4,0	4,2	4,0	4,0	3,0	26,3	27,3	29,2	28,3	23,0	58,0	60,0	22,8	24,5	23,4	22,0	21,0	21,4	24,25	
42	Bühlau/Weißer Hirsch	966	992	898	913	923	934	940	26,4	26,8	27,7	27,7	30,0	29,0	32	53,0	57,0	60,0	60,0	62,0	62,0	63,0	63,0	4,0	4,0	5,0	5,0	4,2	4,0	4,0	4,0	1,0	3,0	3,0	3,0	2,2	2,0	2,0	3,0	60,9	63,6	67,2	68,0	57,0	56,0	53,0	20,8	23,2	23,1	24,1	24,3	25,1	24,2778	
43	Hosterwitz/Pillnitz	1116	1118	990	992	1019	1035	1038	6,0	6,0	5,8	5,9	6,0	6,0	6	44,0	44,0	54,0	57,0	56,0	55,0	56,0	54,0	2,0	3,0	3,0	3,0	3,2	3,0	4,0	3,0	3,0	5,0	5,0	5,0	4,7	4,0	5,0	4,0	93,8	97,8	88,3	92,6	76,0	76,0	75,0	22,0	25,3	23,3	25,0	22,6	21,2	18,8333	
45	Weißig	983	1024	889	882	874	930	923	1,8	5,4	7,1	7,2	14,0	11,0	11	38,0	37,0	47,0	48,0	56,0	50,0	49,0	50,0	4,0	5,0	6,0	6,0	9,8	6,0	6,0	6,0	1,0	1,0	1,0	1,0	1,6	2,0	2,0	2,0	17,1	13,6	53,1	61,4	51,0	50,0	53,0	21,5	21,1	22,7	22,8	23,8	24,5	25,25	
46	Gönnsdorf/Pappritz	1309	1295	1163	1163	1177	1182	1197	0,0	2,7	2,6	2,6	0,0	3,0	0	26,0	27,0	37,0	42,0	43,0	41,0	43,0	42,0	1,0	1,0	2,0	2,0	2,6	2,0	2,0	1,0	1,0	1,0	1,0	1,0	0,8	1,0	2,0	2,0	98,4	102,2	56,2	53,3	45,0	43,0	45,0	 	 	 	 	 	 	
47	Schönfeld/Schullwitz	1410	1480	1314	1297	1378	1326	1334	9,2	15,4	15,4	15,5	9,0	9,0	9	44,0	41,0	47,0	47,0	47,0	49,0	49,0	47,0	3,0	4,0	4,0	4,0	3,1	2,0	3,0	3,0	2,0	2,0	3,0	3,0	2,2	3,0	3,0	3,0	65,2	87,2	83,8	84,7	76,0	80,0	79,0	16,3	18,1	19,6	21,1	22,2	22,9	22,6667	
51	Blasewitz	895	852	769	775	788	796	808	62,5	58,3	64,9	64,5	69,0	76,0	73	76,0	81,0	82,0	83,0	81,0	84,0	83,0	81,0	6,0	8,0	7,0	7,0	6,7	7,0	7,0	7,0	1,0	3,0	3,0	3,0	3,6	3,0	4,0	3,0	112,2	114,0	113,3	112,8	92,0	115,0	124,0	20,0	20,9	21,1	23,8	23,0	22,2	23	
52	Striesen-Ost	725	727	676	685	690	692	691	7,3	7,9	7,7	7,6	7,0	8,0	8	47,0	51,0	51,0	50,0	50,0	53,0	51,0	50,0	5,0	5,0	5,0	5,0	3,8	4,0	5,0	4,0	2,0	3,0	2,0	2,0	2,2	2,0	2,0	2,0	25,5	24,3	24,0	23,1	20,0	19,0	30,0	21,1	24,6	25,0	25,0	24,9	25,2	25,75	
53	Striesen-Süd	694	668	612	611	609	604	601	13,4	13,2	11,9	11,8	13,0	14,0	13	34,0	38,0	40,0	40,0	37,0	38,0	37,0	36,0	2,0	2,0	3,0	3,0	3,1	4,0	3,0	3,0	1,0	1,0	1,0	1,0	1,0	1,0	1,0	1,0	30,5	32,7	22,9	29,1	25,0	53,0	52,0	20,3	20,9	19,8	20,6	20,8	20,7	20,5882	
54	Striesen-West	707	713	647	640	649	658	663	8,7	10,3	10,2	10,0	10,0	12,0	14	30,0	32,0	35,0	35,0	35,0	35,0	35,0	35,0	3,0	4,0	4,0	4,0	3,5	3,0	3,0	3,0	1,0	1,0	1,0	1,0	1,1	1,0	1,0	1,0	96,0	90,6	103,1	100,7	87,0	102,0	99,0	20,0	19,7	20,5	20,8	20,7	20,6	20,7778	
55	Tolkewitz/Seidnitz-Nord	764	770	687	686	702	706	694	1,9	1,9	1,9	1,9	3,0	3,0	3	18,0	19,0	20,0	20,0	20,0	22,0	23,0	23,0	1,0	2,0	2,0	2,0	2,1	2,0	2,0	1,0	0,0	1,0	1,0	1,0	0,9	1,0	1,0	1,0	124,7	127,1	118,8	116,2	98,0	100,0	92,0	19,4	19,3	19,4	21,3	23,2	22,5	23,1111	
56	Seidnitz/Dobritz	715	719	651	649	652	658	656	16,8	16,7	18,9	18,5	17,0	18,0	18	30,0	32,0	33,0	34,0	34,0	36,0	35,0	35,0	4,0	4,0	3,0	3,0	3,3	4,0	4,0	4,0	1,0	1,0	2,0	2,0	1,5	2,0	2,0	2,0	116,8	109,1	105,6	93,7	75,0	82,0	85,0	19,2	20,2	21,6	23,1	22,5	21,9	22,2727	
57	Gruna	749	747	664	660	666	666	664	12,3	13,6	14,1	14,2	12,0	12,0	13	34,0	35,0	36,0	37,0	36,0	36,0	35,0	35,0	3,0	3,0	3,0	3,0	4,0	4,0	3,0	3,0	1,0	2,0	2,0	2,0	1,6	1,0	2,0	2,0	94,7	92,6	87,7	97,4	76,0	59,0	51,0	20,6	21,6	23,9	22,8	23,5	23,0	23	
61	Leuben	715	717	634	627	628	631	640	21,0	20,9	23,4	23,2	24,0	24,0	24	32,0	34,0	35,0	34,0	36,0	36,0	36,0	37,0	3,0	4,0	3,0	3,0	3,5	3,0	3,0	3,0	1,0	2,0	2,0	2,0	2,0	2,0	2,0	2,0	120,9	121,2	113,9	102,0	90,0	83,0	122,0	19,7	20,2	20,3	15,7	15,1	18,5	16,1538	
62	Laubegast	848	867	795	790	791	802	801	9,7	8,6	12,8	12,7	11,0	11,0	13	33,0	34,0	33,0	33,0	34,0	34,0	34,0	34,0	4,0	5,0	4,0	4,0	3,5	4,0	3,0	4,0	1,0	2,0	2,0	2,0	1,7	2,0	2,0	2,0	68,5	60,4	60,3	59,6	51,0	53,0	51,0	23,1	24,1	25,2	24,0	23,3	23,9	23,7857	
63	Kleinzschachwitz	1053	1070	986	981	981	994	1007	7,2	8,3	10,7	10,6	9,0	10,0	10	34,0	39,0	39,0	40,0	42,0	39,0	39,0	39,0	3,0	3,0	4,0	4,0	2,7	3,0	3,0	4,0	1,0	2,0	2,0	2,0	1,7	2,0	2,0	2,0	35,7	36,4	36,7	37,5	23,0	23,0	22,0	20,4	20,2	20,7	21,3	21,8	22,3	22,6667	
64	Großzschachwitz	830	823	737	731	726	741	724	6,6	8,3	6,6	6,6	5,0	5,0	5	34,0	37,0	37,0	39,0	39,0	39,0	38,0	37,0	4,0	5,0	5,0	5,0	4,5	4,0	4,0	3,0	1,0	2,0	2,0	2,0	1,7	1,0	1,0	1,0	91,6	86,9	89,2	97,3	96,0	64,0	95,0	19,6	18,6	19,4	21,3	20,3	23,3	24,375	
71	Prohlis-Nord	703	665	585	569	571	582	574	7,3	8,9	7,0	6,9	9,0	9,0	7	18,0	19,0	20,0	20,0	20,0	21,0	21,0	22,0	2,0	2,0	3,0	3,0	2,6	3,0	3,0	3,0	1,0	1,0	1,0	1,0	1,6	2,0	1,0	2,0	124,6	118,6	122,2	101,7	85,0	108,0	103,0	14,2	17,2	17,5	19,1	19,0	19,4	20,9167	
72	Prohlis-Süd	598	582	502	495	489	486	472	27,5	26,9	26,0	25,8	27,0	26,0	24	16,0	16,0	16,0	15,0	15,0	15,0	13,0	13,0	1,0	1,0	1,0	1,0	1,4	1,0	1,0	1,0	0,0	1,0	0,0	0,0	0,2	0,0	0,0	0,0	110,6	100,4	97,5	87,5	69,0	67,0	67,0	 	 	 	 	 	 	
73	Niedersedlitz	915	949	892	931	969	989	992	11,8	12,4	13,2	13,7	14,0	14,0	14	41,0	43,0	48,0	52,0	55,0	59,0	63,0	60,0	3,0	4,0	5,0	5,0	5,6	6,0	6,0	6,0	1,0	1,0	1,0	1,0	1,2	1,0	1,0	1,0	101,0	141,9	121,0	96,2	83,0	62,0	64,0	21,8	21,5	21,0	20,2	20,3	21,7	22	
74	Lockwitz	1292	1276	1173	1170	1170	1196	1208	6,6	6,5	6,5	6,5	6,0	8,0	8	61,0	62,0	62,0	65,0	65,0	64,0	63,0	62,0	8,0	9,0	10,0	10,0	7,5	8,0	8,0	7,0	1,0	2,0	2,0	2,0	2,4	2,0	2,0	2,0	75,8	71,8	71,5	69,2	59,0	56,0	54,0	24,9	25,3	23,9	22,8	21,8	22,5	21,875	
75	Leubnitz-Neuostra	928	901	808	810	821	823	826	8,1	8,1	8,7	8,6	9,0	9,0	9	32,0	34,0	34,0	37,0	36,0	37,0	36,0	36,0	2,0	2,0	2,0	2,0	2,2	2,0	2,0	2,0	1,0	1,0	1,0	1,0	1,5	2,0	1,0	1,0	102,8	112,5	106,9	99,0	71,0	73,0	69,0	23,8	24,9	25,1	25,2	23,9	23,0	23,0833	
76	Strehlen	625	626	541	541	568	577	561	25,6	25,3	26,2	26,3	29,0	26,0	26	44,0	47,0	49,0	49,0	50,0	51,0	51,0	49,0	5,0	5,0	6,0	6,0	5,5	6,0	6,0	5,0	1,0	2,0	2,0	2,0	1,9	2,0	2,0	2,0	76,4	78,3	77,2	79,5	84,0	84,0	78,0	19,8	20,9	20,6	20,3	20,6	19,8	19,9474	
77	Reick	712	717	645	647	653	658	658	2,2	2,1	2,0	1,9	2,0	2,0	2	37,0	41,0	43,0	39,0	39,0	40,0	40,0	42,0	3,0	3,0	3,0	3,0	3,2	3,0	4,0	4,0	2,0	3,0	4,0	4,0	2,8	3,0	3,0	3,0	29,0	25,8	24,1	22,8	20,0	18,0	17,0	 	 	 	 	 	 	
81	Südvorstadt-West	578	574	515	507	506	509	499	33,3	33,9	33,0	32,8	33,0	31,0	31	42,0	47,0	50,0	50,0	49,0	50,0	49,0	50,0	5,0	6,0	5,0	5,0	4,5	4,0	3,0	4,0	1,0	2,0	2,0	2,0	2,1	2,0	2,0	2,0	100,5	100,0	95,9	92,4	76,0	68,0	66,0	14,4	16,2	15,3	15,8	15,0	15,1	16,8182	
82	Südvorstadt-Ost	570	554	491	496	495	510	513	16,8	16,3	16,0	16,2	16,0	17,0	17	47,0	49,0	45,0	45,0	45,0	48,0	47,0	48,0	3,0	3,0	3,0	3,0	3,1	3,0	3,0	3,0	1,0	2,0	1,0	1,0	1,5	2,0	2,0	2,0	178,5	182,6	180,8	178,0	137,0	100,0	111,0	15,9	15,4	17,1	15,6	13,4	14,5	15,875	
83	Räcknitz/Zschertnitz	706	703	628	623	621	625	617	31,1	32,8	34,5	34,6	27,0	29,0	27	26,0	28,0	27,0	27,0	27,0	26,0	26,0	26,0	2,0	2,0	2,0	2,0	2,2	2,0	1,0	1,0	0,0	1,0	1,0	1,0	0,9	1,0	1,0	1,0	139,2	129,5	122,1	116,3	98,0	149,0	147,0	 	 	 	 	 	 	
84	Kleinpestitz/Mockritz	976	956	869	866	870	862	864	1,3	1,4	1,4	1,4	1,0	1,0	1	27,0	28,0	30,0	32,0	33,0	35,0	35,0	35,0	2,0	2,0	2,0	2,0	2,2	2,0	2,0	3,0	1,0	1,0	1,0	1,0	1,1	1,0	1,0	1,0	61,6	61,4	62,5	60,9	51,0	48,0	47,0	18,8	20,4	20,7	19,2	19,8	21,0	21,2857	
85	Coschütz/Gittersee	916	927	839	851	871	875	890	7,4	5,5	5,5	5,4	11,0	7,0	11	55,0	58,0	59,0	62,0	61,0	61,0	61,0	55,0	5,0	6,0	6,0	6,0	4,6	4,0	4,0	4,0	1,0	3,0	3,0	3,0	2,7	3,0	3,0	2,0	76,7	71,9	69,9	73,5	57,0	60,0	83,0	17,4	16,3	18,6	20,6	20,0	22,0	23,1111	
86	Plauen	718	705	647	648	650	654	645	10,8	10,5	11,3	11,1	13,0	11,0	10	41,0	48,0	48,0	46,0	48,0	47,0	48,0	46,0	5,0	5,0	4,0	4,0	4,6	5,0	4,0	4,0	2,0	3,0	2,0	2,0	2,1	2,0	2,0	2,0	60,5	60,1	59,6	60,0	50,0	39,0	40,0	22,1	20,9	22,8	22,5	22,9	24,5	24,2727	
90	Cossebaude/Mobschatz/Oberwartha	961	1138	1051	1050	1059	1071	1069	5,6	5,6	5,6	5,6	0,0	1,0	0	42,0	38,0	50,0	54,0	53,0	57,0	56,0	56,0	4,0	3,0	4,0	4,0	3,6	4,0	4,0	5,0	1,0	2,0	2,0	2,0	2,5	3,0	2,0	2,0	88,8	97,1	108,4	97,8	77,0	115,0	95,0	20,3	21,1	20,8	21,9	21,7	23,4	23,25	
91	Cotta	687	700	614	609	620	630	635	7,3	7,2	7,0	7,0	6,0	6,0	6	33,0	34,0	36,0	37,0	37,0	37,0	37,0	36,0	4,0	4,0	5,0	5,0	4,1	4,0	4,0	4,0	2,0	3,0	3,0	3,0	3,0	3,0	3,0	3,0	59,8	53,6	48,8	44,6	39,0	52,0	53,0	19,6	19,1	20,7	22,0	22,0	21,7	21,25	
92	Löbtau-Nord	507	507	464	455	463	470	461	43,7	40,8	38,7	37,6	38,0	36,0	39	46,0	48,0	47,0	45,0	43,0	44,0	44,0	44,0	8,0	9,0	9,0	8,0	8,0	8,0	7,0	7,0	2,0	4,0	3,0	3,0	3,3	3,0	3,0	3,0	59,7	88,3	85,1	84,0	66,0	66,0	64,0	21,4	21,3	22,4	20,9	23,7	22,0	21,6364	
93	Löbtau-Süd	520	512	464	464	474	479	484	20,1	21,0	20,6	20,2	22,0	24,0	25	40,0	45,0	46,0	44,0	42,0	44,0	44,0	44,0	4,0	4,0	5,0	4,0	3,7	4,0	4,0	4,0	2,0	3,0	2,0	2,0	2,6	3,0	3,0	2,0	30,1	29,1	30,7	28,7	25,0	33,0	51,0	21,4	21,6	21,8	20,2	19,7	22,2	22,75	
94	Naußlitz	927	945	851	837	849	850	849	6,9	9,2	9,1	9,1	8,0	9,0	10	32,0	33,0	35,0	37,0	37,0	39,0	37,0	41,0	2,0	2,0	2,0	2,0	2,6	2,0	2,0	3,0	1,0	1,0	1,0	1,0	1,5	2,0	2,0	2,0	85,2	84,8	92,2	89,1	73,0	84,0	93,0	18,3	20,3	20,4	21,0	24,3	23,4	23,25	
95	Gorbitz-Süd	580	580	487	488	480	485	479	17,2	16,9	18,1	18,3	17,0	17,0	17	16,0	17,0	17,0	17,0	18,0	18,0	19,0	18,0	2,0	2,0	1,0	1,0	1,6	2,0	1,0	1,0	1,0	1,0	1,0	1,0	1,1	1,0	1,0	1,0	91,6	81,6	68,6	69,8	57,0	51,0	49,0	16,2	16,7	17,4	19,8	18,6	17,1	16,9048	
96	Gorbitz-Ost	631	620	542	533	537	519	509	1,7	1,7	1,7	1,7	2,0	2,0	2	11,0	12,0	13,0	13,0	12,0	12,0	12,0	11,0	1,0	1,0	2,0	2,0	0,7	1,0	1,0	1,0	0,0	1,0	1,0	1,0	0,7	1,0	1,0	1,0	256,4	254,5	233,3	212,6	170,0	173,0	141,0	 	 	 	 	 	 	
97	Gorbitz-Nord/Neu-Omsewitz	642	636	543	534	538	542	535	23,7	24,1	25,4	26,0	32,0	29,0	31	14,0	15,0	16,0	18,0	19,0	19,0	18,0	17,0	4,0	4,0	4,0	4,0	4,4	4,0	4,0	3,0	1,0	1,0	1,0	1,0	1,0	1,0	1,0	1,0	167,2	211,2	204,3	222,0	166,0	153,0	152,0	18,1	20,4	21,3	20,2	21,0	22,5	21,8333	
98	Briesnitz	1013	1020	921	920	930	930	937	5,0	3,9	3,9	3,8	4,0	4,0	4	41,0	40,0	40,0	41,0	41,0	43,0	42,0	44,0	4,0	3,0	3,0	3,0	3,1	4,0	4,0	4,0	1,0	2,0	2,0	2,0	1,9	2,0	2,0	2,0	45,8	45,7	44,7	41,6	35,0	34,0	78,0	20,3	22,6	22,4	22,1	21,6	21,8	23,15	
99	Altfranken/Gompitz	1392	1414	1279	1293	1297	1295	1300	0,0	2,4	4,8	4,8	5,0	5,0	5	43,0	44,0	44,0	49,0	49,0	47,0	45,0	48,0	5,0	4,0	5,0	5,0	4,3	4,0	4,0	4,0	1,0	3,0	3,0	3,0	2,7	2,0	3,0	3,0	52,1	54,4	65,9	61,6	53,0	51,0	52,0	20,2	20,6	19,6	21,0	21,8	21,8	23,25	'''

# <markdowncell>

# Wir haben ja die Funktion noch, können sie also noch mal verwenden.
# 
# ![](WhenToWriteAnAlgorithm.png)

# <codecell>

years, pkw = text2dataframe(pkw)

# <markdowncell>

# Pandas DatenFrame erzeugen mit 
# 
# * Daten = PKW Bestand
# * Index = Jahre

# <codecell>

pkwbestand = pd.DataFrame(data=pkw, index=years)
pkwbestand = pkwbestand.convert_objects(convert_numeric=True)

# <codecell>

pkwbestand

# <codecell>

pkwbestand.describe()

# <markdowncell>

# Schauen wir uns nur mal den Bestand von 2011 an

# <codecell>

pkwbestand2011 = pkwbestand[pkwbestand.index.year==2011] # Nur 2011 auswählen
pkwbestand2011 = pkwbestand2011.T # Transponieren, weil wir jetzt Stadtteile als Index haben wollen, nicht Jahr

pkwbestand2011.columns = ['Bestand'] # Umbenennen
pkwbestand2011.sort('Bestand', ascending=False, inplace=True) # Sortieren
pkwbestand2011.plot(kind='barh', figsize=(7,12)) # Darstellen

plt.ylabel('Stadtteil')
plt.title('PKW in Dresden (2011)')
plt.tight_layout()
plt.savefig('PKW Bestand 2011.png', dpi=150)

# <headingcell level=3>

# Korrelation mit Fahrzeit zum Stadtzentrum

# <markdowncell>

# Woher bekommen wir die Fahrzeit? Na z.B. von Google. Google stellt uns mit der [DistanceMatrix API](https://developers.google.com/maps/documentation/distancematrix/?hl=de) eine Schnittstelle an, die es ermöglicht die Fahrzeit von Ort A nach Ort B zu ermitteln.
# 
# Dazu benötigen wir noch eine Bibliothek, welche es uns ermöglicht mit anderen Rechnern im Netz zu kommunizieren. Zum Beispiel [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/).

# <codecell>

import requests # Python Bibliothek für Anfragen an API's oder andere Webseiten

# <markdowncell>

# Jetzt schreiben wir uns eine Funktion, die die Fahrzeit zurück gibt.

# <codecell>

def getFahrzeit(ziel):
    start = 'Centrumgalerie, Dresden'
    fahrzeit = 0.0
    
    # Google Direction API
    baseurl = 'http://maps.googleapis.com/maps/api/distancematrix/json'

    try:
        payload = {'origins': '%s' % (start), \
                   'destinations': '%s' % (ziel), \
                   'sensor': 'false'}
        r = requests.get(baseurl, params=payload)

        #print r.url
        #print r.json()

        fahrzeit = float(r.json()['rows'][0]['elements'][0]['duration']['value'])/60.0 # in Minuten
    except:
        fahrzeit = NaN
        
    return int(fahrzeit)

# <codecell>

fahrzeit = getFahrzeit('Gorbitz, Dresden')
print('%imin Fahrzeit' % fahrzeit)

# <markdowncell>

# OK, das klappt. Dann für alle Stadtteile.

# <codecell>

pkwbestand2011['Fahrzeit'] = pkwbestand2011.index + ', Dresden' # Zielorte erzeugen
pkwbestand2011.head(5)

# <markdowncell>

# Jetzt wenden wir die Funktion auf jede Zeile an

# <codecell>

pkwbestand2011['Fahrzeit'] = pkwbestand2011['Fahrzeit'].apply(getFahrzeit)
pkwbestand2011.head(5)

# <markdowncell>

# Sortieren wir das doch mal

# <codecell>

pkwbestand2011.sort('Fahrzeit', ascending=False, inplace=True)
pkwbestand2011.head(10)

# <markdowncell>

# Schauen wir doch mal, ob es einen Zusammenhang zwischen der Fahrzeit zum Stadtzentrum und dem PKW Bestand in dem Stadtteil gibt

# <codecell>

grafik = sns.lmplot("Fahrzeit", "Bestand", data=pkwbestand2011, scatter_kws={"s": 50, "alpha": 0.8}, palette="Greens_d")
grafik.set_titles('Test')
grafik.set_xlabels('Fahrzeit mit PKW bis zum Stadtzentrum Dresden (in min)')
grafik.set_ylabels('PKW Bestand im Stadtteil')

plt.annotate('Gönnsdorf/Pappritz'.decode('utf-8'), xy=(23, 1220), xytext=(16, 1500),
            arrowprops=dict(facecolor='black', shrink=0.05, alpha=0.4), ha='center')

plt.annotate('Äußere Neustadt'.decode('utf-8'), xy=(7.3, 315), xytext=(15, 300),
            arrowprops=dict(facecolor='black', shrink=0.05, alpha=0.4), ha='left')

plt.savefig('Fahrzeit-PKWBestand-Korrelation-Dresden.png', dpi=150)

# <markdowncell>

# ![](http://triadstrategies.typepad.com/.a/6a0120a6abf659970b0162fde3889c970d-pi)

