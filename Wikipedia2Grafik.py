# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ![CodeWeek Logo](http://blog.slub-dresden.de/uploads/RTEmagicC_codeweek-slider.png.png)

# <headingcell level=1>

# Zusammenhänge aus Zahlen finden.
# 
# Beispiel: Wikipedia Tabelle

# <codecell>

import pandas as pd

# <markdowncell>

# Tabelle von Wikipedia: http://de.wikipedia.org/wiki/Einwohnerentwicklung_von_Dresden#Stadtteile

# <codecell>

wikitable='''
{| class="wikitable sortable" style="text-align:right;"
! 
! Name
! Fläche in km²
! Einwohnerzahl
! Einwohner je km²
|-
| OA || align="left" | [[Altstadt (Ortsamtsbereich)|Altstadt]] || 17,00 || 49.432 || 2.908
|-
| OA || align="left" | [[Blasewitz (Ortsamtsbereich)|Blasewitz]] || 14,48 || 79.292 || 5.476
|-
| OA || align="left" | [[Cotta (Ortsamtsbereich)|Cotta]] || 19,34 || 65.535 || 3.389
|-
| OA || align="left" | [[Klotzsche (Ortsamtsbereich)|Klotzsche]] || 27,10 || 19.839 || 732
|- 
| OA || align="left" | [[Leuben (Ortsamtsbereich)|Leuben]] || 13,05 || 37.600 || 2.881
|-
| OA || align="left" | [[Loschwitz (Ortsamtsbereich)|Loschwitz]] || 68,84 || 19.073 || 277
|-
| OA || align="left" | [[Neustadt (Ortsamtsbereich)|Neustadt]] || 14,85 || 40.127 || 2.702
|-
| OA || align="left" | [[Pieschen (Ortsamtsbereich)|Pieschen]] || 16,20 || 46.595 || 2.876
|-
| OA || align="left" | [[Plauen (Ortsamtsbereich)|Plauen]] || 15,80 || 50.145 || 3.174
|-
| OA || align="left" | [[Prohlis (Ortsamtsbereich)|Prohlis]] || 21,10 || 54.349 || 2.576
|-
| OS || align="left" | [[Altfranken]] || 1,28 || 1.099 || 859
|-
| OS || align="left" | [[Cossebaude (Ortschaft)|Cossebaude]] || 8,04 || 5.324 || 662
|-
| OS || align="left" | [[Gompitz (Ortschaft)|Gompitz]] || 11,72 || 3.053 || 260
|-
| OS || align="left" | [[Langebrück]] || 6,95 || 3.719 || 535
|-
| OS || align="left" | [[Mobschatz (Ortschaft)|Mobschatz]] || 8,50 || 1.481 || 174
|-
| OS || align="left" | [[Oberwartha]] || 2,03 || 355 || 175
|-
| OS || align="left" | [[Schönborn (Dresden)|Schönborn]] || 5,20 || 490 || 94
|-
| OS || align="left" | [[Schönfeld-Weißig]] || 41,33 || 12.570 || 304
|-
| OS || align="left" | [[Weixdorf (Ortschaft)|Weixdorf]] || 15,49 || 5.943 || 384
|-class="sortbottom" 
!  || align="left" | Dresden || 328,30 || 496.021 || 1.511
|}'''

# <markdowncell>

# Schreiben wir uns eine Funktion, die die Wikipedia Tabelle in eine Form bringt, die man zu einem Pandas DatenFrame speichern kann

# <codecell>

header=[] # Array
content=[] # Array

for row in wikitable.split('\n'): # An Umbrüchen teilen und jede Zeile durch gehen
    #print row
    if row.startswith('!'): # Wenn Zeile mit ! beginnt
        header.append(row.strip('! ')) # sind es Überschriften, wo wir noch das ! weg nehmen

    if row.startswith('| '): # Wenn Zeile mit | beginnt, ist es der Inhalt (Zahlen)
        content.append(row.replace('.','').replace(',','.')) # wo wir noch etwas mit . und , korrigieren

header = header[1:-1] # Überschriften selektieren (2. bis Vorletzte)

