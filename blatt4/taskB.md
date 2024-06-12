# B.1) KLM Calculation

Suche nach einer Zugverbindung über diese Website von “Stuttgart Hbf” nach “Berlin Hbf” für den nächsten Tag zur aktuellen Uhrzeit für einen Erwachsenen mit Bahncard 50 in der 1. Klasse. Zu Beginn der Interaktion liegen beide Hände auf der Tastatur. Bitte verwenden Sie hierfür den Firefox-Browser. Die css-Datei muss im gleichen Ordner wie die HTML-Datei liegen, damit die Webseite korrekt angezeigt wird.


Operator | Name | Time
--- | --- | ---
K | Keystroke (key presses != characters) | 0.3 s
H | Homing (move hand between mouse and keyboard) | 0.4 s
B/BB | Pressing/Clicking a mouse button | 0.1 s / 0.2 s
P | Pointing | 1.2 s
D | Drawing nD straight line segments of length lD | 0.9 * nD + 0.16 * lD
R | System response / work time (system-dependent) matrixcalculator.org | 2 s
R | System response / work time (system-dependent) ChatGPT (lots of writing) | 5 s
M | mental acts – ‘thinking’ or ‘look-at’ | 1.3 s

1. Click on origin input field
2. Type "Stuttgart Hbf"
3. Click on destination input field
4. Type "Berlin Hbf"
5. Click on date picker input field
6. Click on next day button (Day next to the blue marked day)
7. Check current time
8. Click on time input field
9. Type current time (HH:MM)
10. Click on "Bahncard" dropdown
11. Click on "Bahncard 50, 1. Klasse" option
12. Click on "1. Klasse" radio button
13. Click on "Suchen" button

```
P [to input field]
BB [click]
H [to keyboard]
M [consider "Stuttgart Hbf"]
13 * K [s-t-u-t-t-g-a-r-t-SPACE-h-b-f]
H [to mouse]

---

P [to input field]
BB [click]
H [to keyboard]
M [consider "Berlin Hbf"]
10 * K [b-e-r-l-i-n-SPACE-h-b-f]
H [to mouse]

---

P [to date picker]
BB [click]
M [consider current date and next day]
P [to next day button]
BB [click]

---

P [to time input field]
BB [click]
H [to keyboard]
M [consider current time]
4 * K [H-H-M-M]
H [to mouse]

---

P [to Bahncard dropdown]
BB [click]
M [consider Bahncard options]
P [to Bahncard 50, 1. Klasse]
BB [click]

---

P [to 1. Klasse radio button]
M [consider 1. Klasse radio button]
BB [click]

---

P [to "Suchen" button]
BB [click]
```

$$TCT = 27*K + 9*BB + 9*P + 6*H + 6*M$$
$$= 27*0.3s + 9*0.2s + 9*1.2s + 6*0.4s + 6*1.3s$$
$$= 8.1s + 1.8s + 10.8s + 2.4s + 7.8s$$
$$= \underline{\underline{30.9s}}$$


# B.2) KLM Optimization

Erstellen Sie zwei verschiedene, verbesserte Interfaces der vorgegebenen Website, sodass Eingaben deutlich schneller (mindestens 2 Sekunden Zeitersparnis mittels der Operatorzeiten aus Tabelle 1) getätigt werden können als bei der ursprünglichen Website, z. B. für aktuelle Pendlerverbindungen, zur Vermeidung von Fehleingaben, usw. Sie können dabei gerne Ideen von bestehenden Systemen übernehmen oder auch mit neuen innovativen Ansätzen arbeiten. Bitte dokumentieren und erklären Sie alle vorgenommenen Änderungen. Die Interfaces müssen nicht implementiert werden (es reicht ein Diagramm, welches die Interfaces ausführlich beschreibt).

## Interface 1
Häufig genutzte Verbindungen können als Favoriten gespeichert werden. Der Nutzer kann diese Favoriten direkt auswählen und muss nicht mehr die Stationen eingeben. Die Eingabe der Uhrzeit kann ebenfalls gespeichert werden, sodass der Nutzer nur noch die Uhrzeit bestätigen muss und das Datum bereits auf den nächsten Tag gesetzt ist.

## Interface 2
Die Stationen können durch eine Autovervollständigungsfunktion eingegeben werden. Der Nutzer muss nur noch die Anfangsbuchstaben eingeben und kann dann aus einer Liste von nach Relevanz sortierten Vorschlägen auswählen. Wenn eine Bahncard ausgewählt wird, wird automatisch die korrekte Klasse ausgewählt.


# B.3) KLM Calculation

Berechnen Sie auch für die von Ihnen verbesserten Versionen der Website mittels des KLMs und der Operatorzeiten aus Tabelle 1 die TCT der Suche nach der selben Zugverbindung wie zuvor. Vergleichen Sie die Ergebnisse der Ausführungszeiten (B.1 und B.3) miteinander.


## Interface 1

```
P [to Favorites dropdown]
BB [click]
M [consider Favorites options]
P [to "Stuttgart Hbf -> Berlin Hbf"]
BB [click]

---

M [consider Date and Time confirmation button]
P [to Date and Time confirmation button]
BB [click]

---

P [to Bahncard dropdown]
BB [click]
M [consider Bahncard options]
P [to Bahncard 50, 1. Klasse]
BB [click]

---

P [to 1. Klasse radio button]
M [consider 1. Klasse radio button]
BB [click]

---

P [to "Suchen" button]
BB [click]
```

$$TCT = 7*BB + 7*P + 4*M$$
$$= 7*0.2s + 7*1.2s + 4*1.3s$$
$$= 1.4s + 8.4s + 5.2s$$
$$= \underline{\underline{15s}}$$

## Interface 2

```
P [to origin input field]
BB [click]
H [to keyboard]
M [consider "Stuttgart Hbf"]
1 * K [s]
M [consider "Stuttgart Hbf" suggestion]
H [to mouse]
P [to "Stuttgart Hbf" suggestion]
BB [click]

---

P [to destination input field]
BB [click]
H [to keyboard]
M [consider "Berlin Hbf"]
1 * K [b]
M [consider "Berlin Hbf" suggestion]
H [to mouse]
P [to "Berlin Hbf" suggestion]
BB [click]

---

P [to date picker]
BB [click]
M [consider current date and next day]
P [to next day button]
BB [click]

---

P [to time input field]
BB [click]
H [to keyboard]
M [consider current time]
4 * K [H-H-M-M]
H [to mouse]

---

P [to Bahncard dropdown]
BB [click]
M [consider Bahncard options]
P [to Bahncard 50, 1. Klasse]
BB [click]

---

P [to "Suchen" button]
BB [click]
```

$$TCT = 2*K + 10*BB + 10*P + 4*H + 7*M$$
$$= 2*0.3s + 10*0.2s + 10*1.2s + 4*0.4s + 7*1.3s$$
$$= 0.6s + 2s + 12s + 1.6s + 9.1s$$
$$= \underline{\underline{25.3s}}$$

### Fazit
Die verbesserten Interfaces haben die Ausführungszeit im Vergleich zur ursprünglichen Website deutlich reduziert. Besonders Interface 1 mit der Favoritenfunktion hat die Ausführungszeit um 15.6s verkürzt, während Interface 2 mit der Autovervollständigungsfunktion die Ausführungszeit um 5.6s verkürzt hat. Die Optimierungen verkürzen die Ausführungszeit und verbessern die Benutzerfreundlichkeit der Website.
