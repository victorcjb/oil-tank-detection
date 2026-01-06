import kagglehub

#Download the data from Kaggle using kagglehub 
#Will print output of location of file
path = kagglehub.dataset_download("towardsentropy/oil-storage-tanks")

print("Path to dataset files:", path)


#C:\Users\XXXX\.cache\kagglehub\datasets\towardsentropy\oil-storage-tanks\versions\1