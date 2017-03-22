
class Task(dict):

    def __init__(self, task):
        super(Task, self).__init__()
        self.update(task)

    @property
    def task_status(self):
        return self.get('status')

    @property
    def task_id(self):
        return self.get('task_id')

    @property
    def task_name(self):
        return self.get('task_name')

    @property
    def task_result(self):
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


class TasksClient(object):

    def __init__(self, api):
        self.api = api

    def list(self, wf_id, *args):
        uri = 'tasks/{workflow_id}'.format(workflow_id=wf_id)
        result, status = self.api.get(uri, params=args)
        return [Task(item) for item in result], status

    def get(self, wf_id, task_id):
        pass
