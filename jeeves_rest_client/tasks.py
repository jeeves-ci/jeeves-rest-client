
class Task(dict):

    def __init__(self, task):
        super(Task, self).__init__()
        self.update(task)

    @property
    def status(self):
        return self.get('status')

    @property
    def task_id(self):
        return self.get('task_id')

    @property
    def task_name(self):
        return self.get('task_name')

    @property
    def result(self):
        return self.get('result')

    @property
    def created_at(self):
        return self.get('created_at')

    @property
    def started_at(self):
        return self.get('started_at')

    @property
    def ended_at(self):
        return self.get('date_done')

    @property
    def traceback(self):
        return self.get('traceback')

    @property
    def content(self):
        return self.get('content')

    @property
    def minion_ip(self):
        return self.get('minion_ip')


class TasksClient(object):

    def __init__(self, api):
        self.api = api

    def list(self, wf_id, **kwargs):
        assert wf_id
        uri = 'tasks'
        params = {'workflow_id': wf_id}
        params.update(kwargs)
        result, status = self.api.get(uri, params=params)
        return [Task(item) for item in result], status

    def get(self, wf_id, task_id):
        pass
