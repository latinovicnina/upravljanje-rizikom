# Project Status Report AI Agent

Jednostavan AI agent koji automatizuje izradu statusnih izveštaja o napretku projekta. Agent prima listu taskova (npr. iz JIRA backlog-a), analizira napredak, identifikuje rizike i blokere, i koristi LangChain i OpenAI model da generiše profesionalan status report u Markdown formatu.

## Problem koji agent rešava

Project manageri i product owneri redovno (nedeljno ili na kraju sprinta) moraju da pripreme status report za klijenta ili tim, na osnovu trenutnog stanja taskova. Ovaj proces se obično radi ručno: PM pregleda JIRA board, broji taskove po statusu, procenjuje rizike i piše izveštaj. Ovo traje 1-2 sata i podložno je propustima.

Agent automatizuje ovaj proces u tri koraka i generiše konzistentan, strukturisan izveštaj za nekoliko sekundi.

## Kome je namenjen

- **Project Manager** - za nedeljne status reportove klijentima i menadžmentu
- **Product Owner** - za praćenje napretka sprinta
- **Scrum Master** - za pripremu retrospektiva i identifikaciju blokera

## Arhitektura i workflow

Agent je implementiran kroz dva fajla:

- `report_generator.py` - sadrži tri koraka obrade (analiza napretka, identifikacija rizika, generisanje finalnog izveštaja pomoću LLM-a)
- `main.py` - ulazna tačka aplikacije, sadrži listu taskova i pokreće generisanje izveštaja

**Tok izvršavanja:**

1. **Analiza napretka** (`analyze_progress`) - deterministički korak koji broji taskove po statusu (Done, In Progress, To Do) i računa procenat završenosti.
2. **Identifikacija rizika i blokera** (`identify_risks`) - deterministički korak koji prepoznaje obrasce koji ukazuju na rizik: visok-prioritetni taskovi koji nisu započeti, taskovi bez zaduženog lica, preopterećenost tima.
3. **Generisanje izveštaja** (`generate_status_report`) - AI korak koji koristi LangChain (`ChatPromptTemplate` + `ChatOpenAI` + `StrOutputParser`) da na osnovu prethodna dva koraka generiše čitljiv, profesionalan Markdown izveštaj sa tri sekcije: pregled napretka, identifikovani rizici, preporuke za sledeće korake.

Ovim pristupom se kombinuje precizna, deterministička logika (brojanje i pravila za rizike) sa LLM komponentom koja prevodi te podatke u prirodan, čitljiv tekst - slično pristupu koji je korišćen i na vežbama za GitHub Repository Analyzer.

## Tehnologije

- Python 3.10+
- LangChain (`langchain`, `langchain-openai`)
- OpenAI API (model `gpt-4o-mini`)
- python-dotenv za upravljanje API ključem

## Instalacija i pokretanje

1. Kloniraj repozitorijum i otvori folder u VS Code-u.

2. Instaliraj potrebne biblioteke:

```
pip install -r requirements.txt
```

3. Kreiraj `.env` fajl u root folderu (na osnovu `.env.example`) i upiši svoj OpenAI API ključ:

```
OPENAI_API_KEY=tvoj_openai_api_kljuc
```

4. Pokreni aplikaciju:

```
python main.py
```

5. Agent će ispisati status report u terminalu i sačuvati ga u fajl `status_report.md`.

Da bi se testirao agent na drugim podacima, potrebno je izmeniti listu `tasks` u `main.py` sa drugim taskovima, statusima, prioritetima i zaduženim licima.

## Primer ulaza

```python
tasks = [
    {
        "name": "Implementirati autentifikaciju",
        "status": "Done",
        "assignee": "Marko",
        "priority": "High",
    },
    {
        "name": "Napisati testove",
        "status": "In Progress",
        "assignee": "Ana",
        "priority": "Medium",
    },
]
```

## Primer izlaza

Agent generiše Markdown izveštaj sa sledećim sekcijama:

- **Project Progress Summary** - broj i procenat taskova po statusu
- **Identified Risks and Blockers** - lista prepoznatih rizika
- **Recommendations for Next Steps** - konkretne preporuke za PM-a

## Testiranje

Agent je testiran na tri različita scenarija:

1. **Mešani projekat** (50% završeno) - prikazuje uobičajen tok rada sa jednim manjim rizikom (jedan neassignovan task)
2. **Zdrav projekat** (80% završeno) - agent korektno prepoznaje da nema značajnih rizika
3. **Kritičan projekat** (0% završeno, više neassignovanih visoko-prioritetnih taskova) - agent prepoznaje ozbiljne rizike i daje konkretne preporuke

U sva tri slučaja agent je generisao tačan, koherentan i upotrebljiv izveštaj koji odgovara unetim podacima.

## Ograničenja

- Agent trenutno radi sa ručno unetom listom taskova u `main.py`; nije direktno povezan sa JIRA API-jem (moguće proširenje u budućnosti).
- Identifikacija rizika je zasnovana na jednostavnim, unapred definisanim pravilima, a ne na ML modelu - dovoljno za MVP, ali ne hvata sve moguće tipove rizika.
- Kvalitet finalnog izveštaja zavisi od korišćenog OpenAI modela i može se razlikovati između pokretanja.
- Nema perzistencije istorije izveštaja - svaki put se generiše nov fajl `status_report.md`.

## Mogućnosti za unapređenje

- Direktna integracija sa JIRA API-jem za automatsko povlačenje taskova iz backlog-a.
- Čuvanje istorije izveštaja kroz vreme radi praćenja trenda napretka.
- Proširenje pravila za identifikaciju rizika (npr. analiza datuma dospeća, brzine napredovanja).
- Dodavanje podrške za slanje izveštaja direktno na email ili Slack.