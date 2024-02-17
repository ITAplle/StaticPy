# StaticPy

StaticPy is a superset of the Python 3.12 programming language that adds many new features for writing extensible Python code, with powerful typing and code portability. You will not have any inconvenience when switching to this programming language if you understand:
* Object-oriented programming
* Know and are able to apply the concepts of OPP
* Know how OOP works in Python

To get started, take a look at this code:
```python
# Namespace for this file
__namespace__ = 'Теория'
# What will be available when importing this StaticPy module (specifically this one)
__export__ = [Versions, PROJECT_NAME]

# Docstring as Markdown
'''
# This is the main module of SaticPy. It is educational and designed to show what StaticPy syntax looks like
'''

# The function "version" is imported from the standard StaticPy module - "std"
from std import version

# This is what the constants look like
const PROJECT_NAME = 'Learn'
# Enum
enum Versions[str]:
	ALPHA = '0.1'
	BETA = '0.5'
	RELEASE = '1.0'


class Main:
	# Point of entry
	# args: list[str] - this is updated "sys.args"
	static def main(args: list[str]) -> None:
		# Function calls are the same
		print( version() )
		# Variable annotations are required!
		name: str = input('Your name: ')
		# Using Static Class Metas
		Main.__hello(name)
	
	static def __hello(name: str):
		print('Hello ' + name + '!')

```

But that's not all this programming language adds.
Now development is just underway, in the future there will be opportunities here:
1. Fine-tuning the translator
2. Compilation into different programming languages
3. More abstraction for OOP
4. More features for code optimization

At the moment, the code is not available for use, since the language is still at the development stage
