.PHONY: clean data lint create_environment
# sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

RAW_DATA_DIR = {{ cookiecutter.raw_data_directory }}
PREPROC_DATA_DIR = {{ cookiecutter.preprocessed_data_directory }}
RESULTS_DATA_DIR = {{ cookiecutter.results_data_directory }}
INTERM_DATA_DIR = {{ cookiecutter.intermediate_data_directory }}
METADATA_DIR = {{ cookiecutter.metadata_directory }}
DEPTH_DIR = {{ cookiecutter.depth_directory_structure}}

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 src

## Set up python interpreter environment
create_environment:
	echo "running"
	conda env create -f environment.yml


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Generate directory structures
data_dirs:
	# make raw data folder readonly
	chmod -R 555 ${RAW_DATA_DIR}
	chmod -R 555 ${METADATA_DIR}

	rm -rf ${PREPROC_DATA_DIR}
	rm -rf ${RESULTS_DATA_DIR}
	rm -rf ${INTERM_DATA_DIR}

	mkdir -p ${PREPROC_DATA_DIR}
	mkdir -p ${RESULTS_DATA_DIR}
	mkdir -p ${INTERM_DATA_DIR}

	cd ${RAW_DATA_DIR} ;  find . -maxdepth ${DEPTH_DIR} -print0 | cut -c 2- | xargs -0 tar cnf - | \
		(cd ${PREPROC_DATA_DIR} ; tar xvvkf -)
	chmod -R 755 ${PREPROC_DATA_DIR}

	cd ${RAW_DATA_DIR} ;  find . -maxdepth ${DEPTH_DIR} -print0 | cut -c 2- | xargs -0 tar cnf - | \
		(cd ${RESULTS_DATA_DIR} ; tar xvvkf -)
	chmod -R 755 ${RESULTS_DATA_DIR}

	cd ${RAW_DATA_DIR} ;  find . -maxdepth ${DEPTH_DIR} -print0 | cut -c 2- | xargs -0 tar cnf - | \
		(cd ${INTERM_DATA_DIR} ; tar xvvkf -)
	chmod -R 755 ${INTERM_DATA_DIR}

	# for d in $(find ${RESULTS_DATA_DIR} -maxdepth ${DEPTH_DIR} -type d); do echo ${d}/results ; done
	# find ${RESULTS_DATA_DIR} -maxdepth ${DEPTH_DIR} -type d -exec sh -c "file='$$0'; mkdir '$${file}'/results" {} ';'
	find ${RESULTS_DATA_DIR} -maxdepth ${DEPTH_DIR} -type d -exec mkdir {}/results ';'
	find ${RESULTS_DATA_DIR} -maxdepth ${DEPTH_DIR} -type d -exec mkdir {}/figures ';'

	rm -rf data/raw && ln -sf ${RAW_DATA_DIR} data/raw
	rm -rf data/preprocessed && ln -sf ${PREPROC_DATA_DIR} data/preprocessed
	rm -rf data/intermediate && ln -sf ${INTERM_DATA_DIR} data/intermediate
	rm -rf data/results && ln -sf ${RESULTS_DATA_DIR} data/results
	rm -rf data/metadata && ln -sf ${METADATA_DIR} data/metadata


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>

.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
