
import json
import unittest

#log = json.load(open("log.json", encoding="utf8"))

#accuracy = log["prediction"]
#elasped_time = log['elasped_time']


class Test(unittest.TestCase) : 

    def test_model_performance(self) : 
        self.assertGreater(accuracy, 0.95)

    def test_elasped_time(self) : 
        self.assertGreater(1e-5, elasped_time)




if __name__ == "__main__" : 
    log = json.load(open("log.json", encoding="utf8"))

    accuracy = log["prediction"]
    elasped_time = log['elasped_time']
    unittest.main()