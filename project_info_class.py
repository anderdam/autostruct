class ProjectInfo:
    def __init__(
        self, project_name, repo_name, author_name, description, open_source_license
    ):
        self._project_name = project_name
        self._repo_name = repo_name
        self._author_name = author_name
        self._description = description
        self._open_source_license = open_source_license

    def get_project_name(self):
        return self._project_name

    def get_repo_name(self):
        return self._repo_name

    def get_author_name(self):
        return self._author_name

    def get_description(self):
        return self._description

    def get_open_source_license(self):
        return self._open_source_license

    def _set_project_name(self, project_name):
        self._project_name = project_name

    def _set_repo_name(self, repo_name):
        self._repo_name = repo_name

    def _set_author_name(self, author_name):
        self._author_name = author_name

    def _set_description(self, description):
        self._description = description

    def _set_open_source_license(self, open_source_license):
        self._open_source_license = open_source_license

    def __str__(self):
        return "Project name: {}\nRepository name: {}\nAuthor name: {}\nDescription: {}\nOpen source license: {}".format(
            self._project_name,
            self._repo_name,
            self._author_name,
            self._description,
            self._open_source_license,
        )
