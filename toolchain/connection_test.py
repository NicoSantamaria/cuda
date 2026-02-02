from jupyter_client import BlockingKernelClient


kc = BlockingKernelClient()
kc.load_connection_file("/Users/nicosantamaria/Projects/parallean/src/cocupy/toolchain/connection.json")
kc.start_channels()
kc.wait_for_ready()

# Now execute code on that remote kernel
kc.execute("print('Hello from Colab!')")