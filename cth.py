# class Buah():
#     def jenis(self):
#         print("tropical")
        
    
# class Mangga(Buah):
#     def rasa(self):
#         print("manis")
        
# class Lemon(Buah):
#     def rasa(self):
#         print("asam")
        
# buah_mangga = Mangga()
# buah_lemon = Lemon()

# # for i in (buah_mangga,buah_lemon):
# #     i.rasa()

# class orang():
#     __status = 'human'
#     def __init__(self,name,umur):
#         self.name = name
#         self.__umur = umur
        
#     def setAge(self,umur):
#         self.__umur = umur
        
    
#     def hasil(self):
#         print(self.name)
#         print(self.__umur)
#         print("\n----------")
        

# manusia = orang("yusuf",16)
# print(manusia.__status)
# manusia.hasil()

# manusia.__umur = 50
# manusia.hasil()

# manusia.setAge(30)
# manusia.hasil()

# import threading
# import time

# def dynamic(total_iteration):
    
#     for i in range(total_iteration):
#         print(f"halo dynamic ke {i}")
#         time.sleep(i)
        

# def static(total_iteration):
#     for i in range(total_iteration):
#         print(f"halo static ke {i}")
#         time.sleep(2)
        
        
# if __name__ == '__main__':
#     t1 = threading.Thread(target=dynamic, args=(5,))
#     t2 = threading.Thread(target=static, args=(5,))
    
#     t1.start()
#     t2.start()
    
#     t1.join()
#     t2.join()
    
#     print("selesai")

a = []

b = {}

c = ''


if a is not None:
    print("b")
else:
    print("c")
# print(not a,not b,not c)
    


