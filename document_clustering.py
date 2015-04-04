#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <pcode.colasanti@gmail.comi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  /home/pi/Programming/Projects/DocumentClustering/Data/nltk_data/

import string
import nltk
import re
import math
from nltk.stem.snowball import SnowballStemmer

class DocumentClustering:
    def __init__(self):
        self.titles=[]
        self.synopsis_frequency=[]
        self.corpus_frequency={}
        self.ascii_codes= string.ascii_letters + ' '#string.punctuation + string.digits+' '
        self.data_path = "/home/pi/Programming/Projects/DocumentClustering/Data/"
        nltk.data.path.append(self.data_path+"nltk_data/")
        self.stemmer = SnowballStemmer("english")
        self.stopwords = nltk.corpus.stopwords.words('english')
        #for word in self.stopwords:
        #    print word,
        
    def read_titles(self):
        t_file =self.data_path+"text/title_list.txt"
        rf = open(t_file, 'r')
        for line in rf:
            newline = line.rstrip('\r\n')
            print newline
            self.titles.append(newline)
            
    def read_synopsis(self):
        t_file =self.data_path+"text/synopsis_list_imdb.txt"
        synopsis=''
        rf = open(t_file, 'r')
        count = 0
        for line in rf:
            if 'BREAKS HERE' in line:
                word_frequency = self.parse_synopsis(synopsis)
                self.synopsis_frequency.append(word_frequency)
                synopsis=''
                print count
                count+=1
            else:
                for c in line:
                    if c in self.ascii_codes:
                        synopsis+=c
        print
        for key in  self.corpus_frequency:
            self.corpus_frequency[key]= math.log(count/self.corpus_frequency[key])
            print key,self.corpus_frequency[key]
                        
    def parse_synopsis(self,synopsis):
        document_frequency={}
        for sent in nltk.sent_tokenize(synopsis):
            for word in nltk.word_tokenize(sent):
                l_word = word.lower()
                if not l_word in self.stopwords:
                    s_word = self.stemmer.stem(l_word)
                    
                    if s_word in document_frequency:
                        document_frequency[s_word]+=1
                    else:
                        document_frequency[s_word]=1
        
        number_of_words = len(document_frequency)
        for key in document_frequency:
            document_frequency[key] = document_frequency[key]/number_of_words 
            if key in self.corpus_frequency:
                self.corpus_frequency[key]+=1
            else:
                self.corpus_frequency[key]=1

        return  document_frequency


def main():
    dc = DocumentClustering()
    #dc.read_titles()
    dc.read_synopsis()
    print len(dc.corpus_frequency)
    return 0

if __name__ == '__main__':
    main()

