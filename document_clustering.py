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
#  

import string

class DocumentClustering:
    def __init__(self):
        self.titles=[]
        self.ascii_codes= string.ascii_letters + string.punctuation + string.digits+' '
        
    def read_titles(self):
        t_file = "/home/pi/Programming/Projects/DocumentClustering/Data/title_list.txt"
        rf = open(t_file, 'r')
        for line in rf:
            newline = line.rstrip('\r\n')
            print newline
            self.titles.append(newline)
            
    def read_synopses(self):
        t_file = "/home/pi/Programming/Projects/DocumentClustering/Data/synopses_list_imdb.txt"
        synopses=''
        count = 0
        rf = open(t_file, 'r')
        for line in rf:
            if 'BREAKS HERE' in line:
                print count,synopses
                synopses=''
                count+=1
            else:
                for c in line:
                    if c in self.ascii_codes:
                        synopses+=c
        



def main():
    dc = DocumentClustering()
    #dc.read_titles()
    dc.read_synopses()
    return 0

if __name__ == '__main__':
    main()

