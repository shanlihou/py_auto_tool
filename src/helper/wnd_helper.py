from cffi import FFI
import const


class WndHelper(object):
    def __init__(self, dllname, process_name, class_name, pic_path) -> None:
        super().__init__()
        self.dllname = dllname
        self.process_name = process_name
        self.class_name = class_name
        self.lib = None
        self.hwnd = None
        self.ffi = None

        self.load_dll()
        self.get_wnd()

    def load_dll(self):
        ffi = FFI()
        ffi.cdef("""
            int generate_pic(const char* windName, const char* className);
            int capture_wnd(long long wnd, const char* pathName);
            long long get_wnd(const char* windName, const char* className, int findState);        
            int click(long long wnd, int x, int y);
        """)

        self.lib = ffi.dlopen(self.dllname)
        self.ffi = ffi

    def get_wnd(self):
        self.hwnd = self.lib.get_wnd(self.process_name.encode('utf-8'), self.class_name.encode('utf-8'), 0)
        print(self.hwnd)
        
    def capture(self):
        self.lib.capture_wnd(self.ffi.cast('long long', self.hwnd), const.SCREEN_PATH.encode('utf-8'))

    def click(self, x, y):
        self.lib.click(self.ffi.cast('long long', self.hwnd), x, y)


