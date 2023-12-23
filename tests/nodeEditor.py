import dearpygui.dearpygui as dpg

def button_callback():
    print("Button clicked!")

with dpg.texture_registry():
    with dpg.create_viewport(title="Basic Dear PyGui App"):
        with dpg.create_window(label="Hello, Dear PyGui!"):
            dpg.add_text("Welcome to Dear PyGui!")
            dpg.add_button(label="Click me", callback=button_callback)

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
