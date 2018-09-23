import json


class Workflow(dict):

    def __init__(self, workflow):
        # super(Workflow, self).__init__()
        self.update(workflow)

    @property
    def status(self):
        return self.get('status')

    @property
    def workflow_id(self):
        return self.get('workflow_id')

    @property
    def started_at(self):
        return self.get('started_at')

    @property
    def ended_at(self):
        return self.get('ended_at')


class Workflows(dict):

    def __init__(self, workflows):
        # super(Workflow, self).__init__()
        self.update(workflows)

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
    def workflows(self):
        return [Workflow(item) for item in self.get('workflows')]


class WorkflowsClient(object):
    def __init__(self, api):
        self.api = api

    def list(self, page=1, size=10, **kwargs):
        uri = 'workflows'
        params = {'page': page,
                  'size': size}
        params.update(kwargs)
        result, status = self.api.get(uri, params=params)
        return Workflows(result), status

    def get(self, workflow_id, **kwargs):
        assert workflow_id
        uri = 'workflow'
        params = {'workflow_id': workflow_id}
        params.update(kwargs)
        result, status = self.api.get(uri,
                                      params=params)
        return Workflow(result), status

    def terminate(self, workflow_id, **kwargs):
        assert workflow_id
        uri = 'workflow'
        params = {'workflow_id': workflow_id}
        params.update(kwargs)
        result, status = self.api.delete(uri,
                                         params=params)
        return Workflow(result), status

    def upload(self, workflow, env, workflow_id=None, execute=None, **kwargs):
        uri = 'workflow'
        if not env:
            env = {}
        data = {'workflow': workflow,
                'env': env}
        params = {'workflow_id': workflow_id,
                  'execute': execute}
        params.update(kwargs)
        result, status = self.api.post(uri,
                                       params=params,
                                       data=json.dumps(data))
        return Workflow(result), status
