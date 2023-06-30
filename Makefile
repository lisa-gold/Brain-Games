install: #poetry install
	poetry install

brain-games: #run brain-games
	poetry run brain-games

build: # собрать пакет
	poetry build

publish: # публикация пакета без добавления его в  каталог PyPI
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install --user dist/*.whl

