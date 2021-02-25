from cx_Freeze import setup, Executable

setup(name="Counter_Test",
    version="0.1",
    description="",
    executables = [Executable("counter.py")])