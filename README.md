# bip39-nl

Download https://opus.nlpl.eu/download.php?f=OpenSubtitles/v2016/xml/nl.zip and extract

mkdir source
wget -O source/nl.zip
cd source
`unzip nl.zip OpenSubtitles/xml/nl/2014/*`
mkdir xml
`find OpenSubtitles/ -type f -name "*xml" -exec mv {} xml/ ';'`
cd ..
