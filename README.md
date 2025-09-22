# Bankovní systém

Vytvoř systém, který po spuštění nabídne uživateli výběr příkazu:

```create, login, send, give, list, balance, logout```

## Popis příkazů:

### `create`
- Vyžaduje 2 vstupy:
  - **jméno uživatele** (na koho je účet napsán)
  - **heslo**
- Automaticky vygeneruje **číslo účtu**
- Po vytvoření účtu vypíše informace o účtu

---

### `login`
- Vyžaduje 2 vstupy:
  - **jméno**
  - **heslo**
- Přihlásí uživatele na účet, který odpovídá danému jménu a heslu

---

### `send`
- Vyžaduje 2 vstupy:
  - **číslo účtu příjemce**
  - **částku**
- Odešle částku z účtu přihlášeného uživatele na zadaný účet

---

### `give`
- **Adminský příkaz** pro testování
- Vyžaduje 1 vstup:
  - **částku**
- Přidá peníze aktuálně přihlášenému uživateli

---

### `list`
- Nevyžaduje vstup
- Vypíše seznam všech účtů a jejich zůstatků

---

### `balance`
- Nevyžaduje vstup
- Vypíše zůstatek aktuálně přihlášeného uživatele

---

### `logout`
- Odhlásí aktuálně přihlášeného uživatele

---

## Bezpečnostní požadavky

- **Přihlášení**: Heslo musí přesně odpovídat účtu, na který se uživatel pokouší přihlásit
- **Příkazy `send`, `give`, `balance`, `logout`**:
  - Není možné je spustit, pokud **není uživatel přihlášen**
- **Příkaz `send`**:
  - Vyhodí chybu, pokud **uživatel nemá dostatečné prostředky**
- **Chybějící vstupy**:
  - Při neúplném vstupu vypíše systém **chybovou hlášku**

---

## Ukládání dat

- Všechna data (např. **číslo účtu, balance, jméno, heslo**) se ukládají do samostatného souboru, aby po vypnutí a zapnutí aplikace zůstala zachována
- Doporučený formát pro ukládání: **JSON soubor**

---

## Bonus: Logování

- Implementovat jednoduchý logovací systém
- Ukládat informace do samostatného **`.txt` souboru**
- Log bude zaznamenávat:
  - Kdo (uživatel)
  - Jaký příkaz provedl
  - (Volitelně: datum a čas)
