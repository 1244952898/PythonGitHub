gbk_str='demo'.encode('gbk')
utf_8_str=gbk_str.decode('gbk').encode('utf-8')

print(gbk_str)
print(utf_8_str)
