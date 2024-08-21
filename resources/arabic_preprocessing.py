import re
import string




class Arabic_preprocessing:
    
    
    def __init__(self):
        
        #preparing punctuations list
        arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
        english_punctuations = string.punctuation
        self.all_punctuations = set(arabic_punctuations + english_punctuations)

        
        
        self.arabic_diacritics = re.compile("""
                                         ّ    | # Tashdid
                                         َ    | # Fatha
                                         ً    | # Tanwin Fath
                                         ُ    | # Damma
                                         ٌ    | # Tanwin Damm
                                         ِ    | # Kasra
                                         ٍ    | # Tanwin Kasr
                                         ْ    | # Sukun
                                         ـ     # Tatwil/Kashida

                                     """, re.VERBOSE)

        
    def normalize_arabic(self, text):
        text = re.sub("[إأآاٱ]", "ا", text)
        text = re.sub("ى", "ي", text)
        text = re.sub("ة", "ه", text)  # replace ta2 marboota by ha2
        text = re.sub("گ", "ك", text)
        text = re.sub("\u0640", '', text)  # remove tatweel
        return text


    def remove_punctuations(self, text):
        return ''.join([c for c in text if c not in self.all_punctuations]) #remove punctuations


    def remove_diacritics(self, text):
        text = re.sub(self.arabic_diacritics, '', text)
        return text

    def remove_english_characters(self, text):
        return re.sub(r'[a-zA-Z]+', '', text)
    
    
    
    def preprocess_arabic_text(self, text):
        
        text = self.remove_punctuations(text)
        text = self.remove_diacritics(text)
        text = self.normalize_arabic(text)
        text = self.remove_english_characters(text)
        text = ' '.join([w for w in text.split() if len(w)>1 and w.isalpha()]) #remove one-character & numeric words
        return text

