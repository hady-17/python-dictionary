def merge_dictionaries(dic1,dic2):
    #create a copy of the first dictionary
    merged=dic1.copy()
    #update with the second dictionary
    merged.update(dic2)
    return merged
def count_word_freq(sent):
    #split sentence provided
    words=sent.split()
    freq_dict={} #create empty dict
    

dict1={"a":1,"b":2,"c":3}
dict2={"b":10,"d":4}

print(merge_dictionaries(dict1,dict2))
