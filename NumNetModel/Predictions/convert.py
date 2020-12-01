#In NumNet the prediced output is in JSON format,
#so need to convert in to JSONL format to run evaluate.py to get scores
#Program for converting JSON to JSONL
import json
with open("prediction_stage3_test_stage3.json") as f:
    data = json.load(f)
    for key in data:
        file_write =  open("prediction_stage3_test_stage3_converted.json","a")
        #file_write.write("{"+"Id"+":"+key+"," + "Answer"+":"+data[key]+"}"+"\n")
        file_write.write("{"+"\""+"Id"+"\""+":"+"\""+str(key)+"\""+","+"\""+"Answer"+"\""+":"+"\""+str(data[key])+"\""+"}"+"\n")