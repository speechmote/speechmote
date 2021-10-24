import requests
f1 = open("c:/Users/rjain/Documents/Projects/speechmote/src/model/sample.wav", errors="ignore")
f2 = open("c:/Users/rjain/Documents/Projects/speechmote/src/model/groot3.wav", errors="ignore")
textfile = open("c:/Users/rjain/Documents/Projects/speechmote/src/model/test.txt", "r")
url = "https://speechmote-329915.ue.r.appspot.com/uploadfile/"

pain = open("i'mdying.txt", "x")
file_dict = {"file1": f1, "file2": f2}
response = requests.post(url, files = file_dict)
print(response)
