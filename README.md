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
You can change `gil=0` to `gil=1` to enable the GIL (global interpreter lock) and see the differences in runtime performance.
