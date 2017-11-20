
# coding: utf-8

# In[2]:


f = open("US_births_1994-2003_CDC_NCHS.csv","r")
text = f.read()
split_lst = text.split("\n")
print(split_lst[0:10])


# In[10]:


def read_csv(file_name):
    f = open(file_name,'r')
    text = f.read()
    split_lst = text.split("\n")
    string_lst = split_lst[1:len(split_lst)]
    final_list = []
    for row in string_lst:
        int_fields = []
        string_fields = row.split(",")
        for value in string_fields:
             int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:10])
             
             


# In[ ]:


def month_births(input_list):
    births_per_month = dict()
    for row in input_list:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return(births_per_month)
cdc_month_births = month_births(cdc_list)
            
            

