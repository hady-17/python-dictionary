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
def count_total_employees(comEmp):
    total=0
    for dep in comEmp.values():
        total+=len(dep)
    return total

def invert_dic(org_dic):
    #creating new dic 
    inverted_dic={}
    for key,value in org_dic.items():
        #if value in dic we add the key to the array 
        if value in inverted_dic:
            inverted_dic[value].append(key)
        #else value is created as key
        else:
            inverted_dic[value]=[key]
    return inverted_dic
    
dict1={"a":1,"b":2,"c":3}
dict2={"b":10,"d":4}

print(merge_dictionaries(dict1,dict2))


sent="hello my name is hady , hady is my first name , while my last name is kaddourah"
print(count_word_freq(sent))


company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print(count_total_employees(company_employees))

orginal_dic={"a":10,"b":20,"c":10,"d":30}
print(invert_dic(orginal_dic))