import sys

general_lexicon = sys.argv[1]
wordlist = sys.argv[2]
output_file = sys.argv[3]

with open(general_lexicon) as lex:
    with open(wordlist) as wlist:
        with open(output_file,'w') as ofiles:
            gen_lex = {}
            for line in lex:
                cline = line.rstrip()
                line_info =cline.split(" ")
                word =line_info[0]
                pronunciation = " ".join(line_info[1:])
                if word in gen_lex:
                    gen_lex[word] = gen_lex[word].append(pronunciation)
                else:
                    gen_lex[word] = [pronunciation]    
                
            for line in wlist:
                word = line.rstrip()
                if word in gen_lex:
                    for pron in gen_lex[word]:
                        ofiles.write("{} {}\n".format(word, pron))
                else: 
                    print("Unknown pronunciation for word: {}".format(word))

