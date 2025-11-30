print('NGUYEN NGOC CHI 245752021610164')
#nhap chuoi tu ban phim
input_string = input("Nhap chuoi cac tu tieng Anh:")
#tach chuoi thanh danh sach cac tu
words = input_string.split()
#sap xep danh sach cac tu theo thu tu
sorted_words = sorted(words)
#in ra cac tu theo thu tu
print("Cac tu theo thu tu:")
for word in sorted_words:
    print(word)
