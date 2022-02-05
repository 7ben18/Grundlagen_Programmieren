def get_url(url):
    result = []
    if "http://www." in url:
        word = url[11:]
        for i in word:
            if i == ".":
                break
            else:
                result.append(i)
    elif "https://www." in url:
        word = url[12:]
        for i in word:
            if i == ".":
                break
            else:
                result.append(i)
    elif "http://" in url:
        word = url[7:]
        for i in word:
            if i == ".":
                break
            else:
                result.append(i)
    elif "https://" in url:
        word = url[8:]
        for i in word:
            if i == ".":
                break
            else:
                result.append(i)
    elif "www." in url:
        word = url[4:]
        for i in word:
            if i == ".":
                break
            else:
                result.append(i)
    else:
        for i in url:
            if i == ".":
                break
            else:
                result.append(i)

    return "".join(result)

test_list = ["http://www.zombie-bites.com","https://youtube.com","www.xakep.ru","http://google.co.jp","codewars.com"]

for x in test_list:
    print(x, get_url(x))

#codewars solution
def get_url2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]