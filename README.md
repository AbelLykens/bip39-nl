# bip39-nl



mkdir source

wget -O source/nl.zip https://opus.nlpl.eu/download.php?f=OpenSubtitles/v2016/xml/nl.zip

wget -O source/opentaal.csv https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/elements/basiswoorden-gekeurd.txt

cd source

`unzip nl.zip OpenSubtitles/xml/nl/2014/*`

mkdir xml

`find OpenSubtitles/ -type f -name "*xml" -exec mv {} xml/ ';'`

cd ..

