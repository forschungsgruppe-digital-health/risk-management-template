# Risikomanagement für Medizinprodukte-Software — eine Einführung für Einsteiger

Eine in sich geschlossene Lektion darüber, *was* Risikomanagement ist, *warum* es
existiert und *wie* es funktioniert — geschrieben für jemanden, der es noch nie gemacht
hat. Anschließend wird gezeigt, wie das **risk-management-template** und sein
**[Beispiel-Repository](https://github.com/forschungsgruppe-digital-health/risk-management-template-example)**
jede Idee in etwas Anklickbares verwandeln.

> **Zur Quellenlage — bitte lesen.**
> Jede Sachaussage ist im tatsächlichen Text der Normen verankert und nennt die
> **Klausel** (z. B. *14971 §7.1*), damit Sie sie nachschlagen können. Normen sind
> **urheberrechtlich geschützt**: diese Einführung gibt sie in einfacher Sprache sinngemäß
> wieder — sie ist **kein Ersatz** für die Normen selbst, die Sie für echte Arbeit
> beschaffen müssen. Der Wortlaut der Normen wurde in der **englischen** Fassung geprüft;
> die **amtliche deutsche Terminologie** richtet sich nach **DIN EN ISO 14971** bzw. der
> deutschen Sprachfassung der MDR — diese Übersetzung verwendet die üblichen deutschen
> Fachbegriffe. Der MDR-Wortlaut wurde gegen öffentliche Volltext-Wiedergaben der
> Verordnung (EU) 2017/745 abgeglichen; **prüfen Sie ihn gegen das
> [Amtsblatt / EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)**. Dieses Dokument
> ist **Lehrmaterial, keine Rechts- oder Regulierungsberatung**.
>
> **Zugrunde gelegte Ausgaben:** ISO 14971:2019 · ISO/TR 24971:2020 ·
> IEC 62304:2006+A1:2015 · IEC 62366-1:2015+A1:2020 · IEC 82304-1:2016 ·
> IEC 81001-5-1:2021 · ISO 81001-1:2021 · Verordnung (EU) 2017/745 (MDR), Anhang I.
>
> *(English version: [`risk-management-primer.md`](risk-management-primer.md).)*

---

## 1. Der eine große Gedanke

Sie können Risiko nicht auf null bringen. Ein nützliches Medizinprodukt **ohne** Risiko
existiert praktisch nicht. Das Ziel des Risikomanagements ist deshalb **nicht**, Risiko zu
beseitigen — sondern es **auf ein vertretbares Maß zu senken und zu belegen, dass man das
getan hat**.

Die Norm, die das für Medizinprodukte festlegt — **ISO 14971:2019** — fasst den Gedanken in
ihrer Definition von *Sicherheit* zusammen: „Freiheit von unvertretbarem Risiko" (14971
§3.26). Lesen Sie das genau: Sicherheit ist nicht die *Abwesenheit* von Risiko, sondern die
Abwesenheit von als *unvertretbar* beurteiltem Risiko. Nach allen Maßnahmen bleibt immer
ein Rest; die Norm nennt ihn **Restrisiko** (14971 §3.17), und auch er muss bewusst
betrachtet und akzeptiert werden.

Daraus folgen zwei Dinge, die alles Weitere prägen:

- **Risiko hat zwei Bestandteile, stets gemeinsam betrachtet:** wie *wahrscheinlich* ein
  Schaden ist (Wahrscheinlichkeit) und wie *schwer* er wäre (Schweregrad). ISO 14971
  definiert *Risiko* genau als Kombination aus der Wahrscheinlichkeit des Auftretens eines
  Schadens und dem Schweregrad dieses Schadens (14971 §3.18). Man kann ein Risiko nie mit
  nur einem der beiden Teile beschreiben.
- **Es braucht Urteilsvermögen, nicht nur Rechnen.** Die Einleitung der Norm hält fest,
  dass verschiedene Menschen dasselbe Risiko je nach erwartetem *Nutzen* unterschiedlich
  akzeptieren (14971, Einleitung). Deshalb ist „Ist das vertretbar?" eine Entscheidung, die
  eine kompetente, verantwortliche Person gegen vorab vereinbarte Kriterien trifft — keine
  Zahl, die ein Werkzeug ausgibt.

Dieses Template setzt diese Haltung unmittelbar um: seine Harm-Risk-Methode
([`../HARM_RISK.md`](../HARM_RISK.md)) liefert eine Akzeptanzmatrix, die ausdrücklich als
„example — adopt consciously" gekennzeichnet ist, weil — wie die folgenden Abschnitte
zeigen — **die Norm Sie Ihre eigenen Kriterien festlegen lässt**; sie gibt sie Ihnen nicht
vor.

---

## 2. Die Begriffe, die Sie beherrschen müssen

Fast jeder Einsteigerfehler ist in Wahrheit ein Begriffsfehler. Vier Wörter bilden eine
**Kette**, und sie sauber auseinanderzuhalten ist das ganze Spiel (alle aus ISO 14971
Abschnitt 3):

