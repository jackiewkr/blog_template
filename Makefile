update:
	python generate_blogposts.py
	python generate_sidebar.py
	neocities push --prune .
