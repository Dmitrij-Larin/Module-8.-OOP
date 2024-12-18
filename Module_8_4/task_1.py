class PowerUnit:

    def __init__(self, power):
        self.__power = power

    def get_power(self):
        return self.__power

    def apply_power(self):
        on_power = input("Введите \"on\", чтоб включить компьютер: ")
        if on_power == "on":
            return f"Компьютер включился. Мощность - {self.__power} Вт.\nВходное напряжение - 220 В.\n"
        else:
            print("Компьютер отключен.")
            exit()


class Motherboard:

    def __init__(self, chipset):
        self.__chipset = chipset

    def get_chipset(self):
        return self.__chipset

    def info_motherboard(self):
        return f"Материнская плата с чипсетом {self.__chipset}."

    def power_input(self):
        power = input("Введите \"on\", чтоб перераспределить мощность по компонентам: ")
        if power == "on":
            return "Мощность распределина по компонентам.\n"
        else:
            print("Компьтер не исправлен!")
            exit()


class CPU:

    def __init__(self, clock_speed, num_cores):
        self.__clock_speed = clock_speed
        self.__num_cores = num_cores

    def get_clock_speed(self):
        return self.__clock_speed

    def get_num_cores(self):
        return self.__num_cores

    def info_cpu(self):
        return (f"Центральный процессор с тактовой частотой {self.__clock_speed} МГц.\n"
                f"Количество ядер - {self.__num_cores}")

    def turbo_mode(self):
        turbo_boost = input("Введите \"on\", чтоб включить турбо режим: ")
        if turbo_boost == "on":
            return (f"Турбо режим активирован\n"
                    f"Тактовая частота процессора при разгоне - {self.__clock_speed + 600} МГц.\n")
        else:
            return "Турбо режим отключен.\n"


class RAM:

    def __init__(self, amount_of_ram, frequency_of_ram):
        self.__amount_of_ram = amount_of_ram
        self.__frequency_of_ram = frequency_of_ram

    def get_amount_of_ram(self):
        return self.__amount_of_ram

    def get_frequency_of_ram(self):
        return self.__frequency_of_ram

    def info_ram(self):
        return f"Оперативная память объёмом {self.__amount_of_ram} Гб и частотой {self.__frequency_of_ram} МГц."

    def download_data(self, memory_data):
        data = input("Введите \"on\", чтоб загрузить данные: ")
        if data == "on":
            return f"Данные объёмом {memory_data} Гб загруженны."
        else:
            return "Ошибка! Не удалось загрузить данные."

    def upload_data(self, memory_data):
        data = input("Введите \"on\", чтоб выгрузить данные: ")
        if data == "on":
            return f"Данные объёмом {memory_data} Гб выгруженны.\n"
        else:
            return "Ошибка! Не удалось выгрузить данные.\n"


class SSD:

    def __init__(self, amount_of_ssd):
        self.__amount_of_ssd = amount_of_ssd

    def get_amount_of_ssd(self):
        return self.__amount_of_ssd

    def info_ssd(self):
        return f"SSD с объёмом памяти {self.__amount_of_ssd} Гб."

    def save_data(self, memory):
        data = input("Введите \"on\", чтоб сохранить данные: ")
        if data == "on":
            return f"Данные объёмом {memory} Гб успешно сохраненны."
        else:
            return "Ошибка! Данные не удалось сохранить."

    def delete_data(self, memory):
        data = input("Введите \"on\", чтоб удалить данные: ")
        if data == "on":
            return f"Данные объёмом {memory} Гб успешно удаленны.\n"
        else:
            return "Ошибка! Данные не удалось удалить.\n"


class VideoCard:

    def __init__(self, model, amount_video_card):
        self.__model = model
        self.__amount_video_card = amount_video_card

    def get_model(self):
        return self.__model

    def get_amount_video_card(self):
        return self.__amount_video_card

    def info_video_card(self):
        return f"Видеокарта {self.__model} объёмом памети {self.__amount_video_card} Гб."

    def image_output(self):
        image = input("Введите \"on\", чтоб вывести изображение на экран: ")
        if image == "on":
            return "Изображение выведенно на экран."
        else:
            return "Не удалось вывести изображение."


class PC(PowerUnit, Motherboard, CPU, RAM, SSD, VideoCard):

    def __init__(self, power, chipset, clock_speed, num_cores, amount_of_ram, frequency_of_ram, amount_of_ssd, model,
                 amount_video_card):
        PowerUnit.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, clock_speed, num_cores, )
        RAM.__init__(self, amount_of_ram, frequency_of_ram)
        SSD.__init__(self, amount_of_ssd)
        VideoCard.__init__(self, model, amount_video_card)


pc = PC(700, "Intel", 4800, 10, 32, 3200, 1500, "GeForce RTX 3060 Ti", 8)

print(pc.apply_power())
print(pc.info_motherboard())
print(pc.power_input())
print(pc.info_cpu())
print(pc.turbo_mode())
print(pc.info_ram())
print(pc.download_data(3))
print(pc.upload_data(2))
print(pc.info_ssd())
print(pc.save_data(14))
print(pc.delete_data(25))
print(pc.info_video_card())
print(pc.image_output())
