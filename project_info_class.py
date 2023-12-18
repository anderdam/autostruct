class ProjectInfo:
    def __init__(
        self, project_name, repo_name, scope, author_name, description, open_source_license
    ):
        self._project_name = project_name
        self._scope = scope
        self._repo_name = repo_name
        self._author_name = author_name
        self._description = description
        self._open_source_license = open_source_license

    @property
    def project_name(self):
        return self._project_name

    @property
    def scope(self):
        return self._scope

    @property
    def repo_name(self):
        return self._repo_name

    @property
    def author_name(self):
        return self._author_name

    @property
    def description(self):
        return self._description

    @property
    def open_source_license(self):
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
        return "Project name: {}\n" \
               "Scope: {}\n" \
               "Repository name: {}\n" \
               "Author name: {}\n" \
               "Description: {}\n" \
               "Open source license: {}"\
            .format(
                self._project_name,
                self._scope,
                self._repo_name,
                self._author_name,
                self._description,
                self._open_source_license,
                )
