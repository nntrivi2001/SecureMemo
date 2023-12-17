import cv2
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file('kv_files\\continuous_capture.kv')

class ContinuousCaptureLayout(BoxLayout):
    def detect_face(self, instance, texture):
        frame = np.frombuffer(texture.pixels, dtype=np.uint8).reshape((texture.height, texture.width, 4))
        # ... (code phát hiện khuôn mặt)

    def start_continuous_capture(self, instance):
        instance.text = 'Capturing...'
        self.ids.capture_label.text = 'Capturing...'
        self.capture_images(30)

    def capture_images(self, num_images):
        for i in range(num_images):
            Clock.schedule_once(lambda dt: self.capture_frame(), i * 0.5)

    def capture_frame(self):
        texture = self.ids.camera.texture
        if texture:
            frame = np.frombuffer(texture.pixels, dtype=np.uint8).reshape((texture.height, texture.width, 4))
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
            cv2.imwrite(f'captured_image_{self.capture_counter}.jpg', frame_bgr)
            print(f"Captured image {self.capture_counter}")
            self.capture_counter += 1
            self.ids.capture_label.text = f'Captured {self.capture_counter}/{30} images.'

class ContinuousCaptureApp(App):
    def build(self):
        return ContinuousCaptureLayout()

if __name__ == '__main__':
    ContinuousCaptureApp().run()
