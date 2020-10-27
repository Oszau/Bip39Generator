#!/usr/bin/env python
# encoding: utf-8
"""


#  Bip39 by TheRealLordFractal 2019

"""

import sys
import getopt
import random

#sys.stdout = open('output.txt','wt')

help_message = '''
Bip39 12 Word Random Generator By TheRealLordFractal
Output File Saved as 12words.txt
Command Exntensions:
-n <x> or --number <x>: Number of sample code phrases given. (Default is 5)
-w <file> or --wordlist <file>: Uses another wordlist to generate code phrases from.
-b: Brute static -c: Charset num -o Offset file start -s: Space unused
'''

#CODEWORDS = open('wordlist.txt', 'r').readlines()

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def generate(brute=False, space=True, charset=3, off_set=0, prefix=False, number=5):
  strnum = len(CODEWORDS)
  if brute == True:
    #strnum = len(CODEWORDS)
    st1 = off_set
    st2 = 0 #off_set
    st3 = 0 #off_set
    st4 = 0 #off_set

    if charset == 2:
      while st1 < strnum:
        word1 = CODEWORDS[st1]
        while st2 < strnum:
          word2 = CODEWORDS[st2]
          #print "%s %s" % (word1.rstrip(), word2.rstrip())
          if space == True:
            print "%s %s" % (word1.rstrip(), word2.rstrip())
          else:
            print "%s%s" % (word1.rstrip(), word2.rstrip())
          st2 += 1
        st1 += 1
        st2 = 0

    if charset == 3:
      while st1 < strnum:
        word1 = CODEWORDS[st1]
        while st2 < strnum:
          word2 = CODEWORDS[st2]
          while st3 < strnum:
            word3 = CODEWORDS[st3]
            #print "%s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip())
            if space == True:
              print "%s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip())
            else:
              print "%s%s%s" % (word1.rstrip(), word2.rstrip(), word3.rstrip())
            st3 += 1
          st2 += 1
          st3 = 0
        st1 += 1
        st2 = 0

    elif charset == 4:
      while st1 < strnum:
        word1 = CODEWORDS[st1]
        while st2 < strnum:
          word2 = CODEWORDS[st2]
          while st3 < strnum:
            word3 = CODEWORDS[st3]
            while st4 < strnum:
              word4 = CODEWORDS[st4]
              #print "%s %s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip())
              if space == True:
                print "%s %s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip())
              else:
                print "%s%s%s%s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip())
              st4 += 1
            st3 += 1
            st4 = 0
          st2 += 1
          st3 = 0
          st3 = 0
        st1 += 1
        st2 = 0
        st4 = 0

  else:
    while number > 0:        
        if prefix == 'TRUE':
           print ("Not Supported.")
           # word1 = PREFIXES[int(random.uniform(0,len(PREFIXES)))]
        elif prefix:
            word1 = prefix
        else:
            #word1 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word2 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word3 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word4 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word5 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word6 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word7 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word8 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word9 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word10 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word11 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]
            #word12 = CODEWORDS[int(random.uniform(0,len(CODEWORDS)))]

            word1 = CODEWORDS[int(random.uniform(0,strnum))]
            word2 = CODEWORDS[int(random.uniform(0,strnum))]
            word3 = CODEWORDS[int(random.uniform(0,strnum))]
            word4 = CODEWORDS[int(random.uniform(0,strnum))]
            word5 = CODEWORDS[int(random.uniform(0,strnum))]
            word6 = CODEWORDS[int(random.uniform(0,strnum))]
            word7 = CODEWORDS[int(random.uniform(0,strnum))]
            word8 = CODEWORDS[int(random.uniform(0,strnum))]
            word9 = CODEWORDS[int(random.uniform(0,strnum))]
            word10 = CODEWORDS[int(random.uniform(0,strnum))]
            word11 = CODEWORDS[int(random.uniform(0,strnum))]
            word12 = CODEWORDS[int(random.uniform(0,strnum))]
            if charset == 12:
              if space == True:
                print "%s %s %s %s %s %s %s %s %s %s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip(), word5.rstrip(), word6.rstrip(), word7.rstrip(), word8.rstrip(), word9.rstrip(), word10.rstrip(), word11.rstrip(), word12.rstrip())
              else:
                print "%s%s%s%s%s%s%s%s%s%s%s%s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip(), word5.rstrip(), word6.rstrip(), word7.rstrip(), word8.rstrip(), word9.rstrip(), word10.rstrip(), word11.rstrip(), word12.rstrip())
            if charset == 4:
              if space == True:
                print "%s %s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip())
              else:
                print "%s%S%S%s" % (word1.rstrip(), word2.rstrip(), word3.rstrip(), word4.rstrip())
            if charset == 3:
              if space == True:
                print "%s %s %s" % (word1.rstrip(), word2.rstrip(), word3.rstrip())
              else:
                print "%s%s%s" % (word1.rstrip(), word2.rstrip(), word3.rstrip())
            if charset == 2:
              if space == True:
                print "%s %s" % (word1.rstrip(), word2.rstrip())
              else:
                print "%s%s" % (word1.rstrip(), word2.rstrip())
        number -= 1
    

def main(argv=None):
    
    number = 5
    prefix = False
    brute = False
    charset = 12
    off_set = 0
    space = True
    
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hn:p:i:bsc:o:vw:", ["help", "number=", "prefix=", "wordlist=", "charset=", "off_set="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-b":
                brute = True
            if option == "-s":
                space = False
            if option in "-c":
                charset = int(value)
            if option in "-o":
                off_set = int(value)
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-n", "--number"):
                number = int(value)
            if option in ("-w", "--wordlist"):
                global CODEWORDS
                #print "Importing: %s" % value
                CODEWORDS = open(value, 'r').readlines()
            if option in ("-p", "--prefixe"):
                
                print value
                
                if (value):
                    prefix = value
                else:
                    prefix = 'TRUE'
    
        generate(brute, space, charset, off_set, prefix, number)
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())
