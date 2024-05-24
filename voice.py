import os
import time
import wave
import pygame
import torch
import subprocess
import piper

class VoiceService:
    def __init__(self) -> None:
        self._device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self._output_dir = 'outputs_v2'

        os.makedirs(self._output_dir, exist_ok=True)
    
            
    def piper(self, text):
        # Run the base speaker tts
        try:

            save_path = f'{self._output_dir}/piper2.wav'
            model_path = 'modules/piper/models/'
            model = 'en_US/en_US-libritts_r-medium.onnx'
            
            synthesize_args = {
                "speaker_id": 8,
                "length_scale": 0.9,
            }

            voice = piper.PiperVoice.load(
                model_path=model_path + model,
                config_path=model_path + model + ".json",
                use_cuda=False)

            with wave.open(str(save_path), "wb") as wav_file:
                voice.synthesize(text, wav_file, **synthesize_args)
                
            self.play(save_path)

        finally:
            print("Finished speaking!")        
              
    def play(self, temp_audio_file):
        
        pygame.mixer.init()
        pygame.mixer.music.load(temp_audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # os.remove(temp_audio_file)   