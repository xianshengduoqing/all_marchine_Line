# -*- coding: utf-8 -*-
# user lj

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
news = fetch_20newsgroups(subset='all')
X_train, X_test, y_train, y_test = train_test_split(news.data,news.target,test_size=0.25)
print(X_train[0])
#数据标准化处理
cv = CountVectorizer()
X_train = cv.fit_transform(X_train)
X_test = cv.transform(X_test)
#创建模型
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
print("得分：")
print(mnb.score(X_test,y_test))