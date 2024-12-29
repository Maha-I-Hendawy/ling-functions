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

# Adjectives:

adjective_endings = ['ful', 'ous', 'y', 'less', 'al', 'ic', 'ish']


Determiners:

definite_articles = ['the'] 
indefintie_articles = ['a', 'an']
demonstrative_determiners = ['this', 'that', 'these', 'those']
interrogative_determiners = ['who', 'whose', 'which']
possessive_determiners = ['my', 'your', 'his', 'her', 'its', 'our', 'their']

# Verbs:

verb_to_be_present = ["am", "'m", "is", "'s", "are", "'re"]

verb_to_be_past = ['was', 'were']

verb_to_have_present = ["have", "has", "'ve", "'s"]

verb_to_have_past = ['had']

# verb endings:

present = ['s', 'es', 'ies'] 

past = ['d', 'ed', 'ied']

# Adverbs:

adverb_endings = ['ly']

# Prepositions:

 
prep_of_time = ['in', 'on', 'at', 'past', 'during', 'by', 'before', 'until']

prep_of_place = ['under', 'underneath', 'over', 'inside', 'beside', 'in', 'in front of', 'on top of', 'in the middle of']

prep_of_direction = ['after', 'down', 'along', 'through', 'towards', 'past', 'away from', 'out of']

# Conjunctions:

conjunctions = ['and', 'or', 'but']

# Interjections:

interjections = ['oh', 'uh', 'huh', 'wow', 'yuck', 'yum']

punctuation = [',', ';', ':', '!', '?', '.']






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










