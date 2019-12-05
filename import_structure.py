top_folder
	__init__.py
	main.py
	sub1_folder
	    __init__.py
	     client.py
	sub2_folder
	    __init__.py
	    client.py

contents of sub1/client.py:
	g = 'here'

contents of sub2/client.py:
	g = 'here2'

contents of main.py:
  from sub1.client import g
  from sub2.client import h
  print(dir())
  print(g)
  print(h)

run the following in folder top_folder
python main.py
output:
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'g', 'h']
here
here2
