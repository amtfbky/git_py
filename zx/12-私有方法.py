class Dog:
    def __send_msg(self):
        print("-------send duabxin")

    def send_msg(self,new_money):
        if new_money>100:
            self.__send_msg()
        else:
            print('no')

dog=Dog()
dog.send_msg(1001)
