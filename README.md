# Personregister i testmiljön

Ett enkelt system för att hantera testdata på ett GDPR-kompatibelt sätt.

## Funktioner

- Skapa och initiera databas med testanvändare
- Visa alla användare
- Rensa all testdata (GDPR åtgärd 1)
- Anonymisera användardata (GDPR åtgärd 2)

## Förutsättningar

- Docker och Docker Compose installerat
- Python 3.9+ (om du kör utan Docker)

## Kör med Docker

1. Klona repot:

```bash
git clone <your-repo-url>
cd personregister-testmiljo

