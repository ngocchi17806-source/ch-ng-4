print('NGUYEN NGOC CHI MSSV 245752021610164')
def tim_tu_dai_nhat(danh_sach_tu):
    """Tim va in ra cac tu dai nhat trong mot danh sach cac tu."""
    #Kiem tra neu danh sach trong
    if not danh_sach_tu:
        print("Danh sach trong! Khong co tu nao de tim.")
        return
    #Tim do dai lon nhat cua cac tu
    do_dai_lon_nhat = max(len(tu) for tu in danh_sach_tu)
    #In ra cac tu co do dai bang do dai lon nhat
    print("Cac tu dai nhat:")
    for tu in danh_sach_tu:
        if len(tu) == do_dai_lon_nhat:
            print(tu)
#Nhap danh sach cac tu tu ban phim
danh_sach_tu = input("Nhap danh sach cac tu:").split()
#Goi ham de tim va in ra cac tu dai nhat
tim_tu_dai_nhat(danh_sach_tu)
