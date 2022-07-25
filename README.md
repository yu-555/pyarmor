# 1. install the pyarmor library

```cmd
(yourenv)$ pip install pyarmor 
```

# 2. Compile the specific my python file
```cmd
(yourenv)$ pyarmor obfuscate sample.py
```

# 3. created a py file like below the code in the dist folder 

```python
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x06\x0f.........')
```

Note;
The dist file store the same folder that you type the using python script.

