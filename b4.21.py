print('nguyen ngoc chi mssv 245752021610164')
data = input("Nhập chuỗi các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ").split(',')
ket_qua = [x for x in data if int(x, 2) % 5 == 0]
print(','.join(ket_qua))
