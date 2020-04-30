# -*- coding: utf-8 -*-
# user lj

00
"""
预测评估标准
mae,mse rmse,mape(一般认为其值小于10时，预测精度较高)
==========================================
分类评估标准
   P       N
P  TP      FN

N  FP      TN
预测准确的个数/总预测个数 （得分即正确率）
两种办法
model.score(x_test,y_test):
accuracy_score(y_test,y_predict)
精度：precision=TP/（TP+FP） （预测对的正列/所有预测为正的正例）
召回率  所有正例中 被预测为正的正例  TP/TP+FN
3）灵敏度（sensitive）
　　sensitive = TP/P(实际为正)，表示的是所有正例中被分对的比例，衡量了分类器对正例的识别能力；
=============================================
ROC曲线
纵轴 真阳性率  TP/TP+FN  (召回率)
横轴 假阳性率  FP/FP+TN  （）

"""
#代码实现
import numpy as np
from sklearn import metrics
metrics.mean_squared_error() #mse
metrics.mean_absolute_error()#mae
metrics.accuracy_score()
# MAPE和SMAPE需要自己实现
def mape(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100

def smape(y_true, y_pred):
    #当真实值有数据等于0，而预测值也等于0时，存在分母0除问题，该公式不可用！
    return 2.0 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))) * 100
    sigm(  (ypre-y)/avg(ypre+y)    )