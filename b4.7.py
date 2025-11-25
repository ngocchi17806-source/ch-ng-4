print('NGUYEN NGOC CHI MSSV 245752021610164')
chuoi = input("Nhap chuoi: ")
chuoi_moi = ""
for ky_tu in chuoi :
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu
print("Chuoi moi: ", chuoi_moi)
