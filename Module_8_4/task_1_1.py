from task_1 import PowerUnit, Motherboard, CPU, RAM, SSD, VideoCard


class PC:

    def __init__(self, power, chipset, clock_speed, num_cores, amount_of_ram, frequency_of_ram, amount_of_ssd, model,
                 amount_video_card):
        self.power_unit = PowerUnit(power)
        self.motherboard = Motherboard(chipset)
        self.cpu = CPU(clock_speed, num_cores)
        self.ram = RAM(amount_of_ram, frequency_of_ram)
        self.ssd = SSD(amount_of_ssd)
        self.video_card = VideoCard(model, amount_video_card)

    def pc_apply_power(self):
        return self.power_unit.apply_power()

    def pc_info_motherboard(self):
        return self.motherboard.info_motherboard()

    def pc_power_input(self):
        return self.motherboard.power_input()

    def pc_info_cpu(self):
        return self.cpu.info_cpu()

    def pc_turbo_mode(self):
        return self.cpu.turbo_mode()

    def pc_info_ram(self):
        return self.ram.info_ram()

    def pc_download_data(self):
        return self.ram.download_data(4)

    def pc_upload_data(self):
        return self.ram.upload_data(2)

    def pc_info_ssd(self):
        return self.ssd.info_ssd()

    def pc_save_data(self):
        return self.ssd.save_data(10)

    def pc_delete_data(self):
        return self.ssd.delete_data(17)

    def pc_info_video_card(self):
        return self.video_card.info_video_card()

    def pc_image_output(self):
        return self.video_card.image_output()


pc = PC(650, "AMD B450", 3700, 6, 16, 3200, 512, "NVIDIA GeForce RTX 3050", 8)

print(pc.pc_apply_power())
print(pc.pc_info_motherboard())
print(pc.pc_power_input())
print(pc.pc_info_cpu())
print(pc.pc_turbo_mode())
print(pc.pc_info_ram())
print(pc.pc_download_data())
print(pc.pc_upload_data())
print(pc.pc_info_ssd())
print(pc.pc_save_data())
print(pc.pc_delete_data())
print(pc.pc_info_video_card())
print(pc.pc_image_output())
