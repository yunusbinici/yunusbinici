//Created by Yunus

import hashlib as hasher
password= hasher.sha1() 
"""buraya istediğiniz hash algoritmasını girebilirsiniz(sha255,md5 vs....)"""
word= input("hashlenmesini istediğiniz metni giriniz: ")
sifre.update(word.encode("utf-8"))
"""türkçe karakter eklenmesi"""
hash= password.hexdigest()
print(hash)
