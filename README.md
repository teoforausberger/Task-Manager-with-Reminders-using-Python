# Task Manager with Reminders

# Descriere Proiect

Acest proiect reprezintă o aplicație realizată în Python de tip **To-Do
List**, care permite gestionarea taskurilor zilnice împreună cu un
sistem simplu de reminder.

Programul permite: - Adăugarea unui task cu termen limită - Afișarea
taskurilor existente - Calcularea timpului rămas până la termen -
Editarea unui task - Ștergerea unui task - Marcarea unui task ca fiind
completat

Proiect realizat pentru disciplina Python -- Grupa 424E.

------------------------------------------------------------------------

# Tehnologii utilizate

-   Limbaj: Python 3
-   Modul utilizat: datetime (biblioteca standard)

------------------------------------------------------------------------

# Structura proiectului

-   taskbook.py → Codul principal al aplicației
-   Documentatie_python.docx → Documentația teoretică a proiectului
-   README.md → Documentația proiectului (acest fișier)

------------------------------------------------------------------------

# Funcționalitate

Programul definește o clasă `TASK` care gestionează o listă de taskuri
folosind un dicționar Python.

Fiecare task este stocat sub forma:

    "Nume task" : "HH:MM"

Funcționalități principale:

### Adăugare task

Introducere de la tastatură în format: exemplu la ora 15:00

### Afișare taskuri

Afișează lista completă și timpul rămas până la termen.

### Calcul timp rămas

Se calculează diferența dintre ora curentă și ora taskului.

### Editare task

Permite modificarea numelui și orei unui task existent.

### Ștergere task

Elimină un task din listă.

### Completare task

Marchează taskul ca finalizat și îl elimină din listă.

------------------------------------------------------------------------

## Rulare program

1.  Asigură-te că ai instalat Python 3.

2.  Deschide terminalul în folderul proiectului.

3.  Rulează comanda:

    python taskbook.py

4.  Urmează instrucțiunile afișate în consolă.

------------------------------------------------------------------------

# Posibile îmbunătățiri

-   Validare mai strictă a formatului orei
-   Salvare taskuri în fișier (persistență date)
-   Interfață grafică (Tkinter)
-   Notificări reale folosind threading
-   Suport pentru date calendaristice (zi/lună/an)

------------------------------------------------------------------------

# Autori

Forausberger Teodor
Gheorghe Rareș
Grupa 424E
