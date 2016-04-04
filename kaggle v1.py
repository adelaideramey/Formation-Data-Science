# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
### KAGGLE TITANIC - Adélaïde Ramey ###

# 0. Import

    #0.1 Library
import os
rep_cour = os.getcwd()
print (rep_cour)

from os import chdir
chdir("C:\\formation Datascience#2")


    #0.2 Packages
import numpy as np
import scipy.stats as stat
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pydot #ne fonctionne pas
from sklearn.externals.six import StringIO  


    #0.3 Database

input=pd.read_csv("train.csv")
input.head()
input.tail()
print ("La table contient : " , len(input) , "lignes et " , input.shape[1] , "colonnes.")
print ("Le type du fichier est :" ,type(input))
input.dtypes

output=pd.read_csv("test.csv")
output.head()
output.head()
output.tail()
print ("La table contient : " , len(output) , "lignes et " , output.shape[1] , "colonnes.")
print ("Le type du fichier est :" ,type(output))
output.dtypes

# 1. Descriptive Analysis
    #1.1 The table
input.columns
input.info()
input.describe()
input.head()

    #1.2 Retraitement des variables
        #drop Name PassengerId 
input["Cabin"].value_counts()
input["PassengerId"].value_counts()
input["Ticket"].value_counts()

todrop= ['PassengerId','Name','Ticket','Cabin']
print(todrop)
input = input.drop(todrop,axis=1)
input.columns

        #Variables catégorielles
input["Survived"]=pd.Categorical(input["Survived"],ordered=False)
input.Survived.dtypes

input["Pclass"].value_counts()
input['Pclass']=input['Pclass'].fillna("3")
input["Pclass"]=pd.Categorical(input["Pclass"],ordered=False)
input.Pclass.dtypes

input["Sex"].value_counts()
input['Sex']=input['Sex'].fillna("male")
input["Sex"]=pd.Categorical(input["Sex"],ordered=False)
input.Sex.dtypes

input["Embarked"].value_counts()
input['Embarked']=input['Embarked'].fillna("S")
input["Embarked"]=pd.Categorical(input["Embarked"],ordered=False)
input.Embarked.dtypes

        #Transformation en indicatrices
indic=pd.get_dummies(input[["Pclass","Sex","Embarked"]])
indic.info()
input=pd.concat([input,indic],axis=1)
input.info()

todrop2 = ['Pclass','Sex','Embarked',]# Pour les arbres, on garde les indicatrices pour les catégorielles
input_tree = input.drop(todrop2,axis=1)
input_tree.info()

        #Variables numériques
input['Age']=input['Age'].fillna(input['Age'].median())
input['SibSp']=input['SibSp'].fillna(input['SibSp'].median())
input['Parch']=input['Parch'].fillna(input['Parch'].median())
input['Fare']=input['Fare'].fillna(input['Fare'].median())

Tr_Age=pd.qcut(input.Age,4,labels=["Ag1","Ag2","Ag3","Ag4"])
input=pd.concat([input,Tr_Age],axis=1)
Tr_Fare=pd.qcut(input.Fare,4,labels=["Fare1","Fare2","Fare3","Fare4"])
input=pd.concat([input,Tr_Fare],axis=1)
indic2=pd.get_dummies(input[["Tr_Age"]])#ne fonctionne pas avec Fare
input_tree=pd.concat([input,indic2],axis=1)
todrop3 = ['Tr_Age']# Pour les arbres, on garde les indicatrices pour les catégorielles
input_tree = input.drop(todrop3,axis=1)


input.info()
input_tree.info()


    #1.3 Analyses univariées
        # Response Variable
train["Survived"]=pd.Categorical(train["Survived"],ordered=False)
train["Survived"].value_counts()

plt.title("Distribution des Survivants")
ptrain.Survived.value_counts().plot.pie( labels=['Non survivants','Survivant'], 
                                        colors=['b', 'g'], 
                                        autopct='%.0f', 
                                        fontsize=10, 
                                        figsize=(3, 3))
   
   
    #1.3 Analyses umultivariées
       #Echantillonage
Expl_var=input_tree.drop(["Survived","Fare","Fare1","Fare2","Fare3","Fare4","Age","Ag1","Ag2","Ag3","Ag4"],axis=1)
Response=input_tree["Survived"]
Train,Test,Response_train,Response_test=train_test_split(Expl_var,Response,test_size=0.3)
Expl_var.info()

#ARBRES DE DECISIONS

#Version classique
tree=DecisionTreeClassifier()
tree_class=tree.fit(Train,Response_train)
    # Estimation de l’erreur de prévision
1-tree_class.score(data_test,surv_test)

#Version avec spécification d'options
tree=DecisionTreeClassifier(max_depth=3)
tree_opt=tree.fit(data_train,surv_train)
    # Estimation de l’erreur de prévision
1-tree_opt.score(data_test,surv_test)
