print('NGUYEN NGOC CHI MSSV 245752021610164')
#Nhap danh sach cac tu tu ban phim
danh_sach = input("Nhap danh sach cac tu:").split()
#Dao nguoc thu tu cua danh sach
danh_sach.reverse()
#in ra danh sach cac tu dao nguoc
print("Danh sach cac tu sau khi dao nguoc:")
for sach in danh_sach:
    print(sach, end=" ")
