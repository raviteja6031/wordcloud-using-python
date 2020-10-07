# -*- coding: utf-8 -*-
"""wordcloud.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1breBWeKC5KGK7v40WRhoqk7F-_18vo7j
"""

!pip install wordcloud
import wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the","a",  "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    frequencies={}
    taken=[]
    for letter in punctuations:
        file_contents=file_contents.replace(letter,'')
    for i in uninteresting_words:
        w=' '+i+' '
        file_contents=file_contents.replace(w,'')
    for i in file_contents.split():
        if i.lower() not in taken:
            taken.append(i.lower())
            if i not in frequencies:
                frequencies[i]=1
            else:
                frequencies[i]+=1
        
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display your wordcloud image
text="pubg awm m416 scarl ump vector dbs greenade pubg pubg pubg thompson pubg awm m416 pubg pubg pubg pubg pubg pubg pubg pubg pubg pubg pubg pubg  scarl ump vector dbs greenade pubg awm m416 scarl ump vector dbs greenade pubg awm m416 scarl ump vector dbs greenade pubg awm m416 scarl ump vector dbs greenade pubg awm m416 scarl ump vector dbs greenade  stungreenade smoke greenade  vector dbs greenade thompson pubg awm m416 scarl ump vector dbs greenade thompson stungreenade smoke greenade  vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson pubg awm m416 scarl ump vector dbs greenade thompson stungreenade smoke greenade  vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson pubg awm m416 scarl ump vector dbs greenade thompson stungreenade smoke greenade  vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson pubg awm m416 scarl ump vector dbs greenade thompson stungreenade smoke greenade  vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson pubg awm m416 scarl ump vector dbs greenade thompson stungreenade smoke greenade  vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson stungreenade smoke greenade vector dbs greenade thompson stungreenade smoke greenade"
myimage = calculate_frequencies(text)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

