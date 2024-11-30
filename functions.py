prefixes = ['non', 'omni', 'post', 'pre', 'pro', 're', 'un', 'im', 'dis', 'ab', 'ir', 'mis', 'anti']

suffixes = ['able', 'less', 'ful', 'ment', 'er', 'est', 'ed', 'tion', 's', 'ship', 'ly', 'ness']

pronous = ['I', 'you', 'he', 'she', 'it', 'we', 'they']

possessive_pronous = ['my', 'your', 'his', 'her', 'our', 'their']




def clean_words(words):
	for w in words:
		if w.endswith('.') or w.endswith(','):
			w.replace('.', '')
			w.replace(',', '')
		else:
			print(w)



def find_prefix(words):
	for w in words:
		for p in prefixes:
			if w.startswith(p):
				print(w)


def find_suffix(words):
	for w in words:
		for s in suffixes:
			if w.endswith(s):
				print(w)





def find_pronoun(words):
	for w in words:
		if w in pronous:
			print(f"({w}, 'Pronoun')")
		elif w in possessive_pronous:
			print(f"({w}, 'Possive Pronoun')")
		else:
			print(w)




