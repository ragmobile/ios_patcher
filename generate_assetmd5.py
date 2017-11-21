import json
import hashlib
import os
import sys

filesDir = "iOS/resources/script"
iosDir = "iOS"

# ios/iOs
patchedFiles = []



for filename in os.listdir(iosDir):
	if "iOS" in filename:
		filepath = iosDir+"/"+filename
		obj = {}
		obj["FileName"] = filepath
		obj["MD5"] = hashlib.md5(open(filepath,'rb').read()).hexdigest() 
		obj["Size"] = os.path.getsize(filepath)
		patchedFiles.append(obj)

for filename in os.listdir(filesDir):
	if ".unity3d" in filename and "manifest" not in filename:
		filepath = filesDir+"/"+filename
		obj = {}
		obj["FileName"] = filepath
		obj["MD5"] = hashlib.md5(open(filepath,'rb').read()).hexdigest() 
		obj["Size"] = os.path.getsize(filepath)
		patchedFiles.append(obj)

patch = {}
patched = {"Infos":patchedFiles}


patch.update(patched)
patch["ZipFileName"] = sys.argv[1]+".zip"

print json.dumps(patch)    
