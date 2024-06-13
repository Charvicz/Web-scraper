Volební skraper
○ co jde v projektu?
Tento skript umožňuje ziskat výsledky parlamentních voleb z roku 2017 pro konkrétní okres z této webové stránky a uložit je do CSV souboru.
 Jak na to?
Před spuštěním projektu si nainstalujte potřebné knihovny uvedené vsouboru requirements.txt.Skript spustite z příkazového řádku pomocí následujícího příkazu:
 python main.py <odkaz_uzemniho_celku> <vystupni_soubor>
Výstupem bude soubor .csv S výsledky voleb pro daný okres.
Jak to vypadá v praxi?
Například pro Olomoucký kraj:
Odkaz -> https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 2. Název výstupního souboru -> volby.csv
Spuštění programu:
python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" volby.csv"