| Begriff | Einfache Bedeutung | Klausel |
|---|---|---|
| **Gefährdung** (hazard) | Eine *potenzielle* Schadensquelle. Für sich hat sie noch niemandem geschadet — sie ist nur das, was schaden *könnte* (Strom, eine scharfe Kante, unsicheres Softwareverhalten). | §3.4 |
| **Gefährdungssituation** (hazardous situation) | Ein Umstand, in dem Menschen der Gefährdung tatsächlich **ausgesetzt** sind. Das ist die Brücke von „eine Gefährdung existiert" zu „jetzt kann Schaden entstehen". | §3.5 |
| **Schaden** (harm) | Die tatsächliche Verletzung oder Gesundheitsschädigung (einschließlich Schaden durch falsche oder verzögerte klinische Entscheidungen infolge von Software). | §3.3 |
| **Risiko** (risk) | Wahrscheinlichkeit dieses Schadens **×** sein Schweregrad — die zwei Bestandteile aus §1. | §3.18 |

Die Kette lautet: **Gefährdung → (Ereignisfolge) → Gefährdungssituation → Schaden.** Eine
Gefährdung wird erst durch eine *vorhersehbare Ereignisfolge* gefährlich, die jemanden
aussetzt, und **eine Gefährdung kann zu mehreren verschiedenen Gefährdungssituationen und
Schäden führen** (14971 §5.4).

