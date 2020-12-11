import json
import random
from operator import itemgetter
from itertools import groupby

appsFile = open("apps.txt", 'r')
apps = appsFile.readlines()

for app in apps:
    app = app.rstrip()
    with open("./appReviews/" + app + ".json", "r") as f:
        with open("./app20Reviews/" + app + ".json", "w") as fw:
            data = json.load(f)
            if len(data) < 21 :
                json.dump(data,fw, indent=4)
            else:
                reviews = []
                data = groupby(sorted(data, key=itemgetter('score')),key=itemgetter('score'))
                for x in data:

                    l = list(x[1])

                    if len(l) < 5:
                        reviews.append(list(x[1]))
                    else:
                         num_reviews = 0
                         reviews_left = len(l)
                         review_list =[]
                         while num_reviews < 4 or reviews_left == 0:
                             rand = []
                             i = random.randint(0,(len(l) - 1))
                             while i in rand:
                                 i = random.randint(0,(len(l) - 1))
                             rand.append(i)

                             if len(l[i]['content'])>=50:
                                 review_list.append(i)
                                 num_reviews+=1
                                 reviews.append(l[i])
                             else:
                                 reviews_left -= 1
                         while num_reviews< 4:
                             while i in review_list:
                                 i = random.randint(0,(len(l) - 1))
                             num_reviews += 1
                             reviews.append(l[i])


                json.dump(reviews, fw, indent=4)

appsFile.close()