## Code Example Run Instructions
Make sure you have at least Python 3.13 installed as that is when Python added the ability to disable the GIL (global interpreter lock).
You can just change the 3.14t to 3.13t if you are running on Python 3.13 when installing the multithreaded build.
### Install UV
```{bash}
pip install uv
```
### Install Python 3.14t
```{bash}
python -m uv python install 3.14t
```
### Run Either File
```{bash}
python -m uv run --python 3.14t python -X gil=0 .\GILExperimentCPUBound.py
```
```{bash}
python -m uv run --python 3.14t python -X gil=0 .\GILExperimentIOBound.py
```
You can change `gil=0` to `gil=1` to enable the GIL (global interpreter lock) and see the difference in runtime performance.
