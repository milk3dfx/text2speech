# Text to speech with google translate
# https://translate.google.com/translate_tts?q=hello&tl=en

import urllib2
import urllib
import argparse

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Download anime series from Anidub')
	parser.add_argument('phrase', help='Phrase to speech')
	parser.add_argument('-r', type=str, nargs='?', default='en',
	choices=['en', 'ru'], help='Language (default: "en")')
	args = parser.parse_args()

	phrase = args.phrase
	language = "en"
	url = "https://translate.google.com/translate_tts?q=" + urllib.quote(phrase) + "&tl=" + language
	headers = { 'User-Agent' :  'vsreality/1.0'}
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	the_page = response.read()
	f = open('temp.mp3', 'wb')
	f.write(the_page)
	f.close()
	print "Done. See temp.mp3"