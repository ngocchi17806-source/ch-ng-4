print('NGUYEN NGOC CHI MSSV 245752021610164')
ho_ten = input("Ho ten cua ban la gi:")
#Tim vi tri cua khoang trang( gia su ho va ten chi con cach nhau
#boi mot khoang trang
vi_tri_khoang_trang = ho_ten.find(" ")
#tach ho va ten
ho = ho_ten[:vi_tri_khoang_trang]
ten = ho_ten[vi_tri_khoang_trang+1:]
#in ra ket qua
print("Ho:",ho)
print("Ten:",ten)
