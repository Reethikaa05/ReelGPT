from gui.gui_gradio import ShortGptUI

if __name__ == "__main__":
    app = ShortGptUI(colab=True)
    app.launch()
