from threading import Thread, current_thread

"""function based threading"""


# # function to be executed parallaly
# def display(n,msg):
#     print("r1 thread details:",current_thread().ident)
#     for char in range(n):
#         print(msg)

# # create new thread
# r1= Thread(target=display, args=(4,"hi"))

# # start the thread
# r1.start()
# print("r1 thread details:",current_thread().name)


# #with args

# # function to be executed parallaly
# def display(n):
#     print("r1 thread details:",current_thread().ident)
#     for a in range(n):
#         print("Rahul")

# # create new thread
# r1= Thread(target=display, args=(4,))                   #  need to pass values in tuple , incase if you pass as (5) it will consider as int, so with comma it treat as tuple.

# # start the thread
# r1.start()



# #with kwargs

# def display(n,msg):
#     print("r1 thread details:",current_thread().ident)
#     for b in range(n):
#         print(msg)

# # create new thread
# r1= Thread(target=display, kwargs={'n':4,'msg':"bro"})                  

# # start the thread
# r1.start()




"""class based threading"""

# class Example:
#     def display(self):
#         for i  in range(5):
#             print("hello")

# e1= Example()   # create a object of class
# t1 = Thread(target=e1.display)    # access method through class object. 
# t1.start()
# for i in range(5):
#     print("Rahul")




# class Example:
#     @classmethod
#     def display(self):
#         for i  in range(5):
#             print("hello")

# e1= Example()   # create a object of class
# t1 = Thread(target=Example.display)    # access method through class object. 
# t1.start()
# for i in range(5):
#     print("Rahul")



# class Example:
#     @staticmethod
#     def display():
#         for i  in range(5):
#             print("hello")

# e1= Example()   # create a object of class
# t1 = Thread(target=Example.display)    # access method through class object. 
# t1.start()
# for i in range(5):
#     print("Rahul")




"""creating threading by extending Thread class"""

from time import sleep
# videos = ['oop syllabus', 'constructore', 'file handling']


# class Myclass(Thread):
#     def run(self):
#         for video in videos:
#             print(f"{video} started uploading...")
#             sleep(3)
#             print(f"{video} uploaded")

# t1 = Myclass()
# t1.start()

# # def upload_videos(vid ):
# #     print(f"{vid} started uploading")
# #     sleep(3)
# #     print(f"{vid} uplaoded")

# for i in range(3):
#     sleep(2)
#     print("Checking Copyrights")



"""with constructor"""

videos = ['oop syllabus', 'constructore', 'file handling']


class Myclass(Thread):
    def __init__(self):
        print("constructor called")
        Thread.__init__(self)
    def run(self):
        for video in videos:
            print(f"{video} started uploading...")
            sleep(13)
            print(f"{video} uploaded")

t1 = Myclass()
t1.start()

# def upload_videos(vid ):
#     print(f"{vid} started uploading")
#     sleep(3)
#     print(f"{vid} uplaoded")

for i in range(3):
    sleep(1)
    print("Checking Copyrights")

