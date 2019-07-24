class Car:
    def fuel(self):
        print('The future is electric')

    def continent(self):
        print('You can overwrite me anytime..!!')


class Tesla(Car):
    def fuel(self):
        print('I am electric..!!')

    # def continent(self):
    #     print('North America')


class Toyota(Car):
    def fuel(self):
        print('I run on fossil fuels')

    def continent(self):
        print('While world is my base till now..!!')


def func(obj):
    obj.fuel()
    obj.continent()


obj_tesla = Tesla()
obj_toyota = Toyota()

func(obj_tesla)
func(obj_toyota)
