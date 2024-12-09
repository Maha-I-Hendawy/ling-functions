# Affixes

prefixes = ['non', 'omni', 'post', 'pre', 'pro', 're', 'un', 'im', 'dis', 'ab', 'ir', 'mis', 'anti']

suffixes = ['able', 'less', 'ful', 'ment', 'er', 'est', 'ed', 'tion', 's', 'ship', 'ly', 'ness']


possessive_determiners = ['my', 'your', 'his', 'its', 'her', 'our', 'their']

# Pronouns:

# Personal Pronouns  

subject_pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']  

object_pronouns = ['me', 'you', 'him', 'her', 'it', 'us', 'them']

# Reflexive Pronouns 

reflexive_pronouns = ['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'themselves']

# Possessive Pronouns 

possessive_pronouns = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs']

# Interrogrative Pronouns 

interrogrative_pronouns = ['who', 'whom', 'what', 'whose', 'which']

# Demonstrative Pronouns  

demonstrave_pronouns = ['this', 'that', 'these', 'those']

# Indefinite Pronouns 

indefinite_pronouns = ['all', 'another', 'any', 'anybody', 'anyone', 'both', 'each', 'either', 'everybody', 'everyone', 'few', 'many', 'most', 'neither', 'nobody', 'none', 'no one', 'one', 'other', 'several', 'some', 'somebody', 'someone', 'such']




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




