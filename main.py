from kivy.app import App
from kivy.uix.webview import WebView
import os

class EarnNepalApp(App):
    def build(self):
        # यसले एन्ड्रोइडमा index.html फाइल खोज्छ र खोल्छ
        path = os.path.abspath("index.html")
        webview = WebView(url=f"file://{path}", enable_javascript=True, enable_dom_storage=True)
        return webview

if __name__ == "__main__":
    EarnNepalApp().run()
