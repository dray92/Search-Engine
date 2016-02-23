#!/usr/bin/env python

from __future__ import print_function
import sys
import gc
from collections import defaultdict
from porterStemmer import PorterStemmer

porterStemmer = PorterStemmer();

class SearchEngine:
    # stopwords -> filename containing stopwords
    # collections -> filename for collections file
    # index -> output file that will contain inverted index

    def __init__(self):
        self.index = defaultdict(list)


    def getParams(self):
        '''
            USAGE: python SearchEngine.py
            [stopwords file] [collection file] [output index file]
        '''
        params = sys.argv
        if len(params) != 4:
            # print error message to stderr
            print("USAGE: python SearchEngine.py [stopwords file] [collection file] [output index file]", file=sys.stderr)
            sys.exit(0);

        # param[0] -> script name
        self.stopwordsfile = params[1]
        self.collections = params[2]
        self.index = params[3]


    # read in words from the stopwords file
    def getStopwords(self):
        f = open(self.stopwordsfile, 'r')
        stopwords = [line.rstrip() for line in f]
        self.stopwords = dict.fromkeys(stopwords)
        f.close();

    # get the ID, title, text of the next page in the collection
    def parseCollections(self):



    def createIndex(self):
        ''' get the file of xml contents
            and parse it to build inverted index '''

        # get parameters passed in
        self.getParams()

        # open collection file
        self.colFile = open(self.collections, 'r')

        self.getStopwords()

        ''' might want to disable the garbage collector
            here since as the size of a list grows,
            insert takes O(N) instead of O(1) '''
        gc.disable()

        pageDict = {}
        pageDict = self.parseCollections()

if __name__=="__main__":
    c=SearchEngine()
    c.createIndex()
