# Projektarbeit-I-OpenAlex
Anmerkungen zur Vorstellung am 14.12.2022
* kleines Subset statt 300GB
* Zielgruppe definieren
* Planungsweise genauer beschreiben 
  * nächsten Schritte einplanen 
  * Deadlines genauer beschreiben (bsp: bis zu diesem Datum eine CSV)
  * explorierend --> Was brauchen wir?
<br></br>

## Einleitung
Was ist OpenAlex?
* ein offenes System zur Abbildung von Forschungsprozessen anhand der Entitäten
* basierend auf "Fünf-Einheiten-Modelle" Autoren, Werke, Orte (Zeitschriften, Repositorien), Institutionen und Konzepte, die miteinander verbunden sind
* Fokus auf Wissenschaftsdaten
* eigene API-Endpunkte 

Was ist Neo4j?
* eine eingebettete, plattenbasierte, transaktionale Datenbank-Engine, die Daten in Graphen statt in Tabellen speichert

<br></br>
## Projektbeschreibung

Das OpenAlex Katalog bietet eine gute Grundlage dafür, über die API wissenschaftliche Werke zu finden. Darüber hinaus sind  verwandte Werke zu einer bestimmten wissenschaftlichen Arbeit sichtbar. Auf dieser Basis enstand das Projektziel, über die mit der API verbundenen Werke zu wissenschaftlichen Arbeiten von OpenAlex zu extrahieren und diese in der Graphdatenbank NEO4j visuell dazustellen. Dazu soll ein Web-Interface erstellt werden, welcher den Knowledge Graph darstellt und für die Nutzer des Web Interfaces veranschaulicht. Vor allem Studierende, die eine wissenschaftliche Arbeit schreiben sollen die Möglichkeit haben über ein Thema Werke zu finden, die miteinander verbunden sind und zusätzlich dazu weitere Verbindungen zu finden. Das soll zielgreifend die Recherche der Studierenden erleichtern und sich einfacher in den Themen zu explorieren. Ein ideales Ergebnis ist ein Minimal Viable Product, bei dem ein Knowlegde Graph im Web Interface abgebildet ist.



![image](https://user-images.githubusercontent.com/92934375/208732448-cff613fd-4cdd-48c2-97b5-cbe929fc9b42.png)



<br></br>
### SMARTE Ziele

### Projektplanung


<br></br>
### Ressourcen
Die API ist der primäre Weg, um OpenAlex-Daten zu erhalten. Es ist kostenlos, einfach, schnell zu erhalten um alle Ergebnisse als Snapshot im gleichen Format wie von 
auf den Computer herunterzuladen.
* https://api.openalex.org/works?filter=cites:W2741809807
* https://api.openalex.org/works?filter=cited_by:W2766808518

* https://docs.openalex.org/download-snapshot   
* https://docs.openalex.org/download-snapshot/download-to-your-machine


## getting started

<br></br>
## Beispiele

<br></br>
## FAQ

<br></br>
## Sicherheitserläuterungen

<br></br>


## Arbeitsweise
<br></br>

 
**Vorbereitungsphase**

Die Projektinformationen werden gesammelt und erörtert, das Projektziel wird definiert und erste Vereinbarungen hinsichtlich der Projektorganisation werden getroffen. Die Vorbereitungsphase endet mit einer Projektidee und mit den verfassten SMART'en Ziele.

**Planungsphase**

Die Aufgaben werden festgelegt, ein Terminplan wird erstellt, Ressourcen und Kosten werden ermittelt. Am Ende der Planungsphase steht der Start der Umsetzungsphase.


**Umsetzungsphase**

Das Projekt wird unter Berücksichtigung von Terminen, Ressourcen und Kosten umgesetzt. Regelmäßige Sachstandsberichte werden zur Steuerung des Projekts erstellt.


**Abschlussphase**

Das Projekt wird abgeschlossen, die Arbeitsergebnisse werden abgenommen und die gesammelten Erfahrungen gesichert (Lessons Learned). Das Projekt wird vorgestellt und in einem Bericht zusammengefasst. 


Wir arbeiten klassisch, wollen jedoch zum agilen Projektmanagement wechseln soald wir unsere Projektziel erweitern.

