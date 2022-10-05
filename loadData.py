import pandas as pd
import datetime
import warnings

class loadData:
    def __init__(self, name, interval):
        self.interval = interval
        self.data = pd.read_csv(name,sep=";",decimal=",")
        self.data.rename(columns={"Unnamed: 0":"timestamp"}, inplace = True)
        self.data.drop('timestamp', axis=1).astype('float64')
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], format='%Y-%m-%d %H:%M:%S')
        self.assertTimestampAreCorrect()

    def assertTimestampAreCorrect(self):

        isError = False
        currentTimestamp = self.data.iloc[0]['timestamp']

        for i in range(len(self.data.iloc[:]['timestamp'])):
            if currentTimestamp != self.data.iloc[i]['timestamp']:
                isError = True
                warnings.warn("Timestamp " + str(self.data.iloc[i]['timestamp']) + " should be " + str(currentTimestamp) + ", please check dataframe !")
            currentTimestamp += datetime.timedelta(minutes=self.interval)

        if isError == False:
            print("--- Timestamp are correct, no errors ---")

        


        