import simpleaudio 

wave_obj = sa.WaveObject.from_wave_file("path/to/file.wav")
play_obj = wave_obj.play()
play_obj.wait_done()