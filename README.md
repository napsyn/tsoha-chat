# Hackfeed - hakkerien blogi
Ideana on sovellus, joka toimii hakkeritoiminnan blogina hacklabeille, tekijätiloille ja hakkerimielisille. Jäsenet voivat luoda uusia julkaisuja, missä
he kertovat vaikkapa juuri valmistuneen löylykauhan tekovaiheista. Julkaisuille voi antaa avainsanoja, joilla niitä voidaan kategorisoida ja listata rajausten avulla.
Julkaisuissa näkyy sisällön lisäksi käyttäjänimi, julkaisuaika, sekä kommentit.

Päänäkymä kirjautuessa näyttää muutaman viimeisimmistä julkaisuista, jota voi rajausten avulla muuttaa näyttämään käyttäjän haluamia julkaisuja.

Ylläpitäjillä on oikeus hallinnoida käyttäjiä ja sisältöä, sekä antaa moderointioikeuksia perustason käyttäjille.

Sovellus on vielä hieman karu, mutta siinä toimii jo käyttäjien hallinta ja julkiasujen luominen/hakeminen. Julkaisuihin tulee vielä huomattavia muutoksia ––
tajusin esimerkiksi, ettei ole mitään järkeä näyttää julkaisun sisältöä listauksessa. Tulen vaihtamaan listauksessa sisällön tilalle julkaisun otsikon, jonka käyttäjä syöttää
tehdessä julkaisua. Lisäsin juuri kategoriat ja käyttäjätasot, mutten ehtinyt testata niitä, joten älkää ihmetelkö.

Sovelluksessa voi nyt testata kirjautumista ja julkaisujen tekoa. Käyttöliittymä on hyvin supraviivainen, joten sen kanssa ei pitäisi tulla ongelmia.

Komennot käynnistykseen:

python3 -m venv venv

source venv/bin/activate

pip install -r ./requirements.txt

Lisää enviin ympäristömuuttujat

psql < schema.sql

flask run



