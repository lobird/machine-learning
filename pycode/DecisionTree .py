# -*- coding: utf-8 -*-
"""
Decision Tree                                                            
"""
import numpy as np
import pandas as pd

class DecisionTree():
    def __init__(self):
        self.e = 0.3
        self.tree = {}
    
    def entropy(self,data):
        '''
        计算信息熵
        '''
        count_class = data.groupby(data.iloc[:,-1]).count().iloc[:,0]
        p = count_class / count_class.sum()
        return np.sum(-p*np.log2(p))

    def gain(self,data):
        e = self.entropy(data)
        gain = []
        for col in data.columns[:-1]:
            count_class = data.groupby([data[col],data.iloc[:,-1]]).count()
            count_class = count_class.unstack().iloc[:,0:2].fillna(0)
            p = (count_class.T / count_class.T.sum()).T
            row_entropy = (-p*np.log2(p)).sum(axis=1)
            col_ratio = count_class.sum(axis=1) / count_class.sum().sum()
            col_gain = e - row_entropy.T @ col_ratio
            gain.append([col,col_gain])
        gain = pd.DataFrame(gain).sort_values(by=1,ascending=False)
        return gain.iloc[0].values
    def fit(self, X,y):
        pass

    def predict(self,X):
        pass
    
    def build_tree(self,data,e):
        pass

    def list_div(self,m_list,n_div):
        '''
        list分割
        输入：带分割的list，分割份数
        输出：已分割的list
        '''
        l1 = (m_list - np.min(m_list))
        l2 = (np.max(m_list) - np.min(m_list))
        l = l1/l2*n_div
        return l.astype(int)

    def data_div(self,data,n_div=3):
        '''
        dataframe分割
        输入：待分割的dataframe，分割份数
        输出：分割后的dafaframe
        '''
        for col in data.columns:
            type_d = type(data[col][0])
            count_d = len(np.unique(data[col]))            
            if (type_d is not str) and (count_d > 30) :
                data[col] = self.list_div(data[col],n_div)
        return data

df = pd.read_csv('bank.csv',sep=';')
df = DecisionTree().data_div(df)
divRatio = 0.2
divNumber = int(len(df)*divRatio)
train = df.iloc[:divNumber,:].copy()
test = df.iloc[divNumber:,:].copy()
trainX = train.iloc[:,:-1]
trainy = train.iloc[:,-1]
testX = test.iloc[:,:-1]
testy = test.iloc[:,-1]

dt = DecisionTree()
print(dt.gain((df)))




