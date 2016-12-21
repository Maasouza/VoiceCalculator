from trainning import *

pastas = ["um","dois","tres","mais","igual"]

vt = VoiceTrainer(record_times = 10,centroid_path="centroid_test")

vt.create_folders(pastas)

vt.generate_centroid_files()

