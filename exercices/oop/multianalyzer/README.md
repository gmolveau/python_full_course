## Programmation objet

NB: l'utilisation des `dataclass` est autorisée.

Suite à une réunion avec le service commercial de votre entreprise, les besoins  de potentiels utilisateurs d'un produit qui n'existe pas encore sont exprimés. Votre mission consiste à imaginer et concevoir ce produit (POC / Proof-Of-Concept).

Dans le cadre de cet exercice, aucune logique d'analyse ne sera implémentée, des valeurs par défaut seront retournées.

Votre chef vous demande que ce POC soit codé en python. Ce chef est très pointilleux et vous imposera des choses, comme certains paradigmes de programmation pour certaines fonctionnalités du produit, ou bien des noms de classes et fonctions.

Dans le cadre de cet exercice, on imagine que du TDD (Test Driven Development) a été mis en place. Cela signifie simplement que des jeux de test vous sont fournis pour tester vos solutions.

### Le produit

Le produit qui doit être codé est un multi-analyseur de malware. Le but de ce produit est d'analyser un fichier avec plusieurs analyseurs et de fournir un rapport à la fin.

Par exemple, un utilisateur soumet un fichier `bizarre.pdf` à l'outil, il selectionne un analyseur anti-virus, un analyseur yara et un analyseur de PDF.

Le produit va donc lancer toutes les analyses et créer un rapport à la fin.

### Etude du besoin (3 points)

- un résultat (`Result`) d'un `Service` est composé d'un `score` sous forme d'un entier et des indicateurs de compromissions (`iocs`) sous la forme d'une liste de string.

- un rapport (`Report`) est composé de résultats. La représentation sous forme de string d'un rapport contient un score qui est égal à la somme des scores des résultats, ainsi que la liste triée par ordre alphabétique complète de tous les `iocs` de tous les résultats.
La représentation sous forme de string du rapport doit avoir la forme suivante :

```
Report :
- score = <score>
- iocs :
  - <ioc1>
  - <ioc2>
```

voici un exemple :

```
Report :
- score = 1000
- iocs :
  - cestpasnous.com
  - 1.1.1.1
```

- un service (`Service`) est composé d'un nom (`name`) sous la forme d'une string. Un service doit être en mesure d'analyser un fichier via son chemin `filepath` qui est une string, et de renvoyer un résultat (`Result`).

- notre outil est un `MultiAnalyzer`. Cet outil est composé d'une liste de services. Pour utiliser le `MultiAnalyzer`, l'utilisateur passera par la méthode `analyze` en spécifiant le fichier via son chemin `filepath` sous forme de string, ainsi que la liste des noms des `services` à utiliser sous forme de liste de string. Cette analyse renverra un rapport (`Report`).

### Exercice

- pour cet exercice, vous devez :
  - coder le multi-analyzer et toutes les autres classes nécessaires ;
  - inventer 3 services :
    - un service fictif ayant pour nom `Yara`, qui renverra toujours un résultat avec un `score` de `500` et une liste d'`iocs` composée d'une seule adresse IP `1.1.1.1` ;
    - un service fictif nommé `ScanPDF`, qui renverra toujours un résultat avec un `score` de 0 et une liste d'`iocs` composée d'un seul nom de domaine `cestpasnous.com` ;
    - un service fictif nommé `Antivirus`, qui renverra toujours un résultat avec un `score` de `500` et aucun `iocs`.
  - instancier votre multi-analyzer que vous nommerez `tool`, en lui spécifiant les 3 services fictifs.

Ensuite nous allons tester ce multi-analyzer en lui soumettant un fichier fictif `bizarre.pdf` et en sélectionnant les services `Yara`, `ScanPDF` et `Antivirus` (qui correspondent aux 3 services fictifs).

Votre produit devra donc lancer toutes les analyses (fictives) et fournir un rapport (fictif) à la fin.

Ce rapport aura un score de `1000` et une liste de 2 `iocs` : `1.1.1.1` et `cestpasnous.com`.

Voici à quoi devra ressembler la représentation sous forme de string du rapport d'analyse final :

```
Report :
- score = 1000
- iocs :
  - 1.1.1.1
  - cestpasnous.com
```
