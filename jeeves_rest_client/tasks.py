
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


class Tasks(dict):

    def __init__(self, tasks):
        super(Tasks, self).__init__()
        self.update(tasks)

    @property
    def page(self):
        return self.get('page')

    @property
    def size(self):
        return self.get('size')

    @property
    def total(self):
        return self.get('total')

    @property
    def tasks(self):
        return [Task(item) for item in self.get('tasks')]


class TasksClient(object):

    def __init__(self, api):
        self.api = api

    def list(self, wf_id, page=1, size=100, **kwargs):
        assert wf_id
        uri = 'workflow/{}/tasks'.format(wf_id)
        params = {'page': page,
                  'size': size}
        params.update(kwargs)
        result, status = self.api.get(uri, params=params)
        return Tasks(result), status

    def get(self, wf_id, task_id):
        pass
