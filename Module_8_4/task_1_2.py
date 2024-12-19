from task_1 import PowerUnit, Motherboard, CPU, RAM, SSD, VideoCard


class PC:

    def __init__(self, pc_power_unit, pc_motherboard, pc_cpu, pc_ram, pc_ssd, pc_video_card):
        self.power_unit = pc_power_unit
        self.motherboard = pc_motherboard
        self.cpu = pc_cpu
        self.ram = pc_ram
        self.ssd = pc_ssd
        self.video_card = pc_video_card


power_unit = PowerUnit(650)
motherboard = Motherboard("AMD B450")
cpu = CPU(3700, 6)
ram = RAM(16, 3200)
ssd = SSD(512)
video_card = VideoCard("NVIDIA GeForce RTX 3050", 8)

pc = PC(power_unit, motherboard, cpu, ram, ssd, video_card)

print(pc.power_unit.apply_power())
print(pc.motherboard.info_motherboard())
print(pc.motherboard.power_input())
print(pc.cpu.info_cpu())
print(pc.cpu.turbo_mode())
print(pc.ram.info_ram())
print(pc.ram.download_data(2))
print(pc.ram.upload_data(4))
print(pc.ssd.info_ssd())
print(pc.ssd.save_data(20))
print(pc.ssd.delete_data(41))
print(pc.video_card.info_video_card())
print(pc.video_card.image_output())