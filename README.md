Maxs
====

Scraping Max's Taphouse and Cross-Referencing BeerAdvocate!

**Update**: Added functionality for Frisco Taphouse and The Ale House in Columbia!!!

I originally wanted to do all of this in a self-contained JS application, but it turns out that Google and Bing don't like you hammering on their servers, and Maxs.com has a restrictive `Access-Control-Allow-Origin` anyhow.  Python seemed like the next best option.

Requirements
====

- Python 2.7
- BeautifulSoup 4

Usage
====

    python maxs.py
    python frisco.py
    python alehouse.py

Example Output
====
 
```
 97  Firestone Walker Double Jack
 95  Allagash Curieux
 95  Great Divide Espresso oak Aged Yeti
 93  Oxbow Farmhouse pale
 93  Allagash White
 93  Sierra Nevada Bigfoot
 93  Thornbridge Bracia
 93  Bahnof Berliner Weisse w/ Brett
 92  Blaugies La Moneuse 
 92  Struise Rio Reserva 2008
 92  Boulevard Grainstorm
 92  Delirium Tremens
 92  Stillwater Ales As Follows
 92  Smuttynose IPA
 92  Carengie Stark Porter
 92  Chimay Cinq Cents
 91  Rodenbach Classic
 91  Sierra Nevada Kellerweiss
 91  Harpoon Leviathan Imperial IPA
 91  Victory Prima Pils
 91  Franziskaner Hefeweizen
 91  De Dolle Arabier
 91  Heavy Seas Loose Cannon
 90  The Bruery Saison De Lente
 90  Oskar Blues oSKAr G'Rauch
 90  Van Eecke Popering Hommel
 90  Mission Dark Seas
 90  Sixpoints Resin
 90  Scheldebrouwerij Hop Ruiter
 89  Boulevard 80 Acre
 89  Flying Dog Double Dog (Nitro)
 89  Stillwater Stateside Saison
 89  Evil Twin Femme Fatale Brett
 89  Sierra Nevada Ovila Quad w/ Plums
 88  Olivers 20th Anniversary
 88  Sierra Nevada Ruthless Rye IPA
 88  Lindemans Framboise
 88  Maine Mean Old Tom (Nitro)
 88  DuClaw Sweet baby Jesus
 88  Terrapin Rye Squared
 87  De Glazen Toren Canaster
 87  La Rulles Estivale
 87  Terrapin Barley Ryne
 87  Brewers Art Resurrection
 87  Contreras Valeir Extra
 87  La Rulles Cuvee Meilleurs Voeux
 87  Union Duckpin Pale Ale
 86  Oxbow Space Cowboy
 86  Harpoon Rich & Dan Rye IPA
 86  Van Steenberge Klokke Roeland
 86  Burley Oak Aboriginal Gangster
 86  Scheldebrouwerij Lamme Goedzak
 86  Heavy Seas Black Cannon
 85  New Belgium Rampant
 85  New Belgium/Dieu Du Ciel Heavenly Feijoa
 85  Fritz Briem Gratzer
 85  Burley Oak Rude Boy
 84  Van Eecke Cuvee Watou
 84  Blue Mountain  Steel Wheels
 84  Harpoon Black IPA
 84  Alvinne Undressed
 84  Terrapin Double Feature
 84  Sierra Nevada Blindfold 
 84  Hof Ten Dormaal Amber
 84  Guinness Stout
 84  Jandrain V Cense
 84  Cazeau Tournay Black
 83  Vapeur Saison De Pipaix
 83  New Belgium Shift
 83  Crispin Cider
 83  Heavy Seas BIG DIPA 
 82  New Belgium Fat Tire
 82  New Belgium Cascara Quad
 82  Harpoon Directors Cut
 81  Harpoon UFO Raspberry
 80  Steigl Lager
 79  Terrapin Tom Foolery
 78  Yuengling Lager
 78  Fruli Strawberry
 78  Blue Moon White
 77  Dupont Monks Stout
 76  Palm Ale
N/A  CCM Montseny Blat
N/A  Dominion Cherry Blossom Lager
N/A  Elysian Arboreal
N/A  Terrapin Full of Blarney(Nitro)
N/A  Het Nest Kleveretien
N/A  Troubadour Magma Sorachi Ace
N/A  Thornbridge Beadeca's Well
N/A  Flying Dog Pumpernickel IPA
N/A  Stift Gregerious
N/A  Thornbridge Breadeca's Well
N/A  Maine Peeper
N/A  Flying Dog Green Tea Imperial Stout
```