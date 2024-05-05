# Hackfeed - hakkerien blogi
Ideana on sovellus, joka toimii hakkeritoiminnan blogina hacklabeille, tekijätiloille ja hakkerimielisille. Jäsenet voivat luoda uusia julkaisuja, missä
he kertovat vaikkapa juuri valmistuneen löylykauhan tekovaiheista. Julkaisuille voi antaa avainsanoja, joilla niitä voidaan kategorisoida ja listata rajausten avulla.
Julkaisuissa näkyy sisällön lisäksi käyttäjänimi, julkaisuaika, sekä kommentit.

Päänäkymä kirjautuessa näyttää muutaman viimeisimmistä julkaisuista, jota voi rajausten avulla muuttaa näyttämään käyttäjän haluamia julkaisuja.

Ylläpitäjillä on oikeus hallinnoida käyttäjiä ja sisältöä, sekä antaa moderointioikeuksia perustason käyttäjille.

Sovelluksessa voi nyt luoda oletuskäyttäjän, jolla on pääsy päänäkymään ja omalle sivulle. Päänäkymässä on lista kaikista julkaisuista ja suodatin, jonka avulla voi karsia julkaisuja kategorioiden avulla. Päänäkymässä on myös mahdollista luoda uusi julkaisu, joka tulee näkyviin julkaisun jälkeen. Omalla sivulla voi nähdä omat julkaisut ja halutessaan poistaa niitä. Admineilla ja moderaattioreilla on pääsy käyttäjien hallistaan tarkoitetulle sivulle, jossa kukin näkee oman käyttötasonsa käyttäjät ja peruskäyttäjät. Käyttäjille voi antaa mitä tahansa käyttöoikeuksia, mutta moderoivat käyttäjät eivät pääse admin-käyttäjiin käsiksi muutoksen jälkeen. Käyttäjiä voi myös poistaa hallintanäkymästä.

Komennot käynnistykseen:

python3 -m venv venv

source venv/bin/activate

pip install -r ./requirements.txt

Lisää enviin ympäristömuuttujat

psql < schema.sql

flask run

Tietokantaan on luotu valmiiksi roolit ja kategoriat. Ensimmäisen admin-käyttäjän joudut luomaan itse ja manuaalisesti muuttamaan käyttäjätason tietokannassa.

Jos haluat muuttaa tyylejä, käytä seuraavaa komentoa:
npx tailwindcss -i ./app/static/main.css -o ./app/static/output.css --watch



