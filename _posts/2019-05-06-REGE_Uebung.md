---
layout: post
title: "Regular Expression Übung"
---



======================================================
*===RE :  More than one Road leads to Rome===
======================================================



**PART I

***1. What regular expression matches each of the following?
	
    >**\w[ea]**  or   **eat(s|en)?|ate**    

***2. Find all Qadhdhafis... 

    >**\w[f]**



***3. Find all variations of Iṣbahān
	(construct the shortest possible regular expression):

    >**\w[*n,]**



**PART II (more practice)

***1. Conversion: Convert “Askin, Leon” > “Leon Askin” 

    >**\t(\w+),(\w+)$ \t\2 \1**



***2. Simple: Construct regular expressions that finds references all Austrian cities.
    >1)**find ,  replace | **	

	>**2)Vienna|Graz|Linz|Salzburg|Innsbruck|Klagenfurt|Villach|Wels|Sankt Pölten|Dornbirn|Wiener Neustadt|Steyr|Feldkirch|Bregenz|Leonding|Klosterneuburg|Baden bei Wien|Wolfsberg|Leoben|Krems|Traun|Amstetten|Lustenau|Kapfenberg|Mödling|Hallein|Kufstein|Traiskirchen|Schwechat|Braunau am Inn|Stockerau|Saalfelden|Ansfelden|Tulln|Hohenems|Spittal an der Drau|Telfs|Ternitz|Perchtoldsdorf|Feldkirchen|Bludenz|Bad Ischl|Eisenstadt|Schwaz|Hall in Tirol|Gmunden|Wörgl|Wals-Siezenheim|Marchtrenk|Bruck an der Mur|Sankt Veit an der Glan|Korneuburg|Neunkirchen|Hard|Vöcklabruck|Lienz|Rankweil|Hollabrunn|Enns|Brunn am Gebirge|Ried im Innkreis|Bad Vöslau|Waidhofen|Knittelfeld|Trofaiach|Mistelbach|Zwettl|Völkermarkt|Götzis|Sankt Johann im Pongau|Gänserndorf|Gerasdorf bei Wien|Ebreichsdorf|Bischofshofen|Groß-Enzersdorf|Seekirchen am Wallersee|Sankt Andrä**

3. More Difficult: Construct regular expression that finds only cities from 1) Lower Austria; 2) Salzburg.

    >**\w\s\W\Salzburg** , **\w\s\W\Lower** or **\b([\w ]+) \(Lower Austria\)**

	
