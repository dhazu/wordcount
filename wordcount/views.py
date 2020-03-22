from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['fulltextarea']
    list_word = data.split()
    list_len = len(list_word)
    word_dict = {}
    for word in list_word:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word] = 1

    sorted_list = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'name':data, 'length':list_len, 'dict':sorted_list})
