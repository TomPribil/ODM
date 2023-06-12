# Obsah

- [Obsah](#obsah)
  - [1. Databázový server](#1-databázový-server)
  - [2. Výběr datové sady](#2-výběr-datové-sady)

## 1. Databázový server
- Pro zpracování a maniplaci s daty byla použita databáze MySQL a pro správu byl použit nástroj phpMyAdmin.
- Celá tato infrastruktura - MySQL databáze a phpMyAdmin - byla nastavena v Dockeru, který umožňuje vytvořit izolované prostředí (kontejner), což usnadňuje nastavení a přenositelnost projektu.
- K vizualizaci a analýze dat byl použit Metabase, což je nástroj, který umožňuje snadno vytvářet grafy a dashboardy bez nutnosti psaní SQL dotazů.

## 2. Výběr datové sady
- V rámci tohoto projektu jsem se rozhodl využít dat z databáze Coffee Quality Institute (CQI). CQI je nezisková organizace se sídlem v Kalifornii, USA, která provádí širokou škálu aktivit v oblasti výzkumu, školení a certifikace s cílem zlepšit standardy kvality kávy, podporovat udržitelnost a podporovat rozvoj průmyslu se specializovanou kávou.
- Tato datová sada byla vybrána pro její rozsáhlé informace o kvalitě kávy, které pokrývají mnoho aspektů, včetně senzorických hodnocení, jako jsou aroma, chuť, dochuť, kyselost, vyváženost, čistý šálek a sladkost. Navíc sada obsahuje také data o defektech v kávových zrnech, které mohou ovlivnit její celkovou kvalitu.
- CQI spravuje databázi na svých webových [stránkách](https://database.coffeeinstitute.org/coffees/arabica).
- Data v csv formátu jsou dostupná na serveru Kaggle na následujícím [odkazu](https://www.kaggle.com/datasets/fatihb/coffee-quality-data-cqi?resource=download).
