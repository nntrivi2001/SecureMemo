from kivy.uix.image import Image
from kivy.core.camera import Camera as CoreCamera
from kivy.properties import NumericProperty, ListProperty, BooleanProperty


# access to camera
core_camera = CoreCamera(index=0, resolution=(1280,1280), stopped=True)

# Widget to display camera
class MyCamera(Image):
    '''Camera class. See module documentation for more information.
    '''

    play = BooleanProperty(True)


    index = NumericProperty(-1)


    resolution = ListProperty([-1, -1])


    def __init__(self, **kwargs):
        self._camera = None
        super(MyCamera, self).__init__(**kwargs)  # `MyCamera` instead of `Camera`
        if self.index == -1:
            self.index = 0
        on_index = self._on_index
        fbind = self.fbind
        fbind('index', on_index)
        fbind('resolution', on_index)
        on_index()

    def on_tex(self, *l):
        self.canvas.ask_update()

    def _on_index(self, *largs):
        if self.index < 0:
            return
        if self.resolution[0] < 0 or self.resolution[1] < 0:
            return

        self._camera = core_camera # `core_camera` instead of `CoreCamera(index=self.index, resolution=self.resolution, stopped=True)`
        self._camera.bind(on_load=self._camera_loaded)

        if self.play:
            self._camera.start()
            self._camera.bind(on_texture=self.on_tex)

    def _camera_loaded(self, *largs):
        self.texture = self._camera.texture
        self.texture_size = list(self.texture.size)

    def on_play(self, instance, value):
        if not self._camera:
            return
        if value:
            self._camera.start()
        else:
            self._camera.stop()
    def update(self, dt):
        super(MyCamera, self).update(dt)
        print('update')
        # frame = self.texture
        # image = cv2.imdecode(numpy.frombuffer(frame.pixels, dtype=numpy.uint8), cv2.IMREAD_COLOR)

        # # Gọi chức năng xác thực khuôn mặt tự động
        # self.auto_face_authentication(image)
