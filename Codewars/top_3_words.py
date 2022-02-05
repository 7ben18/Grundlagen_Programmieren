def top3_words(text):
    replace_words = ["#","/", "\\", ".",","]
    text = text.lower()
    for x in replace_words:
        text = text.replace(x,"")
    text = text.strip().split()
    dict_count = {}
    for index, value in enumerate(text):
        if value not in dict_count:
            dict_count[value] = 1
        else:
            dict_count[value] += 1

    result = []
    value_list = []
    for key, value in dict_count.items():
            value_list.append(value)
    value_list = sorted(value_list)[-3:]
    for x in value_list:
        for key, nums in dict_count.items():
            if nums == x:
                result.append(key)
    return result

test_list = ["a a a  b  c c  d d d d  e e e e e","e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e","  //wont won't won't ",
             "  , e   .. ","  ...  ","  '  ","  '''  "]

for x in test_list:
    print(x, "->", top3_words(x))