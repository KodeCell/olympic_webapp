import pandas as pd
data = pd.read_csv('C:/Users/anshu.JITENDER-VIG-ME/Desktop/Project/Olympic-webapp/athlete_events.csv')
df = pd.read_csv('C:/Users/anshu.JITENDER-VIG-ME/Desktop/Project/Olympic-webapp/noc_regions.csv')


def preprocessing():

    global data,df


    # merging the datasets

    data1 = pd.merge(data,df,on = 'NOC',how = 'left')


    # dropping the duplicate columns
    data2 = data1.drop_duplicates()


    # encoding the medals i.e. Gold,Silver,Bronze

    data3 =  pd.concat([data2,pd.get_dummies(data2['Medal'])],axis =1 )

    return data3