**Durchgerechnetes Beispiel (aus dem Beispiel-Repository).** Issue
[#2 im Beispiel-Repository](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/2)
ist ein vollständiges, synthetisches Harm-Risk genau in dieser Kette: *Gefährdung* — ein
Fragebogen-Score wird für den **falschen Patienten** angezeigt; *Ereignisfolge* — zwei
Datensätze in benachbarten Tabs offen, veralteter Zustand rendert den Score von Patient A
in der Ansicht von Patient B; *Gefährdungssituation* — eine Ärztin liest bei der Triage den
falschen Score; *Schaden* — verzögerte Eskalation der Versorgung. Beachten Sie: die
*Abhilfe* ist **nicht** die Gefährdung — das Register dokumentiert die Gefahr, nicht das
Ticket, das sie schließt.

Weitere Begriffe, die Ihnen begegnen (ISO 14971 Abschnitt 3):

- **Zweckbestimmung** (intended use, §3.6) — wofür der Hersteller das Produkt *bestimmt*;
  ohne Ehrlichkeit hierüber findet man die Gefährdungen nicht.
- **Vernünftigerweise vorhersehbare Fehlanwendung** (§3.15) — vorhersehbarer *falscher*
  Gebrauch, den man berücksichtigen muss, weil viele reale Schäden aus menschlichem
  Verhalten stammen, nicht aus Produktfehlern.
- **Nutzen** (benefit, §3.2) — eine positive Wirkung auf Gesundheit, Patientenmanagement
  oder öffentliche Gesundheit; das, wogegen ein Restrisiko abgewogen wird.
- **Stand der Technik** (§3.28) — der aktuell *allgemein anerkannte gute Stand* — wichtig:
  **nicht** notwendigerweise das Neueste oder Fortschrittlichste.

---

## 3. Der Prozess, Schritt für Schritt

ISO 14971 ordnet alles in **einen fortlaufenden Prozess**, den der Hersteller „festlegen,
umsetzen, dokumentieren und aufrechterhalten" muss und der „über den gesamten Lebenszyklus
des Medizinprodukts" gelten muss (14971 §4.1). „Fortlaufend" und „Lebenszyklus" sind der
Kern: Risikoarbeit ist mit der Markteinführung nie fertig.

Der Prozess hat vier vorgeschriebene Teile — **Risikoanalyse, Risikobewertung,
Risikobeherrschung sowie Tätigkeiten während Produktion und Nachproduktion** — alle gelenkt
durch einen schriftlichen **Risikomanagementplan** (14971, Bild 1). Nachfolgend die ganze
Schleife, jeder Schritt mit *was er ist*, *warum es ihn gibt*, seiner Klausel und **wie
dieses Template ihn umsetzt**.

### 3.0 Vor der Arbeit: Plan, Akte, Politik, Personen

- **Ein Risikomanagement-PLAN, vorab geschrieben** (14971 §4.4). Für das konkrete Produkt
  planen Sie die Arbeit, *bevor* Sie sie tun. Der Plan muss mindestens enthalten: Umfang
  und Lebenszyklusphasen; Verantwortlichkeiten; wann Überprüfungen stattfinden; **die
  Kriterien für die Risikoakzeptanz**; eine **Methode und Kriterien für das
  Gesamt-Restrisiko**; Verifizierungstätigkeiten; und wie Informationen aus Produktion und
  Nachproduktion gesammelt werden. Die Akzeptanzkriterien werden *vorab* festgelegt, damit
  spätere Entscheidungen nicht an ein Ergebnis angepasst werden können.
  → *Template:* [`../HARM_RISK.md`](../HARM_RISK.md) **§1** ist diese Plantabelle, mit
  Zeilen für die Politik-Grundlage (§4.2), die Gesamt-Restrisiko-Methode (§4.4 e) und die
  Überprüfungsanforderungen (§4.4 f) — je Projekt auszufüllen.
- **Die Risikomanagement-AKTE** (14971 §4.5) — die Nachweiskette, die es *für jede
  Gefährdung* erlaubt, Analyse → Bewertung → Beherrschung + deren Verifizierung → Restrisiko
  nachzuverfolgen. → *Template:* das Register selbst (GitHub-Issues) plus der §9-Bericht und
  die Register-Exporte je Release.
- **Die oberste Leitung legt eine POLITIK für vertretbares Risiko fest** (14971 §4.2): Die
  oberste Leitung muss eine Politik zur Festlegung der Kriterien für die Risikoakzeptanz
  definieren und dokumentieren, gerahmt durch Vorschriften, Normen, den Stand der Technik
  und bekannte Interessengruppen-Anliegen. Akzeptanz ist eine Entscheidung auf
  Unternehmensebene, nicht die Improvisation jedes einzelnen Ingenieurs.
- **Kompetente Personen** (14971 §4.3) — die Ausführenden müssen durch Ausbildung, Schulung,
  Fertigkeiten und Erfahrung kompetent sein, mit Nachweisen. Eine Risikoanalyse ist nur so
  vertrauenswürdig wie die Personen, die die Urteile fällen.

### 3.1 Risikoanalyse — Gefährdungen finden, Risiken bemessen (14971 §5)

1. **Zweckbestimmung & vernünftigerweise vorhersehbare Fehlanwendung** (§5.2) — beides
   dokumentieren. → *Template:* die Zweckbestimmung steht in
   [ADR-0001](../adr/0001-mdsw-qualification.md); das Feld *Ereignisfolge* des
   Harm-Risk-Formulars erfasst die vorhersehbare Fehlanwendung.
2. **Sicherheitsbezogene Merkmale** (§5.3) — jede Produkteigenschaft auflisten, die die
   Sicherheit beeinflussen könnte, damit keine Schadensquelle übersehen wird.
3. **Gefährdungen und Gefährdungssituationen identifizieren** (§5.4) — bekannte und
   vorhersehbare Gefährdungen im *Normal- und im Fehlerzustand* auflisten, dann die
   Ereignisketten ermitteln, die jede in eine Gefährdungssituation überführen. → *Template:*
   die vier Pflichtfelder des [Harm-Risk-Formulars](../../.github/ISSUE_TEMPLATE/harm-risk.yml)
   sind genau diese Kette; `hazard-cat:*`-Labels kategorisieren sie.
   **Hilfsmittel (ISO/TR 24971):** *Anhang A* ist eine Frageliste, um sicherheitsbezogene
   Merkmale aufzudecken, und *Anhang B* nennt Analysetechniken (PHA, FTA, FMEA, HAZOP,
   HACCP) — oft braucht man mehr als eine (TR 24971 Anhang A, Anhang B).
4. **Risikoeinschätzung** (§5.5) — für jede Gefährdungssituation **Wahrscheinlichkeit** und
   **Schweregrad** einschätzen (qualitativ oder quantitativ). Wenn eine Wahrscheinlichkeit
   wirklich nicht einschätzbar ist, stattdessen die möglichen Folgen auflisten. Das
   verwendete Einstufungs-*System* muss festgehalten werden. → *Template:* die S- und
   P-Auswahlfelder des Formulars; [`../HARM_RISK.md`](../HARM_RISK.md) §3.

   **Wichtige Hilfe (ISO/TR 24971 §5.5.2):** die Wahrscheinlichkeit des Schadens *P* lässt
   sich in **P1 × P2** zerlegen — *P1* = Wahrscheinlichkeit, dass die
   **Gefährdungssituation** eintritt (jemand wird ausgesetzt), *P2* = Wahrscheinlichkeit,
   dass sie dann **zum Schaden führt**. Diese Zerlegung „ist nicht verpflichtend" — sie ist
   eine hilfreiche Option. Und wenn eine Wahrscheinlichkeit wirklich nicht einschätzbar ist,
   besteht der **konservative Ansatz** darin, „die unbekannte Wahrscheinlichkeit gleich 1 zu
   setzen". Für **Software** ist die Ausfallwahrscheinlichkeit der klassische
   nicht-einschätzbare Fall (TR 24971 §5.5.3), weshalb üblicherweise P1 = 1 (Worst Case)
   gesetzt und die Bewertung von Schweregrad und P2 getragen wird — die Konvention, die die
   Methode des Templates dokumentiert.

### 3.2 Risikobewertung — das Go/No-Go-Tor (14971 §6)

Für jede Gefährdungssituation **vergleichen Sie das eingeschätzte Risiko mit den
Akzeptanzkriterien aus Ihrem Plan** und entscheiden: vertretbar oder nicht (14971 §6). Ist
es vertretbar, dürfen Sie die Minderungsschritte überspringen und die Einschätzung als
Restrisiko behandeln; wenn nicht, müssen Sie Risikobeherrschung durchführen. Weil die
Kriterien vorher festgelegt wurden, ist dies ein ehrlicher Ja/Nein-Test, keine Verhandlung.

**Gibt die Norm Ihnen die Skala oder die Matrix?** Nein — und das überrascht Einsteiger.
ISO 14971 verlangt vom Hersteller objektive Kriterien für die Risikoakzeptanz, legt aber die
vertretbaren Risikoniveaus *nicht* fest (14971 §1); die Kriterien stammen aus *Ihrer*
dokumentierten Politik (§4.2) und Ihrem Plan (§4.4). ISO/TR 24971 *zeigt* Beispielmatrizen
(3×3, 5×5), betont aber, dass dies nicht bedeutet, dass diese Methode allgemein für alle
Medizinprodukte gilt (TR 24971 §5.5.1) — Sie wählen die Stufen, definieren jede und
begründen die Matrix für Ihr Produkt. → *Deshalb* trägt die Matrix des Templates den Zusatz
„example — adopt consciously", und der Plan fragt, wer sie ratifiziert hat.

### 3.3 Risikobeherrschung — mindern, in verpflichtender Reihenfolge (14971 §7)

Dies ist einer der wichtigsten Lehrpunkte. Um ein unvertretbares Risiko zu senken, müssen
Sie die Beherrschungsoptionen in einer **festen Prioritätsreihenfolge** versuchen — nicht
die billigste (14971 §7.1):

1. **(a) Inhärent sichere Gestaltung und Herstellung** — die Gefährdung *herauskonstruieren*
   (z. B. eine Falschpatienten-Anzeige baulich unmöglich machen).
2. **(b) Schutzmaßnahmen** im Produkt oder im Herstellprozess — Prüfungen, Bestätigungen,
   Alarme — für Risiken, die Sie nicht herauskonstruieren konnten.
3. **(c) Informationen für die Sicherheit** — Warnungen, Anweisungen und ggf. Schulung der
   Anwender. Die **schwächste** Maßnahme, weil sie davon abhängt, dass Menschen lesen und
   befolgen; nie das Mittel erster Wahl.

Die Reihenfolge besteht, weil sichere Gestaltung alle automatisch schützt, ein Warnhinweis
hingegen nicht. → *Template:* das Harm-Risk-Formular verlangt, „die Hierarchiestufe je
Maßnahme anzugeben"; [`../HARM_RISK.md`](../HARM_RISK.md) §5 wiederholt die Reihenfolge als
verpflichtend.

Anschließend müssen Sie für jede Maßnahme (14971 §7.2) **zwei getrennte Dinge verifizieren**:
dass jede Maßnahme *umgesetzt* wurde **und** dass sie *wirksam* ist — eine Maßnahme kann
existieren, ohne zu wirken, daher sind beide nötig. → *Template:* das Board-Feld
`Control verification` (`None → Implemented → Verified effective`) und das
Verifizierungsplan-Feld des Formulars.

Der Rest von §7 schließt die Schleife:

- **Restrisiko nach Beherrschung** (§7.3) — das Verbleibende erneut gegen dieselben
  Kriterien prüfen; wenn weiter unvertretbar, zurück zu weiteren Maßnahmen.
- **Nutzen-Risiko-Analyse** (§7.4) — bleibt ein Restrisiko unvertretbar und ist keine
  weitere Beherrschung praktikabel, *dürfen* Sie Daten sammeln, um zu beurteilen, ob der
  Nutzen der Zweckbestimmung dieses Restrisiko überwiegt. Dies ist der **einzige** Weg, auf
  dem ein sonst unvertretbares Risiko gerechtfertigt werden kann — durch belegten Nutzen,
  nicht durch Behauptung. → *Template:* das Nutzen-Risiko-Feld des Formulars.
- **Risiken durch die Beherrschungsmaßnahmen** (§7.5) — jede Abhilfe kann *neue*
  Gefährdungen schaffen (ein Alarm erzeugt Alarmmüdigkeit; ein erneutes Laden schafft ein
  Race-Fenster). Sie müssen prüfen, „ob neue Gefährdungen oder Gefährdungssituationen
  eingeführt werden", und sie erneut durch den Prozess führen. → *Template:* ein
  **Pflicht**-§7.5-Feld im Harm-Risk-Formular („‚keine festgestellt' mit Begründung ist eine
  gültige Antwort").
- **Vollständigkeit der Risikobeherrschung** (§7.6) — bestätigen, dass Risiken aus *allen*
  identifizierten Gefährdungssituationen betrachtet und *alle* Maßnahmen abgeschlossen sind.
  → *Template:* das §7.6-Vollständigkeits-Häkchen.

### 3.4 Gesamt-Restrisiko und Information der Anwender (14971 §8)

Einzelrisiken können jeweils vertretbar sein und sich dennoch zu zu viel **summieren**.
Nachdem alle Maßnahmen umgesetzt und verifiziert sind, bewerten Sie deshalb das
**Gesamt-Restrisiko** des ganzen Produkts gegen seinen Nutzen, mit Methode und Kriterien aus
dem Plan (14971 §8). Ist es vertretbar, müssen Sie die wesentlichen Restrisiken den
Anwendern **offenlegen** — die notwendigen Informationen in die Begleitdokumentation (die
Gebrauchsanweisung) aufnehmen —, damit sie informiert entscheiden können. → *Template:* die
Gesamtbetrachtung steht in [`../HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md); das Label
`disclose-in-ifu` markiert Maßnahmen, deren Warnung die Anwenderdokumentation erreichen muss.

### 3.5 Überprüfung und Bericht — das Tor vor dem Markt (14971 §9)

Vor der Markteinführung **überprüft eine verantwortliche Person, dass der Plan ausgeführt
wurde**: der Plan wurde umgesetzt, das Gesamt-Restrisiko ist vertretbar, und es bestehen
Methoden zur Sammlung von Informationen aus Produktion und Nachproduktion. Das Ergebnis wird
als **Risikomanagementbericht** in der Akte aufbewahrt (14971 §9). → *Template:*
[`../HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md) kodiert genau diese drei Schlussfolgerungen
samt Freigabe; die Release-Workflows hängen den Bericht-Nachweis und Register-Snapshots an.

### 3.6 Nach der Einführung — weiter beobachten (14971 §10)

Risikomanagement endet nicht mit dem Release. Der Hersteller muss „aktiv Informationen
sammeln und überprüfen" aus Produktion, von Anwendern, Installateuren, der Lieferkette,
öffentlichen Quellen und dem sich wandelnden Stand der Technik (§10.1–§10.2), sie auf
Sicherheitsrelevanz prüfen — neue Gefährdungen? ein Risiko nicht mehr vertretbar? Stand der
Technik weitergezogen? (§10.3) — und definierte **Maßnahmen** ergreifen, wenn ja (§10.4),
zurückgespeist in die Prozessüberprüfung der Leitung. „Aktiv" ist das Schlüsselwort: man
sucht aktiv, wartet nicht bloß auf Beschwerden. → *Template:* das
[Field-Feedback-Formular](../../.github/ISSUE_TEMPLATE/field-feedback.yml) (§10-Eingang), das
SOUP-Anomalie-Formular und die CVE→Register-Automatik sind diese Schleife; die Issues
[#4](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/4)
und
[#5](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/5)
des Beispiel-Repos demonstrieren die beiden Eingangsformulare.

---

## 4. Das größere Bild: Software, Gebrauchstauglichkeit, Sicherheit

ISO 14971 ist die *Methode*, doch ein Gesundheits-Software-Produkt berührt vier
Nachbarnormen, die ein Einsteiger kennen sollte.

**IEC 62304 — der Software-Lebenszyklus.** Software verletzt selten jemanden *direkt*,
deshalb müssen Sie nachvollziehen, *wie* ein Softwarefehler zu Schaden führen könnte, und
belegen, dass Sie ihn beherrscht haben. Ihr Risikoprozess ist ausdrücklich „in den
Risikomanagementprozess des Produkts nach ISO 14971 eingebettet" (62304 §4.2/§7) — er fügt
sich ein, ersetzt nicht. Zwei Dinge muss ein Einsteiger wissen:

- **Software-Sicherheitsklassen A / B / C** (62304 §4.3, geändert durch AMD1:2015) sind
  **risikobasiert**. Sie nehmen an, dass ein Softwareausfall *eintritt*
  (Wahrscheinlichkeit = 1), und betrachten nur Beherrschungsmaßnahmen *außerhalb* der
  Software. **Klasse A heißt nicht einfach „keine Verletzung möglich"** — ein System, das zu
  Schaden beitragen *könnte*, ist dennoch Klasse A, wenn externe Maßnahmen das Risiko
  vertretbar halten; **B** = mögliche nicht-schwere Verletzung; **C** = möglicher Tod oder
  schwere Verletzung. Die Klasse entscheidet dann, wie viel der Norm Sie erfüllen müssen. →
  *Template:* [ADR-0002](../adr/0002-software-safety-classification.md) hält diese Klasse
  fest; [`../standards/IEC-62304-COVERAGE.md`](../standards/IEC-62304-COVERAGE.md) bildet ab,
  welche Klauseln gelten.
- **SOUP** („software of unknown provenance", 62304 §3.29) — wiederverwendeter Fremdcode,
  den Sie nicht nach der Norm entwickelt haben. Sie müssen ihn mit einer eindeutigen
  Versionsbezeichnung **identifizieren** (§8.1.2), die **funktionalen/Leistungs-Anforderungen
  angeben, auf die Sie sich verlassen** (§5.3.3), und die vom Lieferanten **veröffentlichten
  Anomalie-(Fehler-)Listen** für Ihre genaue Version **bewerten** (§7.1.3). → *Template:*
  [`../soup.yaml`](../../soup.yaml) + [`../SOUP.md`](../SOUP.md) + das SOUP-Anomalie-Formular.

**IEC 62366-1 — Gebrauchstauglichkeit (Usability Engineering).** Viele Produkte versagen
nicht, weil Hardware bricht, sondern weil ein Anwender sie falsch bedient — ein
**Gebrauchsfehler**: „unvertretbares Risiko kann aus einem Gebrauchsfehler entstehen"
(62366-1). Die Norm führt einen Prozess, um Gebrauchsfehler zu finden und zu mindern, und
unterscheidet die **formative** Evaluierung („während der Gestaltung … um Stärken, Schwächen
und unerwartete Gebrauchsfehler zu erkunden", 62366-1 §3.7 — Probe, iterativ) von der
**summativen** Evaluierung (am Ende, „um objektive Nachweise zu erhalten", dass die
Schnittstelle **sicher** benutzbar ist, §3.13 — die Validierung). → *Template:* die
Kategorie `hazard-cat:usability` und die Wirksamkeitsverifizierung, die auf einer
Usability-Bewertung beruhen kann.

**IEC 82304-1 — Produktsicherheit eigenständiger Gesundheitssoftware.** Sie stellt
Anforderungen an Sicherheit+Security des Gesamtprodukts für Software, die auf allgemeinen
Rechenplattformen *ohne dedizierte Hardware* läuft, und erfindet nichts neu: für den
Lebenszyklus verweist sie auf **IEC 62304** und darüber auf **ISO 14971** für das
Risikomanagement (82304-1 Abschnitt 2 & §5).

**IEC 81001-5-1 — Security über den Lebenszyklus.** Das Security-Gegenstück zum
Entwicklungsprozess: sie „definiert die Lebenszyklus-Anforderungen für Entwicklung und
Wartung von Gesundheitssoftware" bezüglich **Security**, ist „in der Reihenfolge von IEC
62304 angeordnet", sodass sie sich in Ihre bestehenden Schritte einfügt, und schreibt den
Umgang mit Fremd-/SOUP-Komponenten sowie **Schwachstellenmanagement** vor, das nach dem
Release weiterläuft (81001-5-1 §1, §0.1, §9). → *Template:*
[`../SECURITY_RISK.md`](../SECURITY_RISK.md) (Security-Risiko-Methode) und
[`../../SECURITY.md`](../../SECURITY.md) (Schwachstellen-Offenlegung).

**ISO 81001-1 — das Fundament.** Sie benennt die **drei „Schlüsseleigenschaften"**, die für
Gesundheitssoftware *gemeinsam* gemanagt werden müssen: **Sicherheit, Wirksamkeit und
Security** (81001-1 §3.2.8), und betont, dass sie **voneinander abhängen** — eine zu
verschärfen kann eine andere fördern oder schädigen, also werden sie ausbalanciert, nicht
einzeln optimiert. Das ist die gemeinsame Sprache unter den anderen Normen.

---

## 5. MDR im Besonderen — das Recht hinter der Methode

Alles Bisherige ist das *Wie* des Risikomanagements. In der EU kommt das *Warum Sie müssen*
aus der **Medizinprodukte-Verordnung, Verordnung (EU) 2017/745 (MDR)** — dem **Recht**. Ihr
**Anhang I, „Grundlegende Sicherheits- und Leistungsanforderungen" (GSLA/GSPR)** ist der
Ort, an dem Risikomanagement vorgeschrieben ist. ISO 14971 ist die anerkannte Methode, die
das erfüllt. Die wichtigsten GSPR (Anhang I, Kapitel I):

- **GSPR 1** — das oberste Versprechen: Produkte müssen *sicher und wirksam* sein und den
  klinischen Zustand oder die Sicherheit der Patienten nicht beeinträchtigen, *sofern die
  Risiken vertretbar sind, wenn sie gegen den Nutzen abgewogen werden*, und mit einem hohen
  Schutzniveau vereinbar, unter Berücksichtigung des Stands der Technik. Jede andere
  Anforderung dient diesem Nutzen-Risiko-Versprechen.
- **GSPR 2 — Risiken „so weit wie möglich" senken (AFAP).** Die MDR verlangt, Risiken *so
  weit wie möglich* zu senken — und stellt klar, dass dies *ohne nachteilige Beeinflussung
  des Nutzen-Risiko-Verhältnisses* zu geschehen hat. Auf Deutsch: **nicht null Risiko und
  auch nicht ‚so niedrig wie wirtschaftlich bequem'**, sondern das niedrigste erreichbare
  Risiko unter Erhalt des klinischen Nutzens. Genau deshalb existiert der
  Nutzen-Risiko-Schritt von ISO 14971.
- **GSPR 3** — ein **Risikomanagementsystem und -plan** sind Pflicht: Hersteller müssen ein
  Risikomanagementsystem als kontinuierlichen, iterativen Prozess über den gesamten
  Lebenszyklus einrichten, umsetzen, dokumentieren und aufrechterhalten. Das ist das
  gesetzliche Mandat hinter ISO 14971 §4.
- **GSPR 4 — dieselbe Prioritätsreihenfolge, gesetzlich.** Maßnahmen müssen, „in folgender
  Rangfolge", erfolgen: (a) Risiken durch sichere Gestaltung und Herstellung beseitigen/so
  weit wie möglich senken; (b) Schutzmaßnahmen, nötigenfalls einschließlich Alarmen; (c)
  Informationen für die Sicherheit und ggf. Schulung. Das ist der gesetzliche Zwilling von
  ISO 14971 §7.1.
- **GSPR 8** — Restrisiken und Nebenwirkungen müssen *minimiert und vertretbar sein, wenn
  sie gegen den bewerteten Nutzen abgewogen werden*, und die verbleibenden Restrisiken den
  Anwendern **offengelegt** werden. Das ist die gesetzliche Grundlage für ISO 14971 §8.
- **GSPR 17** — Software ist ausdrücklich erfasst: Produkte, die *elektronische
  programmierbare Systeme einschließlich Software* enthalten, und Software, die selbst ein
  Produkt ist, müssen nach dem Stand der Technik entwickelt werden, einschließlich
  Entwicklungslebenszyklus, Risikomanagement sowie Verifizierung und Validierung — was
  Software-Risikomanagement an IEC 62304 bindet.

**Wie Recht und Norm zusammentreffen: die Brücke „harmonisierte Norm".** Die MDR nennt die
Ziele (GSPR), nicht die Methode. Eine **harmonisierte Norm** ist eine, die die Europäische
Kommission im Amtsblatt zitiert hat; wendet man sie an, entsteht eine gesetzliche
**„Konformitätsvermutung"** — die Behörden vermuten, dass die abgedeckten Anforderungen
erfüllt sind. **EN ISO 14971:2019+A11:2021** wurde für MDR/IVDR durch den
Durchführungsbeschluss (EU) 2022/757 (2022) zitiert; die **Änderung A11 ergänzt die
„Anhang-Z"-Tabellen**, die die Klauseln der Norm den GSPR der MDR zuordnen. *Die Anwendung
von EN ISO 14971 ist somit der anerkannte Weg, die Risikomanagement-Anforderungen der MDR zu
erfüllen.* (Hinweis: die reine **ISO**-Ausgabe enthält **keinen Anhang ZA** — diese
EU-Zuordnung steht nur in der **EN**-Fassung.)

→ *Template:* [`../standards/CONFORMANCE.md`](../standards/CONFORMANCE.md) ist der gestufte
Normen-/Regulierungs-Index; [`../standards/GSPR-CHECKLIST.md`](../standards/GSPR-CHECKLIST.md)
bildet die software-relevanten GSPR auf Repo-Nachweise ab;
[ADR-0001](../adr/0001-mdsw-qualification.md) ist die lebende Entscheidung „Sind wir
überhaupt ein Medizinprodukt?", die festlegt, ob all dies verbindlich wird.

---

## 6. Wie das Template auf den Prozess abbildet

Eine einzige Tabelle zum Danebenlegen. Jeder ISO-14971-Schritt (oder Nachbarnorm-Schritt) →
das konkrete Template-Artefakt, das ihn operationalisiert → wo man ihn live sieht.

| Prozessschritt (Klausel) | Template-Artefakt | Live im Beispiel-Repo |
|---|---|---|
| Risikomanagementplan (14971 §4.4) | [`HARM_RISK.md`](../HARM_RISK.md) §1 Plantabelle | `docs/HARM_RISK.md` |
| Akzeptanz-Politik & -Kriterien (§4.2, §6) | die §4-Matrix („adopt consciously") + Politik-Zeile im Plan | — |
| Zweckbestimmung / Fehlanwendung (§5.2) | [ADR-0001](../adr/0001-mdsw-qualification.md); Feld *Ereignisfolge* | Issue #2 |
| Kette Gefährdung → Situation → Schaden (§5.4) | die vier Kettenfelder des Formulars; `hazard-cat:*` | [Issue #2](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/2) |
| Risikoeinschätzung, P1×P2 (§5.5; TR 24971 §5.5.2) | S-/P-/P1×P2-Felder; `HARM_RISK.md` §3 | Issue #2 |
| Beherrschungs-Hierarchie (§7.1) | Feld „Stufe je Maßnahme angeben"; `HARM_RISK.md` §5 | Issue #2 |
| Zwei Verifizierungen (§7.2) | Board-Feld `Control verification`; Verifizierungsplan-Feld | Harm-Risk-File-Board |
| Nutzen-Risiko (§7.4) | Nutzen-Risiko-Feld | — |
| Neue Risiken durch Maßnahmen (§7.5) | Pflicht-§7.5-Feld | Issue #2 |
| Vollständigkeit (§7.6) | §7.6-Häkchen | — |
| Gesamt-Restrisiko + Offenlegung (§8) | [`HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md); Label `disclose-in-ifu` | — |
| Überprüfung & Bericht (§9) | [`HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md) | — |
| Produktion/Nachproduktion (§10) | Field-Feedback- + SOUP-Anomalie-Formular; CVE→Register | [#4](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/4), [#5](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/5) |
| Software-Sicherheitsklasse (62304 §4.3) | [ADR-0002](../adr/0002-software-safety-classification.md) | `docs/adr/0002…` |
| SOUP (62304 §8.1.2/§5.3.3/§7.1.3) | [`soup.yaml`](../../soup.yaml) + [`SOUP.md`](../SOUP.md) + SOUP-Anomalie-Formular | Issue #4 |
| Security-Lebenszyklus (81001-5-1) | [`SECURITY_RISK.md`](../SECURITY_RISK.md) + [`SECURITY.md`](../../SECURITY.md) | — |
| MDR-GSPR / harmonisierte Norm | [`CONFORMANCE.md`](../standards/CONFORMANCE.md) + [`GSPR-CHECKLIST.md`](../standards/GSPR-CHECKLIST.md) | `docs/standards/` |

Für die *Situationen* („eine CVE kam herein", „ein Release steht an", „ein Pilotanwender hat
etwas gemeldet") ist der Schritt-für-Schritt-Begleiter [`../RECIPES.md`](../RECIPES.md).

---

## 7. Häufige Missverständnisse von Einsteigern

- **„Sicher heißt null Risiko."** Nein — Sicherheit ist „Freiheit von unvertretbarem
  Risiko" (14971 §3.26). Ein Restrisiko bleibt immer und muss bewusst akzeptiert werden.
- **„Ein Befund mit hohem Schweregrad ist automatisch ein hohes Risiko."** Nein — Risiko ist
  Schweregrad **und** Wahrscheinlichkeit zusammen (14971 §3.18). Ein katastrophaler, aber
  wirklich seltener Schaden und ein milder, aber häufiger sind verschiedene Risiken (eine
  gute Methode behandelt katastrophalen Schaden dennoch konservativ).
- **„Eine Gefährdung ist ein Schaden."** Nein — eine Gefährdung ist nur *potenziell*; sie
  wird erst über eine Gefährdungssituation zum Schaden (14971 §3.4–§3.5).
- **„Die billigste Maßnahme wählen."** Nein — die Rangfolge ist **verpflichtend**: sichere
  Gestaltung → Schutzmaßnahmen → Informationen für die Sicherheit (14971 §7.1; MDR GSPR 4).
- **„Der PR ist gemergt, also ist die Maßnahme verifiziert."** Das ist nur die *Umsetzung* —
  Sie schulden auch die *Wirksamkeit* (14971 §7.2).
- **„Jedes Einzelrisiko ist vertretbar, also passt es."** Nicht zwingend — das
  **Gesamt-Restrisiko** ist ein eigener, getrennter Beurteilungsschritt (14971 §8).
- **„AFAP heißt so niedrig, wie wir es uns leisten können."** Nein — *so weit wie möglich
  ohne nachteilige Beeinflussung des Nutzen-Risiko-Verhältnisses* (MDR GSPR 2); Kosten
  allein sind keine gültige Begründung.
- **„Die Norm gibt mir die Risikomatrix."** Nein — Sie legen die Kriterien fest (14971 §1,
  §4.2, §4.4); die Matrizen der TR 24971 sind *Beispiele*, die je Produkt zu begründen sind
  (TR 24971 §5.5.1).
- **„Klasse-A-Software bedeutet, keine Verletzung ist möglich."** Nein — Klasse A kann
  Software umfassen, die zu Schaden beitragen *könnte*, wenn externe Maßnahmen das Risiko
  vertretbar halten (62304 §4.3).

---

## 8. Glossar & woher Sie die echten Normen bekommen

**Glossar** (alle ISO 14971:2019 Abschnitt 3, sofern nicht anders angegeben): *Schaden*
§3.3 · *Gefährdung* §3.4 · *Gefährdungssituation* §3.5 · *Risiko* §3.18 · *Schweregrad*
§3.27 · *Restrisiko* §3.17 · *Sicherheit* §3.26 · *Risikoanalyse* §3.19 · *Risikobewertung*
§3.23 · *Risikobeurteilung* (Analyse + Bewertung) §3.20 · *Risikobeherrschung* §3.21 ·
*Risikomanagement* §3.24 · *Risikomanagementakte* §3.25 · *Nutzen* §3.2 · *Zweckbestimmung*
§3.6 · *vernünftigerweise vorhersehbare Fehlanwendung* §3.15 · *Stand der Technik* §3.28 ·
*SOUP* (62304 §3.29) · *Gebrauchsfehler* (62366-1 §3.21) · *Software-Sicherheitsklasse*
(62304 §4.3) · *Schlüsseleigenschaften: Sicherheit/Wirksamkeit/Security* (81001-1 §3.2.8) ·
*GSPR/GSLA* — grundlegende Sicherheits- und Leistungsanforderungen (MDR Anhang I) · *AFAP* —
so weit wie möglich (MDR GSPR 2) · *harmonisierte Norm / Konformitätsvermutung* (MDR +
Amtsblatt).

**Normen beschaffen** (sie sind urheberrechtlich geschützt; diese Einführung ist kein
Ersatz): ISO- und IEC-Normen über die offiziellen Kataloge (iso.org, webstore.iec.ch) oder
Ihr nationales Gremium (z. B. DIN, BSI, ANSI); die MDR ist kostenlos auf
[EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj). Für den EU-Risikomanagement-Weg
beschaffen Sie **DIN EN ISO 14971:2019+A11:2021** (die Fassung mit der Anhang-Z-Zuordnung)
und lesen **ISO/TR 24971:2020** daneben für das Wie.

---

*Teil des [risk-management-template](https://github.com/forschungsgruppe-digital-health/risk-management-template).
Lehrmaterial — keine Rechts-, Regulierungs- oder klinische Beratung. Verankert in den oben
genannten Normausgaben; die Klausel-Verweise erlauben es, jede Aussage gegen die Quelle zu
prüfen.*
