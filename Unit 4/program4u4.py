import glob

path="E:/PYTHON/College/Unit 4"

files=[f for f in glob.glob(path+"**/*.py",recursive=True)]

 

for f in files:

    print(f)