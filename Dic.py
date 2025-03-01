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
    for word in words:
        if word in freq_dict:
            freq_dict[word]+=1
        else:
            freq_dict[word]=1
    return freq_dict


dict1={"a":1,"b":2,"c":3}
dict2={"b":10,"d":4}

print(merge_dictionaries(dict1,dict2))


sent="hello my name is hady, hady is my first name , while my last name is kaddourah"
print(count_word_freq(sent))