daten = []
for col in content: # Alle Spalten in content durch gehen
    daten.append(col.split('||')[1:]) # und bei || trennen

# <markdowncell>

# `daten` sieht jetzt so aus:
# 
# ```
#  [' align="left" | [[Altstadt (Ortsamtsbereich)|Altstadt]] ',
#   ' 17.00 ',
#   ' 49432 ',
#   ' 2908'],
#  [' align="left" | [[Blasewitz (Ortsamtsbereich)|Blasewitz]] ',
#   ' 14.48 ',
#   ' 79292 ',
#   ' 5476'],
#  ...
# ```

# <markdowncell>

# Jetzt fügen wir alles zum Pandas Datenframe zusammen:
#     
# * Daten = `daten`
# * Überschriften = `header`

# <codecell>

df = pd.DataFrame(data=daten, columns=header)
df.head(5)

# <markdowncell>

# Noch etwas die Spalte `Name` korrigieren

# <codecell>

df['Name'] = df['Name'].map(lambda x: x.split('|')[1][3:].rstrip(']] '))
df['Name'] = df['Name'].map(lambda x: x.replace(' (Ortsamtsbereich)', '').replace(' (Ortschaft)','').replace(' (Dresden)',''))
df.head(5)

# <markdowncell>

# Jetzt noch den Index festlegen (nehmen wir die Namen der Stadtteile) und die Zahlen auch zu Zahlen konvertieren, sind nämlich noch Texte, weil wir ja einen Text eingelesen haben.

# <codecell>

df.index = df['Name'] # Name als Index
df.drop('Name', inplace=True, axis=1) # Dafür Name raus werfen
df.index.name='Ortsamt' # Index Name umbenennen
df = df.convert_objects(convert_numeric=True) # Zahlen konvertieren in Zahlen

# <codecell>

df.sort()

# <headingcell level=2>

# Ready!

# <markdowncell>

# ![Big Data Borat](BigDataBorat.png)

# <headingcell level=2>

# Darstellungen

# <codecell>

import matplotlib.pyplot as plt
from matplotlib import image, patches, colors
import mpld3
%matplotlib inline

# <markdowncell>

# OK, schauen wir uns doch mal die Einwohnerdichte an

# <codecell>

EWjeKM = df.sort(['Einwohner je km²'])

EWjeKM['Einwohner je km²'].plot(kind='barh', figsize=(5,6))

plt.xlabel(u'Einwohner je km²')
plt.tight_layout()
plt.savefig('Dresden-Einwohnerjekm2.png', dpi=150)

# <markdowncell>

# Hm. Vielleicht können wir ja noch andere Zusammenhänge bekommen

# <codecell>

df.plot(kind='scatter', x='Fläche in km²', y='Einwohnerzahl', s=250, figsize=(12,12))

for label, x, y in zip(df.index, df['Fläche in km²'], df['Einwohnerzahl']):
    plt.annotate(
        label.decode('utf-8'), 
        xy = (x, y), xytext = (20, -10),
        textcoords = 'offset points', ha = 'left', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'w', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    
plt.tight_layout()
plt.savefig('Einwohner-Scatter.png', dpi=150)

# <headingcell level=2>

# Wie wäre es mit einer interaktiven Grafik?

# <codecell>

fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
N = 100

scatter = ax.scatter(df['Fläche in km²'],
                     df['Einwohnerzahl'],
                     alpha=0.8,
                     s=100,
                     c=df['Einwohnerzahl']/df['Fläche in km²'],
                     cmap=plt.cm.winter_r)
ax.grid(color='white', linestyle='solid')

ax.set_title("Einwohnerdichte Dresdner Stadtteile", size=20)
ax.set_xlabel(u'Fläche in km²')
ax.set_ylabel(u'Einwohnerzahl')

tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=df.index.tolist())
mpld3.plugins.connect(fig, tooltip)

mpld3.save_html(fig, 'Einwohner-Scatter.html')

mpld3.display()

# <markdowncell>

# ![](http://triadstrategies.typepad.com/.a/6a0120a6abf659970b0162fde3889c970d-pi)

